from fastapi import FastAPI
from .models import ActionRequest, TurnResponse, WorldState
from .agents import run_turn

app=FastAPI(title="QuestForge AI", version="1.0.0")
sessions: dict[str, WorldState] = {}

@app.get("/health")
def health(): return {"status":"ok","service":"questforge"}

@app.get("/session/{session_id}", response_model=WorldState)
def get_session(session_id: str):
    return sessions.setdefault(session_id, WorldState())

@app.post("/turn", response_model=TurnResponse)
def turn(req: ActionRequest):
    world=sessions.setdefault(req.session_id, WorldState())
    scene, trace=run_turn(req.action, world)
    return TurnResponse(scene=scene, world=world, trace=trace)
