#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

./scripts/sync-platforms.sh
./scripts/sync-platforms.sh --check
python3 scripts/validate.py --github-annotations
echo "Ready to push: git push -u origin main"
