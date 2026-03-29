set -euo pipefail

source "$(dirname "$0")/lib.sh"

file="${WIDGET_TODO_FILE:-$HOME/.local/share/wave-term-widgets/todo.md}"
mkdir -p "$(dirname "$file")"
if [[ ! -f "$file" ]]; then
  cat > "$file" <<'EOF'
# Todo
- [ ] Add your first widget note
- [ ] Collect useful localhost URLs
- [ ] Track things to do in WaveTerm
EOF
fi

widget_title "TODO / NOTES"
kv File "$file"

widget_section "Preview"
awk 'NF {print "  " $0}' "$file" | sed -n '1,12p'
