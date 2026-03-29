set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "SERVICES PANEL"

widget_section "Listening sockets"
if have ss; then
  ss -tuln 2>/dev/null | sed -n '1,12p' | sed 's/^/  /'
else
  printf '  ss not available\n'
fi

widget_section "Docker containers"
if have docker; then
  docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null | sed 's/^/  /'
else
  printf '  docker not available\n'
fi
