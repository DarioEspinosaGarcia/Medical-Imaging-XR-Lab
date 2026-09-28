# SMOKE-TEST-XR-001 — MRHead volume visibility in XR

Historical alias: SMOKE-XR-001. Experiment: [EXP-001](../experiments/EXP-001-dicom-mri-volumetric-xr/README.md).

## Preconditions

Use the [Windows baseline setup](../docs/setup/windows-host.md). Quest Link must be active, SlicerVirtualReality installed and OpenXR selected. Use MRHead from Slicer Sample Data, not patient data. Record the environment and chosen volume-rendering settings.

## Procedure

1. Start a clean Slicer scene and load MRHead through Sample Data.
2. Select MRHead in Volume Rendering, enable visibility and center the desktop 3D view so the volume is in view.
3. Enable the Virtual Reality view and inspect the scene inside Quest 3.
4. Confirm that the visible object is the MRHead volume rendering. Record a screenshot/mirror capture where possible and the operator's in-headset observation.
5. Record any startup error, disappearance or rendering artifact. Disable VR at the end of the session.

## Acceptance criteria

| Criterion | Required observation |
| --- | --- |
| C1 | MRHead loads and its volume rendering is visible in the desktop 3D view |
| C2 | An XR session opens using the recorded OpenXR setup |
| C3 | MRHead volume rendering is visible inside Quest 3 |

PASS requires C1–C3. This test has no quantitative performance, stereo-calibration or tracking-accuracy threshold. A successful result does not establish DICOM import correctness, surface grabbing or clipping.

Historical outcome: [SMOKE-XR-001 result](../experiments/EXP-001-dicom-mri-volumetric-xr/results/SMOKE-XR-001.md).
