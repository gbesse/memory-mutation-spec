"""Offline transition-by-transition memory contract runner."""
import copy
import json
import subprocess
import sys
from pathlib import Path


def oracle(scenario):
    state = copy.deepcopy(scenario['initial'])
    snapshots = []
    for operation in scenario['operations']:
        key = operation['id']
        kind = operation['op']
        if kind == 'put':
            state[key] = {'text': operation['text'], 'tags': operation.get('tags', [])}
        elif kind == 'update':
            if key not in state:
                raise ValueError(f'unknown id: {key}')
            state[key]['text'] = operation['text']
            if 'tags' in operation:
                state[key]['tags'] = operation['tags']
        elif kind == 'delete':
            state.pop(key, None)
        elif kind == 'invalid_delta':
            pass  # Rejected delta must leave state unchanged.
        else:
            raise ValueError(f'unknown operation: {kind}')
        snapshots.append(copy.deepcopy(state))
    return snapshots


def check(scenario):
    expected = oracle(scenario)
    command = scenario['adapter_command']
    proc = subprocess.run(command, input=json.dumps(scenario), text=True, capture_output=True,
                          timeout=10, check=False)
    if proc.returncode:
        return {'ok': False, 'findings': [f'adapter exited {proc.returncode}: {proc.stderr.strip()[:300]}']}
    try:
        actual = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {'ok': False, 'findings': ['adapter did not return JSON']}
    if not isinstance(actual, list) or len(actual) != len(expected):
        return {'ok': False, 'findings': [f'expected {len(expected)} state snapshots']}
    findings = []
    for index, (want, got) in enumerate(zip(expected, actual), 1):
        if want != got:
            findings.append(f'operation {index} ({scenario["operations"][index-1]["op"]}): state mismatch; expected {want}, got {got}')
    return {'ok': not findings, 'operations': len(expected), 'findings': findings}


def check_observations(data):
    """Check captured transitions without claiming to execute Hindsight itself."""
    findings = []
    for index, event in enumerate(data['events'], 1):
        kind = event['kind']
        if kind == 'consolidation_update':
            before = set(event['before_tags'])
            after = set(event['after_tags'])
            allowed = set(event.get('explicitly_removed_tags', []))
            lost = sorted(before - after - allowed)
            if lost:
                findings.append(f'event {index}: tags lost without explicit removal: {lost}')
        elif kind == 'delta_refresh':
            skipped = event['operations_skipped']
            if skipped and event['outcome'] == 'content_written' and event['is_stale'] is False:
                findings.append(f'event {index}: {len(skipped)} skipped delta operation(s) reported as clean refresh')
        else:
            raise ValueError(f'event {index}: unsupported kind {kind}')
    return {'ok': not findings, 'events': len(data['events']), 'findings': findings}


def main():
    if len(sys.argv) < 2:
        raise SystemExit('usage: tool.py demo | check SCENARIO.json | observation-demo | check-observations FILE.json')
    if sys.argv[1] in ('observation-demo', 'check-observations'):
        base = Path(__file__).parent / 'examples'
        if sys.argv[1] == 'observation-demo':
            bad = check_observations(json.loads((base / 'hindsight-observations.json').read_text()))
            good = check_observations(json.loads((base / 'hindsight-observations-fixed.json').read_text()))
            print(json.dumps({'reported_transitions': bad, 'fixed_transitions': good}, indent=2))
            return 0 if not bad['ok'] and good['ok'] else 1
        result = check_observations(json.loads(Path(sys.argv[2]).read_text()))
        print(json.dumps(result, indent=2))
        return 0 if result['ok'] else 1
    scenario = json.loads((Path(__file__).parent / 'examples/scenario.json').read_text()) if sys.argv[1] == 'demo' else json.loads(Path(sys.argv[2]).read_text())
    if sys.argv[1] not in ('demo', 'check'):
        raise SystemExit('unknown command')
    base = Path(__file__).parent
    scenario.setdefault('adapter_command', [sys.executable, str(base / 'examples/adapter.py')])
    good = check(scenario)
    if sys.argv[1] == 'demo':
        scenario['adapter_command'].append('--bug')
        bad = check(scenario)
        print(json.dumps({'healthy': good, 'regression': bad}, indent=2, ensure_ascii=False))
        return 0 if good['ok'] and not bad['ok'] else 1
    print(json.dumps(good, indent=2, ensure_ascii=False))
    return 0 if good['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
