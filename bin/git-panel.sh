set -euo pipefail

source "$(dirname "$0")/lib.sh"

repo="${WIDGET_GIT_DIR:-${PWD}}"
widget_title "GIT PANEL"

if ! git -C "$repo" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'Not inside a git repository.\n'
  exit 0
fi

branch="$(git -C "$repo" branch --show-current 2>/dev/null || echo detached)"
ahead_behind="$(git -C "$repo" rev-list --left-right --count HEAD...@{upstream} 2>/dev/null || true)"
status="$(git -C "$repo" status --short 2>/dev/null | sed -n '1,6p' || true)"
latest="$(git -C "$repo" log -1 --pretty=format:'%h %s' 2>/dev/null || echo 'no commits yet')"

kv Repo "$repo"
kv Branch "$branch"
[[ -n "$ahead_behind" ]] && kv Ahead/Behind "$ahead_behind"
kv Latest "$latest"

widget_section "Status"
if [[ -n "$status" ]]; then
  printf '%s\n' "$status" | sed 's/^/  /'
else
  printf '  clean\n'
fi
