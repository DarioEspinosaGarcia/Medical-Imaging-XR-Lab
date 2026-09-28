# Manual XR tests

These tests require the Windows host, Slicer and Quest 3. They cannot be validated by a headless repository check.

| Test ID | Purpose |
| --- | --- |
| [SMOKE-TEST-XR-001](SMOKE-TEST-XR-001.md) | MRHead volume visible in XR |
| [SMOKE-TEST-XR-002](SMOKE-TEST-XR-002.md) | Navigation, two-handed scene interaction and surface-object Grip |

Historical aliases `SMOKE-XR-001` and `SMOKE-XR-002` map one-to-one to these IDs. Their existing result filenames are retained under [EXP-001/results](../experiments/EXP-001-dicom-mri-volumetric-xr/results/evidence-register.md).

## Recording policy

For new executions use PASS only when every required criterion is observed, FAIL when a required criterion fails, BLOCKED when a prerequisite prevents execution, and NOT RUN when no execution occurred. A diagnostic criterion excluded from the overall gate must still retain its own outcome.

Historical records use **Reported PASS** to distinguish conversation evidence from a new execution with retained artifacts. Missing metadata or evidence must be marked as such, not invented.

For a repeat create `YYYY-MM-DD-SMOKE-TEST-XR-NNN-run-N.md` in the experiment's results directory and include:

- Operator, timestamp/timezone and repository commit.
- Environment snapshot and exact dataset/configuration.
- Per-criterion PASS/FAIL/BLOCKED/NOT RUN and actual observation.
- Screenshot/log references, unexpected behavior and overall result.

No automated XR test suite or test framework is added. JSON validity, relative links, whitespace and license preservation can be checked on any development machine; those checks say nothing about headset behavior.
