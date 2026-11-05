# Verification record

Version: 1.1, 6 November 2026.

## Passed

- Tectonic 0.17.0 compiled the complete LaTeX manuscript, ran BibTeX, and resolved
  cross-references. The final log contains no overfull/underfull boxes, undefined
  references, or LaTeX/natbib warnings.
- Bibliography audit: all 13 BibTeX entries are cited; every citation key resolves.
- Cross-reference audit: 32 unique labels, all referenced labels defined.
- Abstract: 202 words. Five keywords. Author block uses the supplied name and
  affiliation; the public link points directly to the paper repository.
- 200,000 synthetic markets rerun with the documented seed and NumPy version.
- Exact enumeration at N=4 for four adoption rates agrees within 2.85e-14.
- 6,564 interior mixed-equilibrium parameter cases check the sign identity.
- 1,404 finite-count cases checked with exact Python Fraction arithmetic.
- The calibration's pure equilibrium count is 41 and best fixed adopter count is
  16. Fixed-count coordination identity checked for every count from 0 to 100.
- Four figures: timing diagram, adoption-region diagram, commonality comparative
  statics, and the adoption-payoff curve. Quantitative inputs are equations or
  reproducibly generated numerical data, not generative artwork.
- Plot-range check includes the minimum of the endogenous-commonality curve;
  no plotted segment is hidden below the axis limits.
- All 12 pages rendered with Poppler and inspected; mathematical pages and plots
  also inspected at larger scale. Fonts are embedded. PDF title/author metadata
  and extracted text were checked. No unresolved `??` markers remain.

- Exact Bayesian conditional enumeration: 37 equilibrium cases / 148 labeled own-signal types, plus 16 off-equilibrium types. All assertions pass.
- Existing numerical output files rerun byte-for-byte; new obedience output also matches.
- The exact commonality threshold is 203/792; the disputed arXiv reference was confirmed at its official record.
- Five slides rendered and inspected individually. PowerPoint package integrity passed; the editable chart and its PDF export were checked for correct markers, axes, and values.

## Scope of these checks

These are automated computational and document checks plus AI-assisted visual
review, not an independent human referee report. No Lean/Coq certificate,
Turnitin/iThenticate database scan, real-market validation, or live-AI experiment
was performed. The closest 2026 firm-entry paper was available only through its
indexed abstract, leaving its exact overlap unresolved. Human author approval,
venue eligibility, and originality are not certified by this checklist.
