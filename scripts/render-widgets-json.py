from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / "bin"


def cmd(script: str) -> str:
    return f"bash -lc '{(BIN / script).as_posix()}'"


widgets = {
    "project-launcher": {
        "icon": "folder-open",
        "label": "Projects",
        "color": "#7bd389",
        "display:order": 10,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("project-launcher.sh")}},
    },
    "system-panel": {
        "icon": "server",
        "label": "System",
        "color": "#8ab4f8",
        "display:order": 20,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("system-panel.sh")}},
    },
    "git-panel": {
        "icon": "code-branch",
        "label": "Git",
        "color": "#f6c177",
        "display:order": 30,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("git-panel.sh")}},
    },
    "todo-notes": {
        "icon": "clipboard-list",
        "label": "Todo",
        "color": "#f38ba8",
        "display:order": 40,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("todo-notes.sh")}},
    },
    "media-controls": {
        "icon": "music",
        "label": "Media",
        "color": "#cba6f7",
        "display:order": 50,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("media-controls.sh")}},
    },
    "services-panel": {
        "icon": "diagram-project",
        "label": "Services",
        "color": "#94e2d5",
        "display:order": 60,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("services-panel.sh")}},
    },
    "quick-links": {
        "icon": "link",
        "label": "Links",
        "color": "#fab387",
        "display:order": 70,
        "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd("quick-links.sh")}},
    },
}

print(json.dumps(widgets, indent=2))
