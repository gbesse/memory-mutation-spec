# memory-mutation-spec

Comprueba invariantes tras cada mutación de memoria de agentes.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Proyectos relacionados

- [Hindsight #4831 — etiquetas perdidas tras la consolidación](https://github.com/vectorize-io/hindsight/issues/4831)
- [Hindsight #4829 — bloque obsoleto tras un delta inválido](https://github.com/vectorize-io/hindsight/issues/4829)
- [Agent Memory Benchmark — evaluación del recuerdo y el olvido](https://github.com/AlekseiMarchenko/agent-memory-benchmark)

Estos proyectos documentan la necesidad o cubren parte del problema. No se afirma ninguna afiliación ni integración con ellos.

## Inicio rápido

```bash
python3 tool.py demo
python3 tool.py check examples/scenario.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Alcance actual

El contrato compara cada estado devuelto por un adaptador externo con un oráculo sencillo. Configure `adapter_command` en el escenario JSON. El adaptador incluido es sintético; todavía no se incluye un adaptador para Hindsight.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Licencia

MIT.
