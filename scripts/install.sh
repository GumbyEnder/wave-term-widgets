set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WAVETERM_HOME="${WAVETERM_HOME:-$HOME/.waveterm}"
DEST_DIR="$WAVETERM_HOME/config"
DEST="$DEST_DIR/widgets.json"

mkdir -p "$DEST_DIR"

if [[ -f "$DEST" ]]; then
  cp "$DEST" "$DEST.bak.$(date +%Y%m%d%H%M%S)"
fi

python3 "$ROOT/scripts/render-widgets-json.py" > "$DEST"

echo "Wrote $DEST"
