# Coco Mods

A repo of mods to customize weird unfavorable design choices that Coco has made, while staying up to date with the latest versions.

## Usage

Run this after each Cortex Code update:

```sh
sudo python3 main.py
```

Then fully quit Cortex Code (Cmd+Q) and reopen it to apply.

`sudo` is required because the app's files in `/Applications/Cortex Code.app` are owned by root.

## Mods

- **Sidebar colors** (`scripts/coco_sidebar_colors_patch.py`): sidebar file names show git decoration colors, and file icons keep their theme colors without needing hover. A backup of the original CSS is saved next to it as `workbench.desktop.main.css.bak`.

If the script reports that the target rules weren't found, the app's CSS changed in an update and the patch needs adjusting. Nothing is modified in that case.
