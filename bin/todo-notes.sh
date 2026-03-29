set -euo pipefail

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

printf 'TODO / NOTES\n'
printf '%s\n' '-------------'
printf 'File: %s\n\n' "$file"

awk 'NF {print "  " $0}' "$file" | sed -n '1,20p'
