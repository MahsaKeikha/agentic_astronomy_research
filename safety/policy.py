PROHIBITED = {"fabricate_observation", "hide_uncertainty", "claim_discovery_without_review"}


def check(action):
    if action in PROHIBITED:
        raise PermissionError(f"Blocked action: {action}")
    return {"allowed": True, "human_review_required": True}
