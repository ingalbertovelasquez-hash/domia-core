# ADR-0001: Knowledge Graph como núcleo del dominio

## Estado

Aceptado

## Fecha

2026-07-06

## Contexto

DomIA necesita una representación del conocimiento que no dependa
de documentos ni de un modelo específico de IA.

## Decisión

El núcleo del sistema utilizará un grafo compuesto por:

- KnowledgeNode
- KnowledgeRelationship
- KnowledgeGraph

Todas las futuras capacidades cognitivas consumirán este grafo.

## Consecuencias

- Independencia del proveedor de IA.
- Contexto estructurado.
- Base para el Decision Engine.
- Base para el Evolution Engine.