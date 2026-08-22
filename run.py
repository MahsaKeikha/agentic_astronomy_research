from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "astronomy research analysis",
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
