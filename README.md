# QuestForge AI

## Agentic AI Interactive Adventure & Dynamic World Simulator

QuestForge AI is an interview-ready multi-agent game-master system where an AI coordinates story generation, world state, NPC behavior, and persistent memory.

### Architecture

`PLAYER → GAME MASTER → WORLD / NPC / STORY → MEMORY → NEW WORLD STATE`

### Agents
- **Game Master** — orchestrates the turn and produces the player-facing scene.
- **World Agent** — resolves locations, objects, hazards, and world-state changes.
- **NPC Agent** — manages NPC intent, relationships, and reactions.
- **Story Agent** — advances narrative threads and consequences.
- **Memory Agent** — retrieves relevant prior events and writes durable memories.

### Why agentic?
The system separates responsibilities instead of asking one model to do everything. A production version can replace deterministic agent logic with LLM-backed nodes while retaining the same state-machine boundaries.

### Included
- FastAPI backend
- React + TypeScript + Vite frontend
- Deterministic mock mode — no API key required
- Persistent in-memory world/session state
- Agent execution trace
- NPC relationship state
- World event history
- Memory retrieval
- Docker Compose
- Pytest tests
- GitHub Actions CI
- Architecture and interview documentation

## Run locally

### Backend
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=. uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173.

### Docker
```bash
docker compose up --build
```

## Example

Start with:
> I enter the abandoned Meridian laboratory.

Then try:
> Search the security room.

Then:
> Talk to the damaged security robot.

The system uses prior events and memory to change later responses.

## Production evolution

A production build could add:
- LangGraph orchestration
- OpenAI/Azure OpenAI or another LLM provider
- PostgreSQL for persistent sessions
- pgvector for semantic memory
- structured tool calling
- Redis for short-lived state
- authentication and multiplayer sessions
- content safety controls
- observability and token/cost tracking
- sandboxed game tools
- streaming responses

## Interview pitch

> "QuestForge is my demonstration of agentic stateful applications. Instead of one LLM prompt generating a story, I separated orchestration into Game Master, World, NPC, Story, and Memory agents. The important engineering problem is maintaining structured state across turns: events, relationships, locations, and retrieved memories influence the next world state. I built it in deterministic mode first so the architecture and tests are reproducible, then designed clear boundaries where an LLM and vector memory can be introduced."
