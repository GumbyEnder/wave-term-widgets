set -euo pipefail

repo="${WIDGET_GIT_DIR:-${PWD}}"
if ! git -C "$repo" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  printf 'GIT PANEL\n'
  printf '%s\n' '----------'
  printf 'Not inside a git repository.\n'
  exit 0
fi

branch="$(git -C "$repo" branch --show-current 2>/dev/null || echo detached)"
status="$(git -C "$repo" status --short 2>/dev/null | sed -n '1,5p' || true)"
latest="$(git -C "$repo" log -1 --pretty=format:'%h %s' 2>/dev/null || echo 'no commits yet')"

printf 'GIT PANEL\n'
printf '%s\n' '----------'
printf 'Repo: %s\n' "$repo"
printf 'Branch: %s\n' "$branch"
printf 'Latest: %s\n' "$latest"
printf '\nStatus:\n'
if [[ -n "$status" ]]; then
  printf '%s\n' "$status" | sed 's/^/  /'
else
  printf '  clean\n'
fi
