
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / "bin"


def cmd(script: str) -> str:
    return f"bash -lc '{(BIN / script).as_posix()}'"


def build_widgets() -> dict[str, dict[str, object]]:
    widgets = [
        ("project-launcher", "folder-open", "Projects", "#7bd389", 10, "project-launcher.sh"),
        ("system-panel", "server", "System", "#8ab4f8", 20, "system-panel.sh"),
        ("git-panel", "code-branch", "Git", "#f6c177", 30, "git-panel.sh"),
        ("todo-notes", "clipboard-list", "Todo", "#f38ba8", 40, "todo-notes.sh"),
        ("media-controls", "music", "Media", "#cba6f7", 50, "media-controls.sh"),
        ("services-panel", "diagram-project", "Services", "#94e2d5", 60, "services-panel.sh"),
        ("quick-links", "link", "Links", "#fab387", 70, "quick-links.sh"),
        ("clock", "clock", "Clock", "#89dceb", 80, "clock.sh"),
        ("weather", "cloud-sun", "Weather", "#74c7ec", 90, "weather.sh"),
        ("clipboard", "paste", "Clipboard", "#f9e2af", 100, "clipboard.sh"),
        ("tailscale-status", "network-wired", "Tailscale", "#a6e3a1", 110, "tailscale.sh"),
        ("ai-status", "robot", "AI", "#ffb86c", 120, "ai-status.sh"),
    ]

    output: dict[str, dict[str, object]] = {}
    for name, icon, label, color, order, script in widgets:
        output[name] = {
            "icon": icon,
            "label": label,
            "color": color,
            "display:order": order,
            "blockdef": {"meta": {"view": "term", "controller": "cmd", "cmd": cmd(script)}},
        }
    return output


def render_widgets_json() -> str:
    return json.dumps(build_widgets(), indent=2) + "\n"
