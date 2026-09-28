# EXP-001 architecture

## Current deployment

| Component | Responsibility | Execution location |
| --- | --- | --- |
| 3D Slicer Preview 5.13 | Load image data and maintain the MRML scene | Windows 11 PC |
| VTK bundled with Slicer | Volume and surface rendering | PC GPU/CPU |
| SlicerVirtualReality | Connect the Slicer scene and controller interaction to XR | Slicer process |
| OpenXR loader and Meta runtime | XR session, headset views and tracked input | Windows PC |
| Meta Horizon Link / Quest Link | PC-to-headset connection | PC and headset |
| Meta Quest 3 and controllers | Display and user input | Headset/controllers |

MRHead is loaded into Slicer as a scalar volume and displayed through Volume Rendering. SlicerVirtualReality exposes the selected 3D scene to the XR session. Controller input can change the viewpoint or the scene; the green surface cube is the positive control for object grabbing.

The planned DICOM route is series import into Slicer, volume inspection, volume rendering and XR visualization. That route has not been validated by the MRHead smoke tests. Volume rendering does not require conversion to a surface mesh or export of an STL file.

## Boundaries demonstrated by the baseline

- General scene interaction and surface-object Grip have reported positive results.
- Direct Grip of MRHead volume rendering did not move the volume in the observed setup. Its cause is not established. This is not a claim about all SlicerVirtualReality versions or volume configurations.
- Controller transform nodes have been observed in the earlier session, but this baseline does not add or certify a third smoke test.
- Rendering is hosted on the PC; no standalone Quest application, cloud service or network DICOM integration is implemented.
- Clipping, cutting planes, segmentation, surgical planning, hand tracking and multi-user synchronization are outside this baseline.

## Upstream references

Consulted on 2026-09-28. These describe upstream behavior, not proof of the locally installed revision:

- [SlicerVirtualReality source and setup/controller documentation](https://github.com/KitwareMedical/SlicerVirtualReality).
- [3D Slicer Volume Rendering documentation](https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html).
- [3D Slicer source](https://github.com/Slicer/Slicer).
- [VTK source](https://github.com/Kitware/VTK).

Use the [version inventory](../versions/environment.json) to separate known component names from unknown build identifiers.
