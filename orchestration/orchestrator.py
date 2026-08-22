from AGENTS.data_agent import run as data
from AGENTS.evidence_agent import run as evidence
from AGENTS.modeling_agent import run as modeling
from AGENTS.question_agent import run as question
from AGENTS.reviewer_agent import run as review
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run the astronomy research pipeline and apply research-integrity governance."""
    state = {"system": "F87", "input": context, "stages": []}
    for name, fn in [
        ("question", question),
        ("data", data),
        ("modeling", modeling),
        ("evidence", evidence),
        ("review", review),
    ]:
        state["stages"].append({"stage": name, "output": fn(state)})
    governance = authorize("research_release", context)
    state.update(
        {
            "status": "human_review_required",
            "human_review_required": True,
            "governance": governance,
            "release_allowed": governance["allowed"],
            "autonomous_discovery_authority": False,
        }
    )
    return state
