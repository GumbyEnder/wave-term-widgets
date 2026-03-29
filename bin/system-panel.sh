set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "SYSTEM PANEL"
kv Host "$(hostname 2>/dev/null || echo unknown)"
kv Uptime "$(uptime -p 2>/dev/null || echo unknown)"
kv Load "$(awk '{print $1" "$2" "$3}' /proc/loadavg 2>/dev/null || echo unknown)"

if have free; then
  widget_section "Memory"
  free -h | awk 'NR==1 || NR==2 || NR==3 {print "  " $0}'
fi

widget_section "Disk"
df -h / 2>/dev/null | awk 'NR==1 || NR==2 {print "  " $0}'

widget_section "Top CPU processes"
ps -eo pid,comm,%cpu,%mem --sort=-%cpu 2>/dev/null | awk 'NR==1 {print "  " $0; next} NR<=6 {print "  " $0}'
