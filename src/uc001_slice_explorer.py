# SPDX-License-Identifier: BSD-3-Clause
"""UC-001 / increment 01A: MRI slice exploration inside 3D Slicer."""

import math

import slicer
import vtk


class SliceExplorer:
    """Use Slicer's Red slice as the exploration plane.

    This changes the Red view's layers, orientation and position.
    Run in a sample-data scene with MRHead already loaded.
    """

    def __init__(self, volume):
        if volume is None or not volume.IsA("vtkMRMLScalarVolumeNode"):
            raise ValueError("Select a scalar volume such as MRHead.")

        if volume.GetImageData() is None:
            raise ValueError("The selected volume has no image data.")

        red_widget = slicer.app.layoutManager().sliceWidget("Red")
        if red_widget is None:
            raise RuntimeError(
                "Select the Four-up layout in Slicer, then run again."
            )

        self.volume = volume
        self.logic = red_widget.sliceLogic()
        self.slice_node = red_widget.mrmlSliceNode()

        # Keep the diagnostic plane tied to this volume only.
        composite = self.logic.GetSliceCompositeNode()
        composite.SetBackgroundVolumeID(volume.GetID())
        composite.SetForegroundVolumeID(None)
        composite.SetLabelVolumeID(None)

        self.slice_node.SetOrientationToAxial()
        self.logic.FitSliceToAll()

        # Center the plane on the volume's bounds in world RAS coordinates.
        bounds = [0.0] * 6
        volume.GetRASBounds(bounds)
        center = [
            (bounds[0] + bounds[1]) / 2.0,
            (bounds[2] + bounds[3]) / 2.0,
            (bounds[4] + bounds[5]) / 2.0,
        ]
        self.slice_node.JumpSliceByCentering(*center)
        self.slice_node.SetSliceVisible(True)

        self.initial_pose = vtk.vtkMatrix4x4()
        self.initial_pose.DeepCopy(self.slice_node.GetSliceToRAS())

        # Preserve the original volume-rendering visibility for restoration.
        self.rendering_states = []
        for index in range(volume.GetNumberOfDisplayNodes()):
            display = volume.GetNthDisplayNode(index)
            if display and display.IsA("vtkMRMLVolumeRenderingDisplayNode"):
                self.rendering_states.append(
                    (display, display.GetVisibility())
                )

        print("UC-001 / 01A ready: Red slice visible in 3D.")

    def move(self, distance_mm):
        """Move relative to the current position, along the slice normal."""
        distance_mm = float(distance_mm)
        if not math.isfinite(distance_mm):
            raise ValueError("Distance must be finite.")

        offset = self.logic.GetSliceOffset()
        self.logic.SetSliceOffset(offset + distance_mm)

    def reset(self):
        """Restore the plane pose established when this explorer started."""
        self.slice_node.GetSliceToRAS().DeepCopy(self.initial_pose)
        self.slice_node.UpdateMatrices()
        self.slice_node.SetSliceVisible(True)

    def show_volume(self, visible):
        """Toggle volume rendering without hiding the slice image."""
        for display, _ in self.rendering_states:
            display.SetVisibility(bool(visible))

    def finish(self):
        """Hide the 3D slice and restore original rendering visibility."""
        self.slice_node.SetSliceVisible(False)
        for display, original_visibility in self.rendering_states:
            display.SetVisibility(original_visibility)