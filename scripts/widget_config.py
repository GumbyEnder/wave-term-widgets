from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / "bin"


def cmd(script: str) -> str:
    return f"bash -lc '{(BIN / script).as_posix()}'"


def build_widgets() -> dict[str, dict[str, Any]]:
    widgets: list[dict[str, Any]] = [
        {
            "name": "alienware-hermes",
            "icon": "rectangle-terminal",
            "label": "Alienware → hermes",
            "display_order": 5,
            "meta": {
                "view": "term",
                "controller": "shell",
                "connection": "gumbyender@100.122.198.32",
            },
        },
        {
            "name": "waveterm-mp3",
            "icon": "music",
            "label": "mp3",
            "display_order": 10,
            "meta": {
                "view": "term",
                "controller": "cmd",
                "cmd": 'python -m mp3_player_waveterm --root "K:\\media vault\\music"',
                "cmd:shell": True,
                "cmd:cwd": "K:\\agents\\hermes\\mp3",
                "cmd:runonstart": True,
                "cmd:clearonstart": True,
                "term:fontsize": 12,
                "term:fontfamily": "JetBrains Mono",
            },
        },
        {
            "name": "project-launcher",
            "icon": "folder-open",
            "label": "Projects",
            "display_order": 20,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("project-launcher.sh")},
        },
        {
            "name": "system-panel",
            "icon": "server",
            "label": "System",
            "display_order": 30,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("system-panel.sh")},
        },
        {
            "name": "git-panel",
            "icon": "code-branch",
            "label": "Git",
            "display_order": 40,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("git-panel.sh")},
        },
        {
            "name": "todo-notes",
            "icon": "clipboard-list",
            "label": "Todo",
            "display_order": 50,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("todo-notes.sh")},
        },
        {
            "name": "media-controls",
            "icon": "music",
            "label": "Media",
            "display_order": 60,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("media-controls.sh")},
        },
        {
            "name": "services-panel",
            "icon": "diagram-project",
            "label": "Services",
            "display_order": 70,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("services-panel.sh")},
        },
        {
            "name": "quick-links",
            "icon": "link",
            "label": "Links",
            "display_order": 80,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("quick-links.sh")},
        },
        {
            "name": "clock",
            "icon": "clock",
            "label": "Clock",
            "display_order": 90,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("clock.sh")},
        },
        {
            "name": "weather",
            "icon": "cloud-sun",
            "label": "Weather",
            "display_order": 100,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("weather.sh")},
        },
        {
            "name": "clipboard",
            "icon": "paste",
            "label": "Clipboard",
            "display_order": 110,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("clipboard.sh")},
        },
        {
            "name": "tailscale-status",
            "icon": "network-wired",
            "label": "Tailscale",
            "display_order": 120,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("tailscale.sh")},
        },
        {
            "name": "ai-status",
            "icon": "robot",
            "label": "AI",
            "display_order": 130,
            "meta": {"view": "term", "controller": "cmd", "cmd": cmd("ai-status.sh")},
        },
    ]

    output: dict[str, dict[str, Any]] = {}
    for widget in widgets:
        name = widget["name"]
        output[name] = {
            "icon": widget["icon"],
            "label": widget["label"],
            "display:order": widget["display_order"],
            "blockdef": {"meta": widget["meta"]},
        }
        if "color" in widget:
            output[name]["color"] = widget["color"]
    return output


def render_widgets_json() -> str:
    return json.dumps(build_widgets(), indent=2) + "\n"
