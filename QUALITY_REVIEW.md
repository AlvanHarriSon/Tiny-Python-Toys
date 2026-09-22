# Engineering quality review

## 1. Project Assessment

Reviewed baseline commit `0a0d93e1f4bc21d3337a8eebd431746e5757e894`. All tracked first-party source, documentation,
dependency/configuration files and entrypoints were inspected. Original source
compiled; no tests or CI existed. No database, server, Docker or build system was
present. Original PixelScribe and trading imports required missing environment
dependencies; this was not caused by the changes. Baseline evidence is retained
in the delivered review archive. Validation environment: Windows, Python 3.14.6.

## 2. Major Issues Found

P0: unrestricted eval executes arbitrary Python. P1: documented sqrt fails; disabling password digits/symbols raises; noncryptographic password randomness; import-time prompts/output block reuse.

## 3. Changes Implemented

Replaced eval with a bounded arithmetic AST evaluator; added sqrt and math.sqrt; used secrets/SystemRandom; honored password options; guarded all seven demos/CLI entrypoints; documented actual filenames and in-memory storage. Added behavioral regression tests, a focused CI matrix, and updated
installation/run instructions. No Git history, user data or model resources were deleted.

## 4. Bugs Fixed

The concrete defects listed above are covered by focused regression tests;
external-service behavior is distinguished below from local evidence.

## 5. Architecture Improvements

Retained all existing filenames and public functions. Importable logic is separated from interactive entrypoints through main guards.

## 6. Performance Improvements

No throughput or latency improvement is claimed: no performance benchmark was run.
Resource-lifetime and correctness changes are not reported as measured speedups.

## 7. Testing & Validation

PASS: `7` tests using `python -m unittest discover -s tests -v`.
PASS: `python -m compileall -q .`.
PASS: `python -m pip check` in the shared isolated review environment.
PASS: `python -m ruff check . --select E9,F63,F7,F82` (focused correctness rules).
PASS: `python -m mypy --follow-imports=skip --ignore-missing-imports Tiny-Python-Toys`
(basic checking, not strict coverage of all unannotated bodies or dependencies).
PASS: `git diff --check`.

PASS: CLI baseline reproduced broken sqrt and disabled password options before modifications. Tests cover arithmetic rejection, all password options, import safety, sorting, task state and game scoring.

NOT TESTED locally: Python 3.10/3.12 and Linux/macOS. GitHub CI defines Linux
Python 3.10/3.12/3.14 checks; adding a workflow is not evidence that it has run.
No separate packaging/build target exists; bytecode compilation is the build check.

## 8. Remaining Risks

Intentional security compatibility change: calculator no longer executes arbitrary Python. Recursive quicksort retains worst-case recursion limits; task data and scores remain session-only.

## 9. How to Run

From the repository root, use Python 3.10+ and a virtual environment.
No third-party runtime dependencies are required.

```bash
python Tiny-Python-Toys/simple_calculator.py.py
python -m unittest discover -s tests -v
```

## 10. Recommended Next Steps

If task persistence is desired, design a storage format and recovery behavior separately; this review preserves existing in-memory behavior.
