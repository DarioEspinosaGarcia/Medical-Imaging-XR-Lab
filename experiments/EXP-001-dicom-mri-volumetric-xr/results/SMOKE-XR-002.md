# SMOKE-TEST-XR-002 — Historical result

Alias retained in filename: SMOKE-XR-002.
Protocol: [SMOKE-TEST-XR-002](../../../tests/SMOKE-TEST-XR-002.md).
Environment: [EXP-001 snapshot](../environment.json).

**Outcome: Reported PASS for general interaction; direct-volume Grip failed in the observed setup.**

| Field | Value |
| --- | --- |
| Session / operator | 2026-09-28, Dario Espinosa |
| Exact run time | Not recorded; report timestamps are in the evidence register |
| Scene | MRHead volume rendering and green surface cube |
| Original software revisions / preset / cube dimensions | Not recorded |
| Original repository commit at execution | Not recorded |
| Evidence | E2 in the [evidence register](evidence-register.md) |
| Documentation date | 2026-09-28 |
| Execution during baseline preparation | NOT RUN |

## Criteria and observations

| Criterion | Outcome | Actual reported observation |
| --- | --- | --- |
| C1: right thumbstick | Reported PASS | Right thumbstick navigation works |
| C2: left X + right A | Reported PASS | Combined control works; individual translation/rotation/scale checks were not separately retained |
| C3: surface cube Grip | Reported PASS | Green cube can be grabbed with Grip |
| D1: MRHead volume Grip | Reported FAIL / known limitation | Grip does not move MRHead volume rendering |

This general-interaction gate deliberately distinguishes navigation, whole-scene interaction and a surface-object positive control from direct volume manipulation. The diagnostic failure remains visible and unresolved. It must not be relabeled as successful volumetric manipulation or attributed to a proven root cause.

The repeat-run cube fixture in the protocol was added during documentation and is not the preserved historical fixture. No screenshots, controller logs or scene files are attached to this result. A fresh reproducibility run remains pending.
