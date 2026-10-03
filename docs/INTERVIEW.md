# Interview Talking Points

### Why multiple agents?
A game world has different responsibilities: physical state, character behavior, narrative continuity, and memory. Separating them makes each responsibility observable and replaceable.

### What makes it stateful?
The system stores discovered locations, events, NPC attitude, and player actions. Later turns can retrieve those memories rather than starting from a blank prompt.

### Why deterministic mode?
LLMs introduce nondeterminism and external costs. I first built a reproducible workflow with tests, then designed adapter boundaries for LLM-backed agents.

### How would you productionize it?
Use LangGraph for orchestration, PostgreSQL for durable sessions, pgvector for semantic memory, Redis for transient state, structured tool calls, streaming, auth, observability, and content moderation.
