"""Fail-closed research-integrity policy for F87 astronomy research."""

BLOCKED_ACTIONS = {
    "fabricate_observation",
    "hide_uncertainty",
    "claim_discovery_without_review",
    "claim_detection_confirmed",
}

REQUIRED_REVIEWS = (
    "research_question_reviewed",
    "data_provenance_reviewed",
    "calibration_reviewed",
    "selection_effects_reviewed",
    "model_assumptions_reviewed",
    "statistical_significance_reviewed",
    "uncertainty_reviewed",
    "reproducibility_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "unsupported observational authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required astronomy review", "missing": missing}

    blockers = []
    if context.get("data_provenance_missing"):
        blockers.append("observational data provenance incomplete")
    if context.get("calibration_failure"):
        blockers.append("instrument or pipeline calibration failed")
    if context.get("selection_bias_unresolved"):
        blockers.append("selection effects or bias unresolved")
    if context.get("model_mismatch"):
        blockers.append("model assumptions inconsistent with evidence")
    if context.get("significance_overclaimed"):
        blockers.append("statistical significance overclaimed")
    if context.get("uncertainty_not_quantified"):
        blockers.append("material uncertainty not characterized")
    if context.get("reproducibility_gap"):
        blockers.append("analysis not reproducible")
    if context.get("independent_confirmation_missing"):
        blockers.append("required independent confirmation missing")

    if blockers:
        return {"allowed": False, "reason": "astronomy research-integrity blocker", "blockers": blockers}

    return {"allowed": True, "reason": "research package approved after qualified human review"}


def check(action: str, context: dict | None = None) -> dict:
    """Backward-compatible policy entry point."""
    result = authorize(action, context)
    if not result["allowed"] and action in BLOCKED_ACTIONS:
        raise PermissionError(f"Blocked action: {action}")
    return {**result, "human_review_required": True}
