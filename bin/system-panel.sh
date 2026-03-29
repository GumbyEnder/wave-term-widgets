set -euo pipefail

printf 'SYSTEM PANEL\n'
printf '%s\n' '------------'
printf 'Host: %s\n' "$(hostname 2>/dev/null || echo unknown)"
printf 'Uptime: %s\n' "$(uptime -p 2>/dev/null || echo unknown)"
printf 'Load: %s\n' "$(awk '{print $1" "$2" "$3}' /proc/loadavg 2>/dev/null || echo unknown)"

if command -v free >/dev/null 2>&1; then
  printf '\nMemory:\n'
  free -h | awk 'NR==1 || NR==2 || NR==3 {print "  " $0}'
fi

printf '\nDisk:\n'
df -h / 2>/dev/null | awk 'NR==1 || NR==2 {print "  " $0}'

printf '\nTop CPU processes:\n'
ps -eo pid,comm,%cpu,%mem --sort=-%cpu 2>/dev/null | awk 'NR==1 {print "  " $0; next} NR<=6 {print "  " $0}'
