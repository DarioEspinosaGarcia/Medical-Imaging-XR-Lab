# EXP-001 environment capture — 2026-09-28

Capture supplied by Dario Espinosa on 2026-09-28 (Europe/Paris). Repository base for this documentation: `a847552f2435e7616c21b470d2ccc7e66af99898`. This identifies documentation provenance, not the user's checked-out or tested commit.

Snapshot: [environment-2026-09-28.json](../environment-2026-09-28.json). The initial [environment.json](../environment.json) and historical smoke-test records are preserved unchanged.

## Evidence inspected

| Source | Captured values |
| --- | --- |
| User-pasted Slicer console output | Slicer `5.13.0-2026-09-26`; revision `d38aed7`; Python `3.12.10`; VTK `9.6.2` |
| Same output, full Python build string | `3.12.10 (main, Sep 26 2026, 23:23:34) [MSC v.1944 64 bit (AMD64)]` |
| User attachment `imagen(6).png` | SlicerVirtualReality installed-extension page displays revision `c9179ed`, last update Sun Sep 27 2026 |
| User attachment `imagen(7).png` | AMD Radeon RX 6600; 8.0 GB dedicated GPU memory; Windows driver `32.0.21030.2001`, date 2025-09-25 |
| User attachment `imagen(8).png` | AMD application displays current version `25.10.30.02`, release date 2025-09-25 |
| Explicit user report | Meta Horizon Link `208.0.0.57.535`; wired Link connection |

Attachment names identify images inspected in the conversation. Raw screenshots are not committed; this record transcribes the relevant fields. The extension page includes a gallery of upstream example images: those are not evidence of a local smoke-test execution. Its displayed revision is retained as manager metadata; the installed binary revision was not separately queried.

## Interpretation and remaining gaps

- The Windows driver version and the AMD application's displayed version are separate fields.
- The Task Manager shared-memory figure is not dedicated VRAM and is not used to infer installed system RAM.
- The FPS figure visible for another application in the AMD screenshot is not a Slicer measurement. Slicer FPS and latency remain unknown.
- Link application version does not establish the exact OpenXR runtime version or prove the active runtime selection.
- Windows build, CPU/system RAM, headset OS, installed extension binary revision, dataset checksum and rendering settings remain to be captured. Git/VS Code versions remain optional development metadata.
- No new smoke-test execution or result was supplied with this capture. Existing reported outcomes and the MRHead Grip limitation are unchanged.

Local Git synchronization is a separate unresolved workflow: the earlier user terminal output showed modifications to `docs/setup/windows-host.md` blocking pull. No later stash/apply status has been supplied. This remote documentation update does not resolve or discard those local modifications.
