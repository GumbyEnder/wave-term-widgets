set -euo pipefail

source "$(dirname "$0")/lib.sh"

tz="${WIDGET_TIMEZONE:-$(date +%Z)}"
widget_title "CLOCK"
kv LocalTime "$(date '+%a %H:%M:%S')"
kv Date "$(date '+%Y-%m-%d')"
kv Timezone "$tz"
kv Uptime "$(uptime -p 2>/dev/null || echo unknown)"
