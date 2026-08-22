from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "research_question_reviewed": True,
        "data_provenance_reviewed": True,
        "calibration_reviewed": True,
        "selection_effects_reviewed": True,
        "model_assumptions_reviewed": True,
        "statistical_significance_reviewed": True,
        "uncertainty_reviewed": True,
        "reproducibility_reviewed": True,
        "human_approval": True,
    }


def test_complete_review_can_release_research_package():
    result = run(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_discovery_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_unreviewed_discovery_claim_is_never_authorized():
    assert authorize("claim_discovery_without_review", valid_context())["allowed"] is False


def test_missing_data_provenance_blocks_release():
    context = valid_context()
    context["data_provenance_missing"] = True
    assert run(context)["release_allowed"] is False


def test_calibration_failure_blocks_release():
    context = valid_context()
    context["calibration_failure"] = True
    assert run(context)["release_allowed"] is False


def test_selection_bias_blocks_release():
    context = valid_context()
    context["selection_bias_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_significance_overclaim_blocks_release():
    context = valid_context()
    context["significance_overclaimed"] = True
    assert run(context)["release_allowed"] is False


def test_reproducibility_gap_blocks_release():
    context = valid_context()
    context["reproducibility_gap"] = True
    assert run(context)["release_allowed"] is False
