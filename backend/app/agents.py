from .models import AgentStep, WorldState

def run_game_master(action: str, world: WorldState):
    return AgentStep(agent="Game Master", status="completed",
                     output=f"Interpreting player action: {action}")

def run_world_agent(action: str, world: WorldState):
    a=action.lower()
    if "security" in a or "room" in a:
        item="Security Room"
        if item not in world.discovered: world.discovered.append(item)
        return AgentStep(agent="World Agent", status="completed",
                         output="The security room is now discovered.")
    if "lab" in a:
        return AgentStep(agent="World Agent", status="completed",
                         output="The laboratory remains unstable but accessible.")
    return AgentStep(agent="World Agent", status="completed",
                     output="The environment reacts to the player's movement.")

def run_npc_agent(action: str, world: WorldState):
    a=action.lower()
    if "robot" in a or "k-9" in a or "talk" in a:
        world.npcs[0].attitude += 1
        return AgentStep(agent="NPC Agent", status="completed",
                         output="K-9 recognizes the player and lowers its defensive posture.")
    return AgentStep(agent="NPC Agent", status="completed",
                     output="NPCs remain alert to the player's actions.")

def run_story_agent(action: str, world: WorldState):
    return AgentStep(agent="Story Agent", status="completed",
                     output="The action creates a new narrative consequence.")

def run_memory_agent(action: str, world: WorldState):
    memories=[m.content for m in world.memories]
    context="No prior memory matched." if not memories else f"Retrieved memory: {memories[-1]}"
    return AgentStep(agent="Memory Agent", status="completed", output=context)

def generate_scene(action: str, world: WorldState):
    a=action.lower()
    if "robot" in a or "k-9" in a or "talk" in a:
        return "K-9's optic flickers from red to amber. It remembers your earlier search of the facility and asks why you returned."
    if "security" in a or "room" in a:
        return "You push through the security door. Dead monitors line the wall, while one terminal still pulses with a warning: PROJECT MERIDIAN."
    if "lab" in a:
        return "Dust hangs in the blue emergency lights. Somewhere deeper inside Meridian Laboratory, a machine powers up."
    return "The abandoned laboratory responds to your movement: lights flicker, metal shifts, and a distant alarm changes tone."

def run_turn(action: str, world: WorldState):
    trace=[]
    trace.append(run_game_master(action, world))
    trace.append(run_memory_agent(action, world))
    trace.append(run_world_agent(action, world))
    trace.append(run_npc_agent(action, world))
    trace.append(run_story_agent(action, world))
    world.events.append({"turn":len(world.events)+1,"actor":"player","summary":action})
    memory=action.strip()
    if memory and not any(m.content == memory for m in world.memories):
        world.memories.append({"content":memory,"importance":2})
    trace.append(AgentStep(agent="Game Master",status="completed",output="Composed scene from updated world state."))
    return generate_scene(action, world), trace
