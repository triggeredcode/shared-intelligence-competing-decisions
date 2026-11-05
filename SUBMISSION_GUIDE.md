# Publication and posting guide

Prepared 5 November 2026; research-status update 6 November 2026. This advice distinguishes public dissemination from
peer-reviewed acceptance. The working paper is being released on GitHub. No journal or preprint-server submission has been made.

Revision 1.1 adds a Bayesian implementation result (Proposition 6.1), exact conditional checks, and five static slides. This narrows the earlier commitment caveat but does not resolve novelty or venue eligibility.

## Recommended route

1. Review the mathematical argument and the disclosed AI contribution with a
   game-theory or information-economics researcher. The present automated checks
   do not replace that review. Obtain and compare the full text of Chi and Yang's
   *Shared Intelligence and Misaligned Firm Entry*, as well as the other closest
   papers. State a specific contribution that those papers do not already make.
2. Revise and take responsibility for the manuscript as its human author. Fill
   in funding, interests, author contributions, and corresponding-author details.
3. Post an accurately labeled working paper or preprint, subject to the selected
   platform's moderation and AI rules. Archive the code separately or together.
4. Consider a journal submission only once the contribution and verification
   are strong enough. A polished PDF does not establish publishability.

## Where to post

### SSRN: an economics-oriented working paper

SSRN is a natural dissemination option for the economic framing, after human
review. It requires an account, author metadata, a full-text PDF, and disclosure
of material AI use. Its policy emphasizes human intellectual contribution and
responsibility. The substantial AI assistance in this manuscript must not be
re-described as grammar editing. Eligibility and acceptance are for SSRN to
determine; this package does not certify them.

Official sources:
- https://www.elsevier.support/ssrn/answer/get-started
- https://www.elsevier.support/ssrn/answer/AI

Use Omkar Tripathi as author and Independent Researcher as affiliation. The
Research repository link can supplement, but does not replace, a valid email where required
by the submission system. Use the email you supplied when entering those fields.

### arXiv: a mathematical/computational preprint

The closest likely subject is Computer Science and Game Theory (cs.GT); an
Economics/Theoretical Economics category may also be relevant. These are fit
suggestions, not category approvals. arXiv requires topical, refereeable content,
moderates submissions, and may require endorsement. Consult the account's actual
endorsement workflow. When a paper is authored in LaTeX, submit the source package
rather than only a PDF. Include `.tex`, `.bib`, `.bbl`, and plot/table inputs;
omit logs, caches, and personal information not meant for release.

Official sources:
- https://info.arxiv.org/help/submit/index.html
- https://info.arxiv.org/help/endorsement.html

Endorsement is not peer review. Posting is not journal acceptance. Do not frame
the note as a newly discovered paradox or an empirically established AI harm.

### GitHub and Zenodo: reproducible artifacts

A GitHub repository under `triggeredcode` can host LaTeX sources and executable
analysis. GitHub alone is not a peer-reviewed publication. Zenodo can preserve
research objects and assign a DOI to a published record; a DOI is an identifier,
not a quality certification. A useful release would include the manuscript,
source, code, parameter files, dependencies, and hashes. Repository: https://github.com/triggeredcode/shared-intelligence-competing-decisions

Official source:
- https://help.zenodo.org/docs/get-started/quickstart/

## Journal fit: International Journal of Game Theory

IJGT publishes original, significant methodological, conceptual or mathematical
contributions to game theory. The subject fits in principle, but this short
model's incremental novelty and specific information restrictions are material editorial
risks. I do not recommend treating it as journal-ready solely because the source
compiles. An editor could reasonably regard it as an illustration of known
monoculture and information-externality results.

Current author guidance recommends LaTeX and the Springer Nature template,
150-250 abstract words, 4-6 keywords, author-year citations, editable source and
PDF, and relevant declarations. The present portable preprint meets the basic
abstract/keyword/citation conventions but is not an IJGT template submission.
The journal's guide also restricts the reference list to published or accepted
works; adapt treatment of preprints to its instructions. Do not silently omit
close unpublished work: discuss it in the text as permitted.

Official sources:
- https://link.springer.com/journal/182/aims-and-scope
- https://link.springer.com/journal/182/submission-guidelines
- https://group.springernature.com/gp/group/ai/ai-guidance-for-researchers-editors-reviewers

The publisher requires human scholarly accountability and transparent AI use.
Whether this extensively AI-assisted research meets the selected venue's policy
must be resolved honestly; disclosure is not a substitute for author-led review.
Check current fees and licensing directly at submission; no fee is quoted here.

## Scientific readiness assessment

Completed: standard mathematical notation; explicit timing and strategy space;
proofs; finite-population extension; countercases; synthetic simulation with
market-level uncertainty; exact rational checks; bibliography; reproducible
LaTeX source and figure.

Still needed before claiming a submission-ready original contribution:
- full-text novelty comparison, especially the close 2026 firm-entry paper;
- substantive human verification of every theorem and the implementation;
- a defensible reason that the commitment or Proposition 6.1 information structure fits the intended application;
- completed personal declarations and a truthful final AI-use statement;
- venue-specific template and reference-policy adaptation.

No real-world experiment has been conducted. A theory journal does not necessarily
require one, but the paper cannot claim real AI-system or macroeconomic effects.
No independent peer review, plagiarism-database screening, or Lean/Coq proof
verification has been performed.
