set -euo pipefail

widget_title() {
  printf '%s\n' "$1"
  printf '%s\n' "${2:-$(printf '%0.s-' $(seq 1 ${#1}))}"
}

widget_section() {
  printf '\n%s\n' "$1"
  printf '%s\n' "${2:-$(printf '%0.s-' $(seq 1 ${#1}))}"
}

kv() {
  printf '%-12s %s\n' "$1:" "$2"
}

have() {
  command -v "$1" >/dev/null 2>&1
}

trim() {
  local s="$1"
  local n="${2:-96}"
  if (( ${#s} > n )); then
    printf '%s…' "${s:0:n}"
  else
    printf '%s' "$s"
  fi
}
