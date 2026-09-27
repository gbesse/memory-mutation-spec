"""Synthetic store adapter; replace with an adapter for a real memory store."""
import copy
import json
import sys

scenario = json.load(sys.stdin)
state = copy.deepcopy(scenario['initial'])
snapshots = []
for op in scenario['operations']:
    key = op['id']
    if op['op'] == 'put':
        state[key] = {'text': op['text'], 'tags': op.get('tags', [])}
    elif op['op'] == 'update':
        state[key]['text'] = op['text']
        if 'tags' in op:
            state[key]['tags'] = op['tags']
        if '--bug' in sys.argv:
            state[key]['tags'] = []
    elif op['op'] == 'delete':
        state.pop(key, None)
    elif op['op'] == 'invalid_delta' and '--bug' in sys.argv:
        state[key] = {'text': 'stale', 'tags': []}
    snapshots.append(copy.deepcopy(state))
json.dump(snapshots, sys.stdout)
