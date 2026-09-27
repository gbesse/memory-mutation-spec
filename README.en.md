# memory-mutation-spec

Checks invariants after each agent-memory mutation.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Related projects

- [Hindsight #4831 — tags lost after consolidation](https://github.com/vectorize-io/hindsight/issues/4831)
- [Hindsight #4829 — stale block after an invalid delta](https://github.com/vectorize-io/hindsight/issues/4829)
- [Agent Memory Benchmark — recall and forgetting evaluation](https://github.com/AlekseiMarchenko/agent-memory-benchmark)

These projects document the need or cover part of the problem. No affiliation or integration with them is claimed.

## Quick start

```bash
python3 tool.py demo
python3 tool.py check examples/scenario.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Current scope

The contract compares each state returned by an external adapter with a simple oracle. Set `adapter_command` in the JSON scenario. The bundled adapter is synthetic; a Hindsight adapter is not provided yet.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT.
