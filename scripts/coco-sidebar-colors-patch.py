import shutil, sys

p = "/Applications/Cortex Code.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.css"
prefix = ".monaco-workbench.coco-consumer-grade-ui:not(.agent-mode) .part.sidebar .monaco-list-row:not(.selected):not(.focused):not(:hover) .monaco-icon-label"
name_rule = prefix + "{color:var(--stellar-text-subtle)}"
name_patched = prefix + ":not([class*=monaco-decoration-itemColor-]){color:var(--stellar-text-subtle)}"
icon_rule = prefix + ":before{color:var(--stellar-text-subtle)!important}"

s = open(p).read()
if name_patched in s and icon_rule not in s:
    sys.exit("Already patched.")
if s.count(name_rule) != 1 or s.count(icon_rule) != 1:
    sys.exit("Target rules not found exactly once; app CSS may have changed. Nothing modified.")

shutil.copy2(p, p + ".bak")
s = s.replace(name_rule, name_patched).replace(icon_rule, "")
open(p, "w").write(s)
print("Patched. Backup at", p + ".bak", "- restart Cortex Code (Cmd+Q, reopen) to apply.")
