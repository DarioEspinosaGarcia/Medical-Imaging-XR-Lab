# SMOKE-TEST-XR-001 — Historical result

Alias retained in filename: SMOKE-XR-001.
Protocol: [SMOKE-TEST-XR-001](../../../tests/SMOKE-TEST-XR-001.md).
Environment: [EXP-001 snapshot](../environment.json).

**Outcome: Reported PASS — retrospective summary evidence, not independently rerun.**

| Field | Value |
| --- | --- |
| Session | Setup work on 2026-09-27–28; exact run timestamp not retained |
| Operator | Dario Espinosa, local setup session |
| Dataset | MRHead, Slicer Sample Data |
| Original software revisions / preset | Not recorded |
| Original repository commit at execution | Not recorded |
| Evidence | E1 in the [evidence register](evidence-register.md) |
| Documentation date | 2026-09-28 |
| Execution during baseline preparation | NOT RUN |

## Criteria and observations

| Criterion | Recorded result | Evidence boundary |
| --- | --- | --- |
| C1: desktop MRHead volume rendering | Not separately evidenced in the retained summary | Do not infer an independent criterion PASS |
| C2: XR session | Reported operational | Prior session summary; no runtime log attached |
| C3: MRHead visible in Quest | Reported PASS | Prior session summary explicitly records visibility |

The historical overall PASS is carried forward as reported, not recomputed as a fully evidenced execution of the newly formalized protocol. Fresh acceptance of C1–C3 needs a repeat run with per-criterion evidence.

No screenshot, scene, dataset checksum or log has been committed for this historical run. There are no FPS/latency measurements. This result does not demonstrate DICOM ingestion, direct-volume Grip or clipping.
