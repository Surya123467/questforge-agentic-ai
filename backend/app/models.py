from typing import Literal
from pydantic import BaseModel, Field

class ActionRequest(BaseModel):
    session_id: str = "demo"
    action: str = Field(min_length=1, max_length=500)

class Event(BaseModel):
    turn: int
    actor: str
    summary: str

class Memory(BaseModel):
    content: str
    importance: int = 1

class NPCState(BaseModel):
    name: str
    role: str
    attitude: int = 0

class WorldState(BaseModel):
    location: str = "Meridian Laboratory"
    discovered: list[str] = []
    events: list[Event] = []
    memories: list[Memory] = []
    npcs: list[NPCState] = [NPCState(name="K-9", role="damaged security robot", attitude=0)]

class AgentStep(BaseModel):
    agent: str
    status: Literal["completed", "review"]
    output: str

class TurnResponse(BaseModel):
    scene: str
    world: WorldState
    trace: list[AgentStep]
    requires_review: bool = False
