# Medical-Imaging-XR-Lab

Research and development laboratory for medical imaging visualization, volumetric rendering and XR interaction using VTK, 3D Slicer, OpenXR and Meta Quest.

## EXP-001 baseline

The initial experiment is [EXP-001: DICOM MRI volumetric XR](experiments/EXP-001-dicom-mri-volumetric-xr/README.md). Its current baseline uses **Windows 11 + 3D Slicer Preview 5.13 + SlicerVirtualReality + OpenXR + Meta Quest 3**. Slicer processes and renders the scene on the Windows PC; the headset is connected through Quest Link. This is a PC VR workflow.

The baseline documents the existing setup and manual observations. It contains no custom application implementation or clipping functionality. Exact build identifiers still need to be captured before claiming a fully reproducible environment.

| Test | Recorded outcome | Qualification |
| --- | --- | --- |
| [SMOKE-TEST-XR-001](experiments/EXP-001-dicom-mri-volumetric-xr/results/SMOKE-XR-001.md) | Reported PASS | MRHead visible in Quest; retrospective conversation evidence |
| [SMOKE-TEST-XR-002](experiments/EXP-001-dicom-mri-volumetric-xr/results/SMOKE-XR-002.md) | Reported PASS for general interaction | Right thumbstick, X+A and green-cube Grip work; direct Grip of MRHead does not |

These outcomes were reported in earlier local sessions, not rerun during repository preparation. MRHead demonstrates sample-volume rendering; it does not validate DICOM ingestion or the complete EXP-001 workflow.

## Repository guide

| Directory | Purpose |
| --- | --- |
| [docs/](docs/README.md) | Architecture, Windows setup and baseline review |
| [experiments/](experiments/README.md) | Experiment scope, environment snapshots and results |
| [src/](src/README.md) | Reserved for future implementation |
| [tests/](tests/README.md) | Manual smoke-test protocols and acceptance criteria |
| [versions/](versions/README.md) | Version inventory and missing reproducibility metadata |
| [data/](data/README.md) | Dataset provenance and local data policy |

Start with the [Windows setup](docs/setup/windows-host.md), then run [test 001](tests/SMOKE-TEST-XR-001.md) and [test 002](tests/SMOKE-TEST-XR-002.md). Record a new dated execution without overwriting the historical results.

## License

[BSD-3-Clause](LICENSE), copyright 2026 Dario Espinosa. Third-party components retain their own licenses; they are not vendored here. No additional Python packages, build system or test framework is required by this documentation baseline.
