# memory-mutation-spec

Vérifie les invariants après chaque mutation d’une mémoire d’agent.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Projets voisins

- [Hindsight #4831 — tags perdus après consolidation](https://github.com/vectorize-io/hindsight/issues/4831)
- [Hindsight #4829 — bloc périmé après delta invalide](https://github.com/vectorize-io/hindsight/issues/4829)
- [Agent Memory Benchmark — évaluation du rappel et de l’oubli](https://github.com/AlekseiMarchenko/agent-memory-benchmark)

Ces projets documentent le besoin ou couvrent une partie du problème. Aucun lien d’affiliation ni intégration avec eux n’est revendiqué.

## Démarrer

```bash
python3 tool.py demo
python3 tool.py check examples/scenario.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Portée actuelle

Le contrat compare chaque état renvoyé par un adaptateur externe à un oracle simple. La commande d’adaptateur se configure avec `adapter_command` dans le scénario JSON. L’adaptateur livré est synthétique ; aucun adaptateur Hindsight n’est encore fourni.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

MIT.
