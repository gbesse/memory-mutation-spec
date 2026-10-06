# memory-mutation-spec

## Nouveau : vérifier la portée partagée

`python3 scope_audit.py scope-demo --lang fr` montre en dix secondes une portée `shared` demandée mais non transmise (démo réussie : code 0). Avec une capture JSON : `python3 scope_audit.py check scope.json --lang fr`. Fournissez `requested_scope: "shared"`, `forwarded_scope` (`"shared"`, `[[]]` ou `null`) et, si disponibles, des `observations` avec `scope_key` et `session_id`. L’outil vérifie la transmission déclarée ; plusieurs groupes observés seuls ne prouvent pas la cause. Aucun parseur de logs Hermes n’est inclus.

**Projets voisins :** [Hindsight #5305](https://github.com/vectorize-io/hindsight/issues/5305) et [#5309](https://github.com/vectorize-io/hindsight/issues/5309) motivent l’audit de la portée demandée face à la configuration transmise. Ces issues sont des sources de problème, pas des intégrations.

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

## Démo liée à Hindsight

Les fichiers `hindsight-observations*.json` modélisent les transitions décrites dans [Hindsight #4831](https://github.com/vectorize-io/hindsight/issues/4831) et [#4829](https://github.com/vectorize-io/hindsight/issues/4829). Le vérificateur accepte aussi des observations JSON capturées séparément :

```bash
python3 tool.py observation-demo
python3 tool.py check-observations examples/hindsight-observations.json
```

La seconde commande échoue volontairement sur les transitions signalées. Ces données sont des fixtures synthétiques dérivées des rapports ; elles ne prouvent pas une reproduction sur Hindsight, et aucun serveur Hindsight n’est appelé.

## Exemple : suppression explicite

`python3 -m examples.explicit_removal` compare une suppression de tag déclarée à une perte silencieuse du même tag. Seule la première respecte l’invariant. Les transitions sont synthétiques ; aucun service de mémoire n’est appelé.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

MIT.
