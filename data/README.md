# Data

EXP-001 smoke tests use **MRHead** from 3D Slicer Sample Data. Obtain it through Slicer and record the actual local filename, format and checksum for repeat runs. No dataset is bundled here.

MRHead sample-volume visualization is distinct from importing a DICOM MRI series. A future DICOM run must record dataset provenance, series selection, geometry checks and the resulting Slicer volume.

Keep local image datasets, DICOM databases, caches and scene bundles in `data/local/` (ignored by Git). Only dataset descriptions belong here. Before committing screenshots or logs, review them for identifiers and use sample data for this baseline.
