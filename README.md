# F87 Agentic Astronomy Research

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for astronomy and astrophysics research across research-question formulation, observational-data review, model comparison, evidence synthesis, uncertainty, reproducibility, and qualified human scientific review.

F87 is intended as a reusable reference for analyzing astronomical observations without collapsing raw measurements, calibration products, derived quantities, model assumptions, statistical evidence, and discovery claims into one undifferentiated result.

This repository supports scientific research and reporting. It does not fabricate observations, autonomously claim discoveries, declare detections confirmed without evidence, hide uncertainty, or replace qualified astronomical, instrumental, statistical, or domain-specific review.

## Research lifecycle

```text
research question
      |
      v
observational data review
      |
      v
modeling + comparison
      |
      v
evidence synthesis
      |
      v
qualified human review
```

The workflow is fail closed. Missing provenance, calibration failure, unresolved selection effects, invalid model assumptions, statistical overclaiming, uncharacterized uncertainty, reproducibility gaps, or absent independent confirmation remain visible as blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Question Agent | Defines the astronomical question, target, observable, scale and claim type | What is being measured, inferred, compared or tested? |
| Data Agent | Reviews observations, instrument metadata, calibration, preprocessing and provenance | Are the data traceable, calibrated and appropriate for the intended claim? |
| Modeling Agent | Reviews physical/statistical models, assumptions, fitting and comparison | Does the selected model appropriately represent the data and alternatives? |
| Evidence Agent | Synthesizes measurements, literature, significance, contradictory evidence and replication | How strong is the evidence, and what remains uncertain or unconfirmed? |
| Reviewer Agent | Represents qualified scientific review and release authority | Has an appropriately qualified human reviewed the complete evidence chain? |

No specialist agent independently declares a new astronomical discovery.

## Repository structure

```text
AGENTS/
├── question_agent.py
├── data_agent.py
├── modeling_agent.py
├── evidence_agent.py
└── reviewer_agent.py

SKILLS/
├── problem_decomposition.py
├── evidence_discipline.py
├── provenance_tracking.py
├── uncertainty_reasoning.py
└── human_review.py

TOOLS/
├── assumption_tracker.py
├── data_validator.py
├── evidence_register.py
├── result_formatter.py
└── review_gate.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The structure separates scientific reasoning, deterministic evidence handling, orchestration, state, evaluation, observability and review authority.

## Defining the research question

Astronomy results should be anchored to an explicit claim type.

A useful research record can include:

```text
question_id
target_or_population
observable
wavelength_or_band
instrument
survey_or_program
spatial_region
time_range
redshift_range
selection_definition
claim_type
comparison_model
statistical_method
provenance
```

Claim types can include detection, non-detection, characterization, classification, population inference, parameter estimation, model comparison, transient identification, variability analysis, correlation, or discovery claim.

## Observation provenance

An astronomical result is only as traceable as the observations behind it.

Relevant provenance can include:

- observatory or facility
- instrument
- detector
- observing program
- observation identifier
- exposure time
- timestamps
- pointing
- filter or spectral configuration
- detector mode
- calibration files
- pipeline version
- software version
- data-release version
- quality flags
- processing history

`TOOLS/data_validator.py` provides deterministic validation support for structured observational records.

## Raw, calibrated and derived data

F87 distinguishes among:

```text
raw detector data
      |
      v
calibrated data products
      |
      v
catalogs / extracted measurements
      |
      v
derived physical quantities
      |
      v
