set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "CLIPBOARD"

text=""
backend=""
if have wl-paste; then
  text="$(wl-paste 2>/dev/null || true)"
  backend="wl-paste"
elif have xclip; then
  text="$(xclip -selection clipboard -o 2>/dev/null || true)"
  backend="xclip"
elif have xsel; then
  text="$(xsel --clipboard --output 2>/dev/null || true)"
  backend="xsel"
elif have pbpaste; then
  text="$(pbpaste 2>/dev/null || true)"
  backend="pbpaste"
fi

kv Backend "${backend:-none}"

if [[ -z "$text" ]]; then
  printf 'No clipboard text available.\n'
  exit 0
fi

text="${text//$'\r'/}"
first_line="${text%%$'\n'*}"
kv Preview "$(trim "$first_line" 96)"
kv Chars "${#text}"
