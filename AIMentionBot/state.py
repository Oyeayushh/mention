# Per-chat tagging state management
# States: "running", "paused", "stopped"

_states = {}  # chat_id -> "running" | "paused" | "stopped"

def set_state(chat_id: int, state: str):
    _states[chat_id] = state

def get_state(chat_id: int) -> str:
    return _states.get(chat_id, "stopped")

def is_running(chat_id: int) -> bool:
    return _states.get(chat_id) == "running"

def is_paused(chat_id: int) -> bool:
    return _states.get(chat_id) == "paused"

def clear_state(chat_id: int):
    _states.pop(chat_id, None)