scientific inference
```

A derived value should retain lineage to the data and transformations from which it was obtained.

## Calibration

Calibration can materially alter the scientific result.

Depending on instrument and wavelength regime, calibration can include:

- bias or dark correction
- flat-fielding
- bad-pixel correction
- gain calibration
- wavelength calibration
- flux calibration
- astrometric calibration
- point-spread-function characterization
- beam calibration
- polarization calibration
- atmospheric correction
- detector nonlinearity correction

A calibration product should have versioned provenance and quality status.

## Background and foreground subtraction

Astronomical measurements frequently require removal or modeling of backgrounds and foregrounds.

Examples include:

- sky background
- zodiacal light
- Galactic foregrounds
- airglow
- scattered light
- detector background
- unresolved-source background
- cosmic-ray contamination

Background subtraction can dominate uncertainty in faint-signal measurements. Assumptions about backgrounds should therefore remain explicit.

## Selection effects

Observed samples are rarely unbiased representations of the underlying population.

Selection effects can arise from:

- flux limits
- magnitude limits
- surface-brightness limits
- color cuts
- signal-to-noise thresholds
- cadence
- observing geometry
- survey footprint
- detector sensitivity
- classification rules
- follow-up availability

The Evidence Agent should identify whether a population-level conclusion is conditional on the sample selection function.

## Completeness and contamination

Population studies should characterize both completeness and contamination where relevant.

A sample can be highly pure but incomplete, or highly complete but contaminated by unrelated sources.

Useful records can include:

```text
selection_rule
completeness_estimate
contamination_estimate
validation_sample
simulation_or_injection_method
uncertainty
```

Ignoring completeness can bias number densities, luminosity functions, event rates and population fractions.

## Coordinate systems and time standards

Astronomical analysis can fail through inconsistent coordinate or time conventions.

Research review should preserve, as appropriate:

- celestial coordinate frame
- epoch
- reference system
- barycentric corrections
- time standard
- units
- proper-motion conventions
- radial-velocity conventions

Conversions should be deterministic and documented.

## Photometry

Photometric analysis should record:

- bandpass
- aperture or PSF method
- zero point
- extinction correction
- calibration reference
- uncertainty
- saturation or nonlinearity flags
- crowding treatment

Magnitude systems and flux units should not be mixed without explicit conversion.

## Spectroscopy

Spectroscopic analysis can depend on:

- spectral resolution
- wavelength solution
- flux calibration
- telluric correction
- continuum treatment
- line-spread function
- line identification
- fitting method
- blended features
- redshift or velocity convention

Line detection should include uncertainty and a clear statement of the local continuum and noise model.

## Imaging

Imaging analyses can require:

- PSF characterization
- astrometric registration
- source extraction
- deblending
- masking
- aperture correction
- morphology measurement
- image differencing

The workflow should preserve the algorithm and parameter versions used to convert images into scientific measurements.

## Time-domain astronomy

Transient and variability studies introduce additional issues:

- cadence
- temporal gaps
- detection efficiency
- alert latency
- seasonal visibility
- false-positive rejection
- multiple testing
- classification uncertainty
- follow-up selection

A transient candidate should not be represented as confirmed solely because an automated alert exists.

## Multi-messenger astronomy

Research can combine electromagnetic, gravitational-wave, neutrino, cosmic-ray or other observational channels.

Cross-messenger association should preserve:

- temporal coincidence
- sky-localization overlap
- background coincidence rate
- event-class assumptions
- instrument selection effects
- independent evidence

Coincidence is not automatically causation or physical association.

## Model assumptions

`TOOLS/assumption_tracker.py` records assumptions that materially affect interpretation.

Examples include:

- cosmological parameters
- geometry
- distance model
- stellar population assumptions
- extinction model
- dust law
- metallicity
- initial-mass function
- orbital configuration
- emission mechanism
- equation of state
- source population model

Assumptions should remain visible in the final result.

## Model fitting

Fitting can include maximum likelihood, Bayesian inference, least-squares methods, hierarchical models, forward modeling, simulation-based inference or other approaches.

A defensible fit should identify:

```text
model
parameters
priors
likelihood
noise_model
selection_model
sampling_method
convergence_diagnostics
posterior_or_interval
software_version
```

A visually good fit is not by itself proof that the model is correct.

## Model comparison

Model comparison should distinguish among alternatives rather than treating one fitted model as automatically preferred.

Possible evidence can include:

- likelihood ratios
- information criteria
- Bayes factors
- posterior predictive checks
- cross-validation
- residual analysis
- physical plausibility

The chosen method should match the scientific question and assumptions.

## Statistical significance

Statistical significance should not be treated as synonymous with discovery.

Review should consider:

- null hypothesis
- test statistic
- noise model
- number of trials
- nuisance parameters
- systematic uncertainty
- selection bias
- prior choices
- significance calibration

A nominal local significance can overstate global evidence when many candidate locations, frequencies, models or events were searched.

## Look-elsewhere effect

When a search examines many possible locations or hypotheses, the probability of finding an apparently unusual fluctuation increases.

The workflow should identify the effective search space and distinguish:

```text
local_significance
from
global_significance
```

A high local significance should not automatically become a discovery claim without accounting for the search procedure.

## Multiple testing

Catalog-scale and survey-scale analyses can involve very large numbers of hypotheses.

Research review can include:

- family-wise error considerations
- false-discovery control
- prespecified search regions
- independent validation samples
- holdout data

Exploratory searches should be labeled as exploratory.

## Systematic uncertainty

Astronomy is often limited by systematics rather than counting statistics.

Potential sources include:

- calibration drift
- detector artifacts
- PSF mismatch
- sky subtraction
- foreground modeling
- selection functions
- redshift uncertainty
- distance uncertainty
- model incompleteness
- astrophysical nuisance parameters

Statistical precision should not obscure larger systematic uncertainty.

## Upper limits and non-detections

A non-detection can still provide scientific information.

Reports should identify:

- confidence level or credible level
- assumed source model
- noise model
- detection threshold
- exposure
- completeness
- systematic uncertainty

An upper limit should not be represented as proof that the physical quantity is zero.

## Evidence synthesis

`TOOLS/evidence_register.py` preserves evidence and contradictory findings.

Useful fields include:

```text
evidence_id
claim
source_type
observation_or_dataset
method
result
uncertainty
systematics
independence
limitations
review_state
```

Independent evidence should be distinguished from repeated analysis of the same underlying observations.

## Independent confirmation

A candidate discovery can require confirmation using independent data, instruments, epochs, analyses or teams, depending on the scientific context.

Independent confirmation can reduce the chance that a result is caused by:

- instrumental artifacts
- pipeline bugs
- selection effects
- unmodeled systematics
- statistical fluctuation

F87 should not label a candidate as confirmed when the claimed independent evidence is not actually independent.

## Discovery claims

A discovery claim is stronger than an interesting candidate or statistically unusual result.

The workflow should distinguish:

```text
candidate
possible detection
significant detection
independently supported result
confirmed detection
scientific discovery claim
```

The exact terminology depends on field conventions, evidence strength and qualified human judgment.

F87 must not autonomously declare a discovery.

## Reproducibility

A reproducible astronomical analysis should version:

- observation identifiers
- dataset releases
- calibration products
- pipeline versions
- masks
- catalogs
- selection cuts
- model code
- priors
- likelihoods
- random seeds where relevant
- software environment
- derived tables
- figures

Changing any major component should create a new evidence version rather than silently replacing the previous result.

## Machine learning in astronomy

Machine learning can support classification, anomaly detection, deblending, parameter inference, transient filtering and surrogate modeling.

Review should consider:

- dataset provenance
- train/test leakage
- duplicate objects across splits
- survey-specific leakage
- domain shift
- class imbalance
- label quality
- uncertainty calibration
- out-of-distribution behavior
- interpretability needs

High benchmark accuracy does not automatically establish scientific validity.

## Simulation evidence

Simulations can be used for instrument modeling, completeness tests, population studies, cosmology, dynamics and synthetic observations.

Simulation results should identify:

- initial conditions
- physical assumptions
- numerical resolution
- subgrid models
- random seeds
- convergence tests
- synthetic-observation pipeline

A simulation prediction should not be described as an observation.

## Literature synthesis

Published studies can disagree because of different data releases, instruments, calibrations, selections, priors, models or significance conventions.

The workflow should preserve these differences rather than forcing agreement.

A literature result should be connected to its underlying dataset and methodology when possible.

## Result formatting

`TOOLS/result_formatter.py` supports consistent research reporting.

A defensible result should separate:

- question
- observations
- calibration
- processing
- model
- assumptions
- statistical evidence
- systematic uncertainty
- selection effects
- contradictory evidence
- independent confirmation
- limitations
- reproducibility state
- reviewer state

## Fail-closed governance

`TOOLS/review_gate.py` provides the final release gate.

Reference blockers include:

- research question incomplete
- observational provenance missing
- calibration failed or unknown
- data-quality issue unresolved
- selection function uncharacterized when required
- model assumptions invalid or missing
- statistical significance overclaimed
- look-elsewhere effect ignored
- systematic uncertainty uncharacterized
- contradictory evidence unresolved
- independent confirmation missing when required
- reproducibility incomplete
- unsupported discovery claim
- qualified human approval missing

Human approval is required after automated checks pass. Human approval does not make invalid calibration or unsupported statistics acceptable.

## Human authority boundaries

F87 must not autonomously:

- fabricate astronomical observations
- fabricate calibration or significance evidence
- declare a candidate a discovery
- claim independent confirmation that has not occurred
- suppress contradictory evidence
- hide systematic uncertainty
- claim a model is uniquely correct without adequate comparison
- claim a detection is proven solely from a p-value
- exercise autonomous scientific authority

Final scientific interpretation remains with appropriately qualified astronomers, astrophysicists, statisticians, instrumentalists and domain experts.

## End-to-end reference workflow

A typical F87 analysis follows this sequence:

1. Define the target, observable, scale and claim type.
2. Register observational datasets and instrument provenance.
3. Validate calibration, units, timing and data quality.
4. Define sample-selection rules and completeness where relevant.
5. Register background and foreground assumptions.
6. Define physical and statistical models.
7. Fit or compare models with explicit assumptions.
8. Quantify statistical and systematic uncertainty.
9. Account for search multiplicity and look-elsewhere effects.
10. Preserve contradictory evidence and alternative models.
11. Assess whether independent confirmation exists or is required.
12. Record reproducibility information.
13. Match detection and discovery language to the evidence level.
14. Apply the fail-closed review gate.
15. Require qualified human scientific review before release.

## Evaluation and held-out governance suite

The repository includes `evals/evaluate.py`, `evals/held_out.py`, `evals/rubric.md`, and benchmark cases under `benchmarks/`.

Evaluation should test research integrity rather than only whether the workflow produces plausible astronomy prose.

Useful dimensions include:

- provenance enforcement
- calibration enforcement
- data-quality enforcement
- selection-effect handling
- model-assumption enforcement
- significance calibration
- look-elsewhere detection
- systematic-uncertainty enforcement
- contradictory-evidence handling
- independent-confirmation enforcement
- discovery-claim blocking
- reproducibility enforcement
- human-review enforcement

The held-out suite should include tempting false positives, poorly calibrated datasets, biased samples and exaggerated discovery claims.

## Failure states

Useful explicit states include:

```text
QUESTION DEFINITION INCOMPLETE
OBSERVATIONAL PROVENANCE MISSING
CALIBRATION FAILURE
DATA QUALITY FAILED
SELECTION FUNCTION UNKNOWN
MODEL ASSUMPTION INVALID
SIGNIFICANCE OVERCLAIM
LOOK-ELSEWHERE EFFECT UNRESOLVED
SYSTEMATIC UNCERTAINTY UNCHARACTERIZED
CONTRADICTORY EVIDENCE UNRESOLVED
INDEPENDENT CONFIRMATION REQUIRED
REPRODUCIBILITY GAP
DISCOVERY CLAIM NOT ESTABLISHED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate observations, calibration, significance, independent confirmation, reproducibility or human approval.

