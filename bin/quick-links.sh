set -euo pipefail

source "$(dirname "$0")/lib.sh"

widget_title "QUICK LINKS"
cat <<'EOF'
- WaveTerm docs: https://docs.waveterm.dev
- WaveTerm GitHub: https://github.com/wavetermdev/waveterm
- Hermes local wiki: /home/gumbyender/Agents/local-wiki/index.html
- Hermes folder: /mnt/nas/agents/hermes/
- NAS root: /mnt/nas
- Dashboard: http://localhost:8086
- Medusa store: /home/gumbyender/Agents/Projects/Medusa-Store
- Zeeva: /home/gumbyender/Agents/Projects/Zeeva
EOF
