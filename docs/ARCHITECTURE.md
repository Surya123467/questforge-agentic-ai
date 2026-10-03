# QuestForge Architecture

## Turn lifecycle

1. Player submits an action.
2. Game Master interprets the intent.
3. Memory Agent retrieves relevant prior events.
4. World Agent resolves environment changes.
5. NPC Agent updates character reactions and relationships.
6. Story Agent evaluates narrative consequences.
7. Game Master composes the next scene.
8. State and event memory are persisted.

## Production architecture

React → FastAPI → LangGraph orchestration → specialized agents → tools/RAG/memory → PostgreSQL + pgvector → streamed scene.

The deterministic implementation deliberately keeps agent boundaries explicit so the behavior can be tested before introducing probabilistic model calls.