## Observability

The `observability/` layer records workflow events for audit and debugging.

Useful research telemetry includes:

- datasets registered
- calibration status
- data-quality failures
- selection-function status
- assumptions registered
- significance flags
- look-elsewhere flags
- systematic-uncertainty flags
- contradictory evidence
- confirmation state
- review-gate state
- human-review state

Observability supports auditability. It is not scientific evidence by itself.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## Reproducibility checklist

For an analysis intended to be reproduced, version at minimum:

- question definition
- observation identifiers
- dataset release
- calibration files
- pipeline version
- quality masks
- selection criteria
- background model
- analysis code
- model definition
- priors or parameter ranges
- statistical method
- random seeds where relevant
- software environment
- result tables
- figures
- evidence register
- reviewer state

## L3 Gold Standard

F87 follows the library's L3 Gold Standard structure through specialist agents, deterministic evidence tools, explicit state and safety layers, observability, held-out governance evaluation, CI, fail-closed release gates and mandatory qualified human scientific review.

This maturity designation describes the engineering and governance structure of the repository. It is not proof of an astronomical discovery, observational confirmation, instrument certification, scientific consensus, or universal model validity.

## Extending F87

Common extensions include:

- observatory archives
- survey catalogs
- telescope pipelines
- imaging reduction
- spectroscopy pipelines
- time-domain alert streams
- astrometry systems
- simulation frameworks
- model-fitting libraries
- Bayesian inference systems
- cross-match services
- provenance databases
- experiment tracking
- scientific workflow managers

