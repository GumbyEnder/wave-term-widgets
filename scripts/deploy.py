from __future__ import annotations

import argparse
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

from widget_config import render_widgets_json


def default_home_candidates() -> list[Path]:
    user_home = Path.home()
    homes: list[Path] = []

    env_home = os.environ.get("WAVETERM_HOME")
    if env_home:
        homes.append(Path(env_home).expanduser())

    homes.extend([
        user_home / ".waveterm",
        user_home / ".config" / "waveterm",
    ])

    deduped: list[Path] = []
    seen: set[str] = set()
    for home in homes:
        key = str(home)
        if key not in seen:
            deduped.append(home)
            seen.add(key)
    return deduped


def existing_home_candidates() -> list[Path]:
    return [home for home in default_home_candidates() if home.exists()]


def write_config(home: Path, content: str, backup: bool = True) -> Path:
    dest_dir = home / "config"
    dest = dest_dir / "widgets.json"
    dest_dir.mkdir(parents=True, exist_ok=True)

    existing = dest.read_text(encoding="utf-8") if dest.exists() else None
    if existing == content:
        return dest

    if backup and dest.exists():
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        shutil.copy2(dest, dest.with_name(f"widgets.json.bak.{stamp}"))

    dest.write_text(content, encoding="utf-8")
    return dest


def latest_backup(home: Path) -> Path | None:
    dest_dir = home / "config"
    backups = sorted(dest_dir.glob("widgets.json.bak.*"), key=lambda p: p.name)
    return backups[-1] if backups else None


def remove_config(home: Path) -> Path | None:
    dest = home / "config" / "widgets.json"
    if dest.exists():
        dest.unlink()
        return dest
    return None


def restore_backup(home: Path) -> Path:
    dest = home / "config" / "widgets.json"
    backup = latest_backup(home)
    if backup is None:
        raise SystemExit(f"No backup found for {home}")

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(backup, dest)
    return dest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate, deploy, remove, or restore WaveTerm widgets.json for Linux or Windows."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--rollback",
        action="store_true",
        help="Restore widgets.json from the latest timestamped backup.",
    )
    mode.add_argument(
        "--remove",
        action="store_true",
        help="Delete widgets.json from the selected WaveTerm home(s).",
    )
    parser.add_argument(
        "--home",
        action="append",
        dest="homes",
        help="WaveTerm home directory to target (repeatable).",
    )
    parser.add_argument(
        "--all-homes",
        action="store_true",
        help="Target every common WaveTerm home candidate instead of just the first one found.",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip making a timestamped backup of an existing widgets.json before writing.",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print the generated JSON instead of writing files.",
    )
    return parser.parse_args()


def resolve_homes(args: argparse.Namespace) -> list[Path]:
    if args.homes:
        return [Path(h).expanduser() for h in args.homes]

    if args.all_homes:
        return default_home_candidates()

    candidates = existing_home_candidates()
    if candidates:
        return [candidates[0]]

    defaults = default_home_candidates()
    return [defaults[0]] if defaults else []


def main() -> int:
    args = parse_args()
    homes = resolve_homes(args)

    if not homes:
        raise SystemExit("No WaveTerm home targets found.")

    if args.rollback:
        for home in homes:
            path = restore_backup(home)
            print(f"Restored {path}")
        return 0

    if args.remove:
        for home in homes:
            removed = remove_config(home)
            if removed is None:
                print(f"No widgets.json at {home}")
            else:
                print(f"Removed {removed}")
        return 0

    content = render_widgets_json()

    if args.print_only:
        sys.stdout.write(content)
        return 0

    written: list[Path] = []
    for home in homes:
        written.append(write_config(home, content, backup=not args.no_backup))

    for path in written:
        print(f"Wrote {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
