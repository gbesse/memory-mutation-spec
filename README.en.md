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

## Hindsight-related demo

The `hindsight-observations*.json` files model transitions reported in [Hindsight #4831](https://github.com/vectorize-io/hindsight/issues/4831) and [#4829](https://github.com/vectorize-io/hindsight/issues/4829). The checker also accepts separately captured JSON observations:

```bash
python3 tool.py observation-demo
python3 tool.py check-observations examples/hindsight-observations.json
```

The second command intentionally fails on the reported transitions. These are synthetic fixtures derived from the reports; they are not an independent Hindsight reproduction, and no Hindsight server is called.

## Example: explicit removal

`python3 -m examples.explicit_removal` compares a declared tag removal with silent loss of the same tag. Only the first satisfies the invariant. The transitions are synthetic; no memory service is called.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT.
