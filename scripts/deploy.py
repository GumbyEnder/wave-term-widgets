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


def choose_default_home() -> Path | None:
    candidates = default_home_candidates()
    for home in candidates:
        if home.exists():
            return home
    return candidates[0] if candidates else None


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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate and deploy WaveTerm widgets.json for Linux or Windows."
    )
    parser.add_argument(
        "--home",
        action="append",
        dest="homes",
        help="WaveTerm home directory to write (repeatable). Defaults to the first common location found.",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip making a timestamped backup of an existing widgets.json.",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Print the generated JSON instead of writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    content = render_widgets_json()

    if args.print_only:
        sys.stdout.write(content)
        return 0

    if args.homes:
        homes = [Path(h).expanduser() for h in args.homes]
    else:
        default_home = choose_default_home()
        homes = [default_home] if default_home is not None else []

    if not homes:
        raise SystemExit("No WaveTerm home targets found.")

    written: list[Path] = []
    for home in homes:
        written.append(write_config(home, content, backup=not args.no_backup))

    for path in written:
        print(f"Wrote {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
