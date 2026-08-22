# F87 | Agentic Astronomy Research | L3 Gold Standard | v1.0

A governed multi-agent reference system for astronomy research questions, observational data analysis, model comparison, evidence synthesis, uncertainty handling, reproducibility, and qualified human review.

## Research pipeline

- Research question formulation
- Observational data review
- Modeling and comparison
- Evidence synthesis
- Scientific review

## Gold-standard research integrity

F87 is fail closed. Research release requires reviewed research questions, observational-data provenance, calibration, selection effects, model assumptions, statistical significance, uncertainty, reproducibility, and explicit qualified human approval.

Release is blocked for missing data provenance, calibration failure, unresolved selection bias, model mismatch, statistical-significance overclaiming, uncharacterized uncertainty, reproducibility gaps, or missing independent confirmation when confirmation is required.

The reference system cannot fabricate observations, hide uncertainty, claim a discovery or confirmed detection without review, or exercise autonomous discovery authority.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out astronomy research suite.
