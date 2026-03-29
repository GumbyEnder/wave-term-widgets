source "$(dirname "$0")/lib.sh"

base_url="${WIDGET_AI_BASE_URL:-http://100.109.144.124:1234/v1/models}"
widget_title "AI STATUS"

if ! have curl; then
  printf 'curl not available.\n'
  exit 0
fi

payload="$(curl -fsS --max-time 4 "$base_url" 2>/dev/null || true)"
if [[ -z "$payload" ]]; then
  printf 'Local AI endpoint unreachable.\n'
  exit 0
fi

printf '%s' "$payload" | python3 -c 'import json,sys
obj = json.load(sys.stdin)
data = obj.get("data", []) if isinstance(obj, dict) else []
print(f"Models: {len(data)}")
for item in data[:4]:
    mid = item.get("id") or item.get("name") or "unknown"
    print(f"  - {mid}")'
