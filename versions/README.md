# Versions and reproducibility

[environment.json](environment.json) is the current inventory. [EXP-001/environment.json](../experiments/EXP-001-dicom-mri-volumetric-xr/environment.json) preserves the initial historical snapshot. The current inventory matches the [2026-09-28 capture snapshot](../experiments/EXP-001-dicom-mri-volumetric-xr/environment-2026-09-28.json), documented in its [evidence record](../experiments/EXP-001-dicom-mri-volumetric-xr/results/2026-09-28-environment-capture.md).

`null` means not captured. The current capture identifies Slicer `5.13.0-2026-09-26`, revision `d38aed7`; unknown values in the initial snapshot remain historical. The extension manager displayed revision is recorded separately from an independently queried installed binary revision. Installed Python/VTK versions belong to the Slicer build; no independent package installation is specified.

Before a reproducibility run, capture the missing fields using the [Windows instructions](../docs/setup/windows-host.md). Create a dated run snapshot rather than rewriting historical unknowns with values from a newer installation. Update the current inventory when the host changes, preserving experiment/run snapshots.

The repository base commit identifies the source tree reviewed for this documentation. It does not identify the commit used during the earlier headset sessions. Each future result must record its own tested commit.
