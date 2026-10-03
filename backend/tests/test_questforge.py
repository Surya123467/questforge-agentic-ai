from fastapi.testclient import TestClient
from app.main import app, sessions

client=TestClient(app)

def setup_function():
    sessions.clear()

def test_health():
    assert client.get("/health").status_code == 200

def test_world_discovery_and_memory():
    r=client.post("/turn",json={"session_id":"a","action":"Search the security room"})
    assert r.status_code == 200
    data=r.json()
    assert "Security Room" in data["world"]["discovered"]
    assert data["world"]["memories"][-1]["content"] == "Search the security room"

def test_npc_state_persists():
    client.post("/turn",json={"session_id":"a","action":"Talk to K-9"})
    r=client.get("/session/a")
    assert r.json()["npcs"][0]["attitude"] == 1
