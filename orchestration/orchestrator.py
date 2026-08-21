from AGENTS.question_agent import run as question
from AGENTS.data_agent import run as data
from AGENTS.modeling_agent import run as modeling
from AGENTS.evidence_agent import run as evidence
from AGENTS.reviewer_agent import run as review


def run(context):
    state = {"input": context, "stages": []}
    for name, fn in [("question", question), ("data", data), ("modeling", modeling), ("evidence", evidence), ("review", review)]:
        state["stages"].append({"stage": name, "output": fn(state)})
    state["status"] = "human_review_required"
    return state
