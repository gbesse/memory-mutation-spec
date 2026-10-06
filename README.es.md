# memory-mutation-spec

## Nuevo: comprobar el envío del alcance compartido

`python3 scope_audit.py scope-demo --lang es` muestra en diez segundos que se solicita `shared` pero no se transmite (la demo correcta sale con código 0). Con JSON guardado: `python3 scope_audit.py check scope.json --lang es`. Proporcione `requested_scope: "shared"`, `forwarded_scope` (`"shared"`, `[[]]` o `null`) y opcionalmente `observations` con `scope_key` y `session_id`. Verifica la transmisión declarada; las observaciones fragmentadas por sí solas no prueban la causa. Todavía no incluye un analizador de logs Hermes.

**Proyectos relacionados:** [Hindsight #5305](https://github.com/vectorize-io/hindsight/issues/5305) y [#5309](https://github.com/vectorize-io/hindsight/issues/5309) motivan comparar el alcance solicitado con la configuración transmitida. Son pruebas del problema, no integraciones.

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

## Demo relacionada con Hindsight

Los archivos `hindsight-observations*.json` modelan las transiciones descritas en [Hindsight #4831](https://github.com/vectorize-io/hindsight/issues/4831) y [#4829](https://github.com/vectorize-io/hindsight/issues/4829). El verificador también acepta observaciones JSON capturadas por separado:

```bash
python3 tool.py observation-demo
python3 tool.py check-observations examples/hindsight-observations.json
```

El segundo comando falla intencionadamente con las transiciones comunicadas. Son ejemplos sintéticos basados en los informes; no constituyen una reproducción independiente en Hindsight y no se llama a ningún servidor Hindsight.

## Ejemplo: eliminación explícita

`python3 -m examples.explicit_removal` compara una eliminación de etiqueta declarada con la pérdida silenciosa de la misma etiqueta. Solo la primera cumple el invariante. Las transiciones son sintéticas; no se llama a ningún servicio de memoria.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Licencia

MIT.