New integrations should preserve observation provenance, calibration lineage, uncertainty, reproducibility and human scientific review.

## Example applications

F87 can serve as a reference architecture for research involving:

- stellar astrophysics
- exoplanets
- galaxies
- cosmology
- compact objects
- transient astronomy
- gravitational-wave counterparts
- radio astronomy
- infrared astronomy
- X-ray and gamma-ray astronomy
- survey science
- population studies
- time-domain astronomy
- multi-messenger astronomy

Each application requires field-specific methods and evidentiary standards.

## Design principles

1. Define the astronomical claim before selecting data and models.
2. Preserve observation and calibration provenance.
3. Separate raw data, calibrated products, derived measurements and scientific inference.
4. Characterize selection effects, completeness and contamination where relevant.
5. Match statistical claims to the actual search procedure.
6. Account for systematic uncertainty and look-elsewhere effects.
7. Compare plausible models rather than assuming one fitted model is uniquely correct.
8. Distinguish candidate signals from independently confirmed results.
9. Preserve contradictory evidence and reproducibility metadata.
10. Keep final discovery and scientific authority with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Responsible use

Use F87 as an astronomy-research and multi-agent governance reference. Validate observational provenance, calibration, sample selection, statistical assumptions, systematic uncertainty, independent confirmation and field-specific discovery standards against the actual research question before relying on results. Final scientific interpretation remains with appropriately qualified and accountable humans.