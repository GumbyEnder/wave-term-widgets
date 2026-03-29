set -euo pipefail

printf 'SERVICES PANEL\n'
printf '%s\n' '---------------'

printf 'Listening sockets:\n'
if command -v ss >/dev/null 2>&1; then
  ss -tuln 2>/dev/null | sed -n '1,12p' | sed 's/^/  /'
else
  printf '  ss not available\n'
fi

printf '\nDocker containers:\n'
if command -v docker >/dev/null 2>&1; then
  docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null | sed 's/^/  /'
else
  printf '  docker not available\n'
fi
