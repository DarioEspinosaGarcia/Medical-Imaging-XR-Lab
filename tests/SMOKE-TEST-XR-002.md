# SMOKE-TEST-XR-002 — General controller interaction

Historical alias: SMOKE-XR-002. Experiment: [EXP-001](../experiments/EXP-001-dicom-mri-volumetric-xr/README.md).

## Preconditions and positive control

Complete [001](SMOKE-TEST-XR-001.md). Both controllers must be available in the XR session. Use a green surface cube as a positive control to distinguish object Grip from volume behavior.

The historical cube's size, location and creation code were not preserved. For a repeat run, this optional Slicer-console fixture creates a uniquely named green model at a known position; record any repositioning. It uses bundled VTK and is not clipping code:

```python
import slicer
import vtk
cubeSource = vtk.vtkCubeSource()
cubeSource.SetXLength(50)
cubeSource.SetYLength(50)
cubeSource.SetZLength(50)
cubeSource.SetCenter(150, 0, 0)
cubeSource.Update()
cube = slicer.modules.models.logic().AddModel(cubeSource.GetOutput())
cube.SetName(slicer.mrmlScene.GenerateUniqueName("XRSmokeCube"))
cube.GetDisplayNode().SetColor(0, 1, 0)
cube.GetDisplayNode().SetVisibility(True)
slicer.util.resetThreeDViews()
```

This fixture is a proposed repeat-run aid and has not been executed during baseline preparation. If it cannot be loaded or reached, record BLOCKED for cube Grip; do not infer FAIL for the XR stack.

## Procedure and criteria

| Step / criterion | Action | Required observation | Role |
| --- | --- | --- | --- |
| C1 | Push the right thumbstick forward/backward | Viewpoint navigation responds | Required |
| C2 | Hold left X + right A together and move the controllers | The scene responds to the two-handed gesture; record which translation, rotation or scaling actions were observed | Required |
| C3 | Place a controller at the green cube, hold Grip, move and release | The cube can be grabbed and repositioned | Required |
| D1 | Attempt the same Grip interaction on MRHead volume rendering | Record whether the volume itself moves; avoid confusing viewpoint or whole-scene motion with volume motion | Diagnostic |

PASS requires C1–C3. D1 is a separately reported volume-interaction probe and is not part of this general-interaction gate. If the objective is direct volumetric manipulation, D1 must pass in a separate acceptance decision; general interaction PASS is insufficient.

Record outcomes per control, errors and evidence. Do not add custom transforms or handlers to make a failed action pass during this baseline. Remove the fixture or close the unsaved test scene after recording the result.

Historical outcome: [SMOKE-XR-002 result](../experiments/EXP-001-dicom-mri-volumetric-xr/results/SMOKE-XR-002.md).
