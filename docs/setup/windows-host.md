# Windows host — EXP-001

## Current inventory — captured 2026-09-28

| Item | Recorded value | Evidence / precision |
| --- | --- | --- |
| OS | Windows 11 | User baseline; build unknown |
| Workspace | `D:\XRLab` | Existing repository setup file |
| Slicer | Preview `5.13.0-2026-09-26`, revision `d38aed7` | User-provided Slicer console output |
| Bundled Python / VTK | Python `3.12.10`; VTK `9.6.2` | Same console output |
| Extension | SlicerVirtualReality; manager displays `c9179ed`, updated 2026-09-27 | Screenshot of installed extension page; installed binary revision not independently queried |
| Backend | OpenXR | Requested baseline and prior session summary |
| Runtime | Meta OpenXR Runtime, configured through Meta Horizon Link | Existing setup file and prior session summary |
| Headset | Meta Quest 3 | User baseline |
| Meta Horizon Link | `208.0.0.57.535` | Explicit user report |
| Connection | USB Quest Link | Wired Link explicitly confirmed by user; no Air Link test recorded |
| GPU | AMD Radeon RX 6600, 8 GB dedicated memory | Task Manager screenshot |
| Windows GPU driver | `32.0.21030.2001`, dated 2025-09-25 | Task Manager screenshot |
| AMD software displayed version | `25.10.30.02` | AMD application screenshot; separate from Windows driver version |
| CPU, system RAM | Not recorded | Capture on the Windows host |
| Git, VS Code | Versions not recorded | Development tools, not XR runtime dependencies |

The [dated capture record](../../experiments/EXP-001-dicom-mri-volumetric-xr/results/2026-09-28-environment-capture.md) documents evidence and remaining gaps. The machine-readable inventory is [versions/environment.json](../../versions/environment.json). Unknown values are JSON `null`, not assumed version pins.

## Setup and launch

1. Install the Slicer Preview 5.13 build selected for the experiment. Record its revision and build date; the current Preview download may be a different build.
2. Install SlicerVirtualReality using Slicer's Extensions Manager for that Slicer build and restart Slicer. Record the extension version/revision shown by the manager.
3. Set up Quest 3 in Meta Horizon Link, connect with USB Quest Link, and select Meta Horizon Link as the active OpenXR runtime in its settings. Enter the PC Link session in the headset.
4. On a host with multiple GPUs, select the high-performance GPU for `SlicerApp-real.exe`. Record the selected GPU and driver.
5. In Slicer, load Sample Data → MRHead. In Volume Rendering select MRHead and enable visibility. Record the preset and rendering settings actually used; the historical values are unknown.
6. Verify the volume in the desktop 3D view. Open Virtual Reality, verify OpenXR, then enable “Show scene in virtual reality”.
7. Run the [001 protocol](../../tests/SMOKE-TEST-XR-001.md), followed by [002](../../tests/SMOKE-TEST-XR-002.md).

The baseline uses Slicer's bundled Python and VTK. No separate `pip install vtk`, OpenXR SDK, SteamVR or custom build is required for this setup. Installation availability must be checked against the selected Preview revision.

## Capture missing metadata

Still capture `winver` output, CPU/system RAM, headset OS version and active runtime confirmation. GPU/driver, Slicer/Python/VTK and Link application versions are now recorded. The Link application version is not assumed to be the OpenXR runtime version. Git and VS Code versions are useful for development provenance only.

In Slicer's Python console, inspect:

```python
import sys
import slicer
import vtk
print("Slicer:", slicer.app.applicationVersion)
print("Revision:", slicer.app.repositoryRevision)
print("Python:", sys.version)
print("VTK:", vtk.vtkVersion.GetVTKVersion())
```

Also copy the Slicer About/build information and SlicerVirtualReality details from Extensions Manager. The user supplied the output of these commands on 2026-09-28; no remote execution on the Windows host was performed.

For each new run record the repository commit, complete environment snapshot, dataset identifier, rendering preset/settings, test date, operator, per-criterion outcome and evidence paths. Keep screenshots limited to the sample dataset. Use a new dated result file and environment snapshot when software or configuration changes.

## Troubleshooting boundaries

- No XR session: check the active runtime and that the headset is in Quest Link before investigating Slicer.
- Desktop volume missing: fix the volume selection/visibility before testing XR.
- Cube Grip works but volume Grip does not: record the known volume-specific limitation; do not treat scene navigation as successful volume grabbing.

Setup reference: [SlicerVirtualReality upstream](https://github.com/KitwareMedical/SlicerVirtualReality), consulted 2026-09-28. Follow the installed build's UI if labels differ.
