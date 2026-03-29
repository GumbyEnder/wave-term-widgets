set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "MEDIA CONTROLS"

if have playerctl; then
  status="$(playerctl status 2>/dev/null || true)"
  title="$(playerctl metadata --format '{{artist}} - {{title}}' 2>/dev/null || true)"
  kv Backend playerctl
  kv Status "${status:-unknown}"
  kv NowPlaying "${title:-nothing active}"
  exit 0
fi

if have mpc; then
  kv Backend mpc
  mpc status 2>/dev/null | sed 's/^/  /'
  exit 0
fi

printf 'No playerctl/mpc backend found.\n'
