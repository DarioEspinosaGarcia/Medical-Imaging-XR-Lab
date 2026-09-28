# Versions and reproducibility

[environment.json](environment.json) is the baseline inventory. [EXP-001/environment.json](../experiments/EXP-001-dicom-mri-volumetric-xr/environment.json) is the experiment snapshot; the two match at baseline creation.

`null` means not captured. Slicer Preview 5.13 is a version family, not an exact build pin. Installed Python/VTK versions belong to the Slicer build; no independent package installation is specified.

Before a reproducibility run, capture the missing fields using the [Windows instructions](../docs/setup/windows-host.md). Create a dated run snapshot rather than rewriting historical unknowns with values from a newer installation. Update the current inventory when the host changes, preserving experiment/run snapshots.

The repository base commit identifies the source tree reviewed for this documentation. It does not identify the commit used during the earlier headset sessions. Each future result must record its own tested commit.
