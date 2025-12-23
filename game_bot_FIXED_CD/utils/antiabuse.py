import time

_last_actions = {}

def check_cd(user_id: int, action: str, cd: int) -> bool:
    now = time.time()
    key = f"{user_id}:{action}"

    last = _last_actions.get(key, 0)
    if now - last < cd:
        return False

    _last_actions[key] = now
    return True
