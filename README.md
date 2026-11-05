# Shared Intelligence, Competing Decisions

**Policy Adoption and Congestion under Common Advice**  
Omkar Tripathi · Independent Researcher · [Paper repository](https://github.com/triggeredcode/shared-intelligence-competing-decisions)

[Read the paper](manuscript.pdf) · [Five-slide overview](slides/shared-intelligence-slides.pdf) · [Editable slides](slides/shared-intelligence-slides.pptx) · [Verification record](CHECKS.md) · [Review response](REVIEW_RESPONSE.md)

Working paper, version 1.1, 6 November 2026. Not peer reviewed.

## Research question

Can individually attractive access to more accurate, shared advice reduce average economic payoff when agents compete for congestible opportunities?

The paper develops a two-opportunity policy-adoption game. Under explicitly stated assumptions, an interior symmetric adoption equilibrium lowers expected per-agent welfare relative to independent advice. It also studies finite adopter counts, partial commonality, and coordinated benchmarks. Greater commonality has different effects when adoption is held fixed and when adoption responds endogenously.

The baseline result concerns policies selected before signals arrive. Proposition 6.1 also implements the interior symmetric outcome as a Bayesian Nash equilibrium when each agent observes only their own two signals. This is an existence result under a specific information structure, not a theorem about all post-signal decision making. Numerical results are synthetic illustrations, not measured losses in real markets or evidence about particular AI products.

## Reproduce

Use Python 3.12 and install the pinned numerical dependency:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python analysis.py .
python verify_obedience.py .
tectonic --keep-logs --keep-intermediates manuscript.tex
```

The executed build used Python 3.12.14, NumPy 2.3.5, and Tectonic 0.17.0. Tectonic downloads required TeX resources on first use. The manuscript uses LaTeX's article class, AMS mathematics, BibTeX/natbib, and vector figures drawn with TikZ/PGFPlots. The analysis makes no external data or model API calls.

A conventional TeX installation can instead run the following sequence; this alternative was not tested for this release:

```sh
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

## Contents

- `manuscript.pdf`, `manuscript.tex`: compiled paper and editable source.
- `references.bib`, `manuscript.bbl`: bibliography source and compiled entries.
- `analysis.py`: simulations, enumeration, and mathematical consistency checks.
- `verify_obedience.py`, `obedience_results.json`: exact conditional Bayesian payoff checks.
- `slides/`: five static slides in PDF, editable PowerPoint, and individual PNG formats.
- `REVIEW_RESPONSE.md`: accepted improvements and corrections from an external AI review.
- `results.json`, `finite_results.json`, `simulation_results.csv`: numerical outputs.
- `curve.dat`, `commonality.dat`, `table_rows.tex`: generated figure and table inputs.
- `CHECKS.md`: completed checks and their scope.
- `CITATION.cff`: citation metadata.
- `SHA256SUMS.txt`: release-file checksums, excluding the checksum file itself.

## Status and attribution

AI was used in model development, analysis, coding, and manuscript preparation.

The proofs and numerical checks are available for scrutiny. Independent scholarly review and full-text comparison with the closest recent work remain outstanding. No real-world observations or live-model experiments are reported.

No reuse license has been granted. This repository is a working-paper archive, not a journal publication. Report technical issues through the repository's issue tracker.
