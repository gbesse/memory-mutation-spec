"""Separate an intentional tag removal from silent tag loss."""
import json

from tool import check_observations

base = {
    "kind": "consolidation_update",
    "before_tags": ["status:active", "topic:billing"],
    "after_tags": ["status:active"],
}
intentional = check_observations({"events": [{**base, "explicitly_removed_tags": ["topic:billing"]}]})
silent = check_observations({"events": [base]})
assert intentional["ok"] and not silent["ok"]
print(json.dumps({"source": "synthetic transitions; no memory service", "intentional_ok": intentional["ok"], "silent_loss_detected": not silent["ok"]}, sort_keys=True))
