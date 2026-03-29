
source "$(dirname "$0")/lib.sh"

roots=(
  "${WIDGET_PROJECT_ROOT:-$HOME/Agents/Projects}"
  "$HOME/Projects"
  "$HOME/src"
  "/mnt/nas/agents"
)

widget_title "PROJECT LAUNCHER"

count=0
for root in "${roots[@]}"; do
  [[ -d "$root" ]] || continue
  while IFS= read -r -d '' dir; do
    name="$(basename "$dir")"
    branch=""
    dirty=""
    if [[ -d "$dir/.git" ]]; then
      branch="$(git -C "$dir" branch --show-current 2>/dev/null || true)"
      [[ -n "$(git -C "$dir" status --porcelain 2>/dev/null)" ]] && dirty='*'
    fi
    if [[ -n "$branch" ]]; then
      printf -- '- %s%s [%s]\n' "$name" "$dirty" "$branch"
    else
      printf -- '- %s%s\n' "$name" "$dirty"
    fi
    printf '  %s\n' "$dir"
    count=$((count + 1))
    if [[ "$count" -ge 18 ]]; then
      break 2
    fi
  done < <(find "$root" -mindepth 1 -maxdepth 1 -type d -print0 2>/dev/null | sort -z)
done

if [[ "$count" -eq 0 ]]; then
  printf '(no project directories found)\n'
fi
