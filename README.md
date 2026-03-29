## Widgets included

Core widgets:
- Project Launcher — jump into common project directories and see git state
- System Panel — CPU, RAM, disk, uptime, and top processes
- Git Panel — current branch, status, and latest commit
- Todo / Notes — quick scratchpad viewer for a local markdown todo file
- Media Controls — now-playing summary for playerctl/mpc-compatible players
- Services Panel — local listening services and Docker containers
- Quick Links — fast access to the terminals, dashboards, and local tools you use most

Popular add-ons:
- Clock — quick time/date glance
- Weather — one-line local weather
- Clipboard — short clipboard preview
- Tailscale — VPN / network status
- AI Status — local LM Studio / OpenAI-compatible endpoint check

## Preview

![WaveTerm widget gallery](assets/widget-gallery.svg)

## How WaveTerm custom widgets work

WaveTerm custom widgets are defined in:

`<WAVETERM_HOME>/config/widgets.json`

This repo keeps the widget command logic in `bin/` and provides a generator that renders a WaveTerm-ready `widgets.json` with absolute paths for your machine.

## Install

From the repo root:

Linux/macOS:

```bash
./scripts/install.sh
```

Windows PowerShell:

```powershell
.\scripts\install.ps1
```

Or run the cross-platform deploy script directly:

```bash
python3 scripts/deploy.py
```

By default this writes to the first WaveTerm home it finds, usually one of:

- `$HOME/.waveterm/config/widgets.json`
- `$HOME/.config/waveterm/config/widgets.json`

If your WaveTerm home is different, set `WAVETERM_HOME` first or pass `--home`:

```bash
WAVETERM_HOME="$HOME/.config/waveterm" ./scripts/install.sh
python3 scripts/deploy.py --home "$HOME/.config/waveterm"
```

It also makes a timestamped backup of any existing `widgets.json` before replacing it.

## Generate the JSON manually

```bash
python3 scripts/render-widgets-json.py > /tmp/widgets.json
```

## Edit the widget list

- `bin/project-launcher.sh`
- `bin/system-panel.sh`
- `bin/git-panel.sh`
- `bin/todo-notes.sh`
- `bin/media-controls.sh`
- `bin/services-panel.sh`
- `bin/quick-links.sh`
- `bin/clock.sh`
- `bin/weather.sh`
- `bin/clipboard.sh`
- `bin/tailscale.sh`
- `bin/ai-status.sh`

## Notes

- The scripts are dependency-light and should work on a plain Linux desktop.
- `media-controls` uses `playerctl` first, then `mpc`.
- `services-panel` shows listening ports and Docker containers when available.
- `todo-notes` reads from `~/.local/share/wave-term-widgets/todo.md` by default.
- `weather` uses `wttr.in` if available, with `Edmonton` as the default location.
- `ai-status` checks the local LM Studio-compatible endpoint at `100.109.144.124:1234` by default.

## Project status

Good next additions later:
- Pomodoro / timer
- Calendar / today agenda
- Log tail widget
- Network / VPN status
- More interactive project and service launchers
