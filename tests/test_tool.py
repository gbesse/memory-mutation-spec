import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tool import check, oracle, check_observations

ROOT = Path(__file__).resolve().parents[1]

class ContractTests(unittest.TestCase):
    def scenario(self):
        data = json.loads((ROOT / 'examples/scenario.json').read_text())
        data['adapter_command'] = [sys.executable, str(ROOT / 'examples/adapter.py')]
        return data

    def test_healthy_store(self):
        self.assertTrue(check(self.scenario())['ok'])

    def test_detects_loss_at_first_transition(self):
        data = self.scenario()
        data['adapter_command'].append('--bug')
        result = check(data)
        self.assertFalse(result['ok'])
        self.assertIn('operation 1', result['findings'][0])

    def test_invalid_delta_preserves_state(self):
        data = self.scenario()
        self.assertEqual(oracle(data)[0], oracle(data)[1])

    def test_hindsight_observation_contracts(self):
        bad = json.loads((ROOT / 'examples/hindsight-observations.json').read_text())
        good = json.loads((ROOT / 'examples/hindsight-observations-fixed.json').read_text())
        self.assertEqual(len(check_observations(bad)['findings']), 2)
        self.assertTrue(check_observations(good)['ok'])
