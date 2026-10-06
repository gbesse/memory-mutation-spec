import unittest

from scope_audit import audit


class ScopeAuditTests(unittest.TestCase):
    def test_requested_shared_scope_dropped_by_adapter(self):
        result = audit({"requested_scope": "shared", "forwarded_scope": None,
                        "observations": [{"scope_key": "session:a", "session_id": "a"},
                                         {"scope_key": "session:b", "session_id": "b"}]})
        self.assertFalse(result["ok"])
        self.assertEqual(result["scope_count"], 2)

    def test_forwarded_shared_scope_passes(self):
        result = audit({"requested_scope": "shared", "forwarded_scope": "shared",
                        "observations": []})
        self.assertTrue(result["ok"])


if __name__ == "__main__":
    unittest.main()
