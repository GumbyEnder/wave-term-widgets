set -euo pipefail

source "$(dirname "$0")/lib.sh"

location="${WIDGET_WEATHER_LOCATION:-Edmonton}"
widget_title "WEATHER"

if have curl; then
  summary="$(curl -fsS --max-time 4 "https://wttr.in/${location// /%20}?format=4" 2>/dev/null || true)"
  if [[ -n "$summary" ]]; then
    printf '%s\n' "$summary"
    exit 0
  fi
fi

printf 'Weather unavailable right now.\n'
