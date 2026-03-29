set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "TAILSCALE"

if have tailscale; then
  kv Status "$(tailscale status 2>/dev/null | sed -n '1p' || echo unknown)"
  kv IP "$(tailscale ip -4 2>/dev/null || true)"
  echo
  tailscale status 2>/dev/null | sed -n '1,6p' | sed 's/^/  /'
  exit 0
fi

printf 'tailscale not installed.\n'
