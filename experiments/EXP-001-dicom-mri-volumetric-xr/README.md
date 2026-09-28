# EXP-001 — DICOM MRI volumetric XR

Baseline documented: 2026-09-28. Status: **initial XR baseline documented; end-to-end DICOM MRI experiment pending**.

## Objective and scope

Establish a traceable PC VR environment for viewing MRI volumes and interacting with the Slicer scene. The initial smoke tests use MRHead from Slicer Sample Data. Later DICOM MRI work must separately verify import, series selection and volume geometry before XR evaluation.

This baseline provides architecture, setup instructions, an [environment snapshot](environment.json), manual test protocols and historical result records. No clipping or custom source implementation is included.

## Test register

| Canonical ID | Historical alias | Protocol | Result |
| --- | --- | --- | --- |
| SMOKE-TEST-XR-001 | SMOKE-XR-001 | [Volume visibility in XR](../../tests/SMOKE-TEST-XR-001.md) | [Reported PASS](results/SMOKE-XR-001.md) |
| SMOKE-TEST-XR-002 | SMOKE-XR-002 | [General controller interaction](../../tests/SMOKE-TEST-XR-002.md) | [Reported PASS with volume Grip limitation](results/SMOKE-XR-002.md) |

## Evidence and interpretation

[Evidence register](results/evidence-register.md) identifies the source and confidence of the historical observations. The protocols formalize acceptance criteria retrospectively; they were not captured as pre-registered criteria before those sessions. Existing results do not certify a fresh run of every procedure step.

The 001 PASS is carried forward from a prior session summary. For 002, the user's reported observations support navigation, two-handed scene interaction and cube Grip. Direct volume Grip failed in that setup and remains unresolved. There are no measured FPS, latency or geometric-accuracy results.

## Completion boundaries

The documentation baseline is complete when the requested directories, environment fields, protocols and traceable results exist and the BSD-3-Clause license is retained.

Full reproduction remains pending until exact software/hardware identifiers are captured and both tests are rerun with retained evidence. EXP-001 end-to-end completion additionally requires a documented DICOM MRI dataset and successful import/geometry/XR checks. The sample-volume smoke tests alone do not meet that objective.

Clipping, ROI/plane manipulation, segmentation, performance optimization and clinical validation are outside this baseline. No acceptance of these features is implied.
