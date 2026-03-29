set -euo pipefail

printf 'MEDIA CONTROLS\n'
printf '%s\n' '---------------'

if command -v playerctl >/dev/null 2>&1; then
  status="$(playerctl status 2>/dev/null || true)"
  title="$(playerctl metadata --format '{{artist}} - {{title}}' 2>/dev/null || true)"
  if [[ -n "$status" || -n "$title" ]]; then
    printf 'Backend: playerctl\n'
    printf 'Status: %s\n' "${status:-unknown}"
    printf 'Now playing: %s\n' "${title:-nothing active}"
    exit 0
  fi
fi

if command -v mpc >/dev/null 2>&1; then
  printf 'Backend: mpc\n'
  mpc status 2>/dev/null | sed 's/^/  /'
  exit 0
fi

printf 'No playerctl/mpc backend found.\n'
