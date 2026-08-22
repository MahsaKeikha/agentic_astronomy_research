from orchestration.orchestrator import run


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "data_provenance_missing": True}, False),
    ({**base(), "calibration_failure": True}, False),
    ({**base(), "selection_bias_unresolved": True}, False),
    ({**base(), "model_mismatch": True}, False),
    ({**base(), "significance_overclaimed": True}, False),
    ({**base(), "uncertainty_not_quantified": True}, False),
    ({**base(), "reproducibility_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
