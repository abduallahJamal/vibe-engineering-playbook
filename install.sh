#!/usr/bin/env bash
set -euo pipefail

# Multi-agent installer for vibe-engineering-playbook
# Supports OpenCode, Claude Code, and Codex CLI (global or project-local).

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS=(vibe vibe-grill vibe-spec-plan vibe-scoped-build vibe-critique vibe-test-gate)

MODE=""
TARGET_DIR=""
INSTALL_OPENCODE=0
INSTALL_CLAUDE=0
INSTALL_CODEX=0

usage() {
  cat <<'EOF'
Usage: ./install.sh [AGENT FLAGS] (--global | --project PATH | --list)

Agent flags:
  --all          Install for OpenCode, Claude Code, and Codex CLI (default if none specified)
  --opencode     Install for OpenCode (.opencode/skills + .opencode/commands/vibe.md)
  --claude       Install for Claude Code (.claude/skills)
  --codex        Install for Codex CLI (.agents/skills)

Scope flags:
  --global       Install into user home config (~/.config/opencode, ~/.claude, ~/.agents)
  --project DIR  Install into a target project directory
  --list         List available skills and exit
  -h, --help     Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --all)
      INSTALL_OPENCODE=1; INSTALL_CLAUDE=1; INSTALL_CODEX=1; shift ;;
    --opencode)
      INSTALL_OPENCODE=1; shift ;;
    --claude)
      INSTALL_CLAUDE=1; shift ;;
    --codex)
      INSTALL_CODEX=1; shift ;;
    --global)
      MODE="global"; shift ;;
    --project)
      MODE="project"; TARGET_DIR="${2:-}"; shift 2 ;;
    --list)
      echo "Available Vibe Engineering skills (${#SKILLS[@]}):"
      for s in "${SKILLS[@]}"; do
        echo "  - $s"
      done
      exit 0 ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

if [[ $INSTALL_OPENCODE -eq 0 && $INSTALL_CLAUDE -eq 0 && $INSTALL_CODEX -eq 0 ]]; then
  INSTALL_OPENCODE=1; INSTALL_CLAUDE=1; INSTALL_CODEX=1
fi

if [[ -z "$MODE" ]]; then
  echo "Error: specify --global, --project PATH, or --list" >&2
  usage >&2
  exit 2
fi

if [[ "$MODE" == "project" ]]; then
  if [[ -z "$TARGET_DIR" ]]; then
    echo "Error: --project requires a target directory path" >&2
    exit 2
  fi
  mkdir -p "$TARGET_DIR"
  TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
fi

copy_skills_into() {
  local dest_base="$1"
  mkdir -p "$dest_base"
  for s in "${SKILLS[@]}"; do
    rm -rf "$dest_base/$s"
    cp -R "$ROOT_DIR/.opencode/skills/$s" "$dest_base/$s"
  done
}

if [[ "$MODE" == "global" ]]; then
  if [[ $INSTALL_OPENCODE -eq 1 ]]; then
    OC_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/opencode"
    copy_skills_into "$OC_DIR/skills"
    mkdir -p "$OC_DIR/commands"
    cp "$ROOT_DIR/.opencode/commands/vibe.md" "$OC_DIR/commands/vibe.md"
    echo "[OK] Installed ${#SKILLS[@]} skills + /vibe command -> $OC_DIR"
  fi
  if [[ $INSTALL_CLAUDE -eq 1 ]]; then
    copy_skills_into "$HOME/.claude/skills"
    echo "[OK] Installed ${#SKILLS[@]} skills -> $HOME/.claude/skills"
  fi
  if [[ $INSTALL_CODEX -eq 1 ]]; then
    copy_skills_into "$HOME/.agents/skills"
    echo "[OK] Installed ${#SKILLS[@]} skills -> $HOME/.agents/skills"
  fi
else
  if [[ $INSTALL_OPENCODE -eq 1 ]]; then
    copy_skills_into "$TARGET_DIR/.opencode/skills"
    mkdir -p "$TARGET_DIR/.opencode/commands"
    cp "$ROOT_DIR/.opencode/commands/vibe.md" "$TARGET_DIR/.opencode/commands/vibe.md"
    echo "[OK] Installed ${#SKILLS[@]} skills + /vibe command -> $TARGET_DIR/.opencode"
  fi
  if [[ $INSTALL_CLAUDE -eq 1 ]]; then
    copy_skills_into "$TARGET_DIR/.claude/skills"
    echo "[OK] Installed ${#SKILLS[@]} skills -> $TARGET_DIR/.claude/skills"
  fi
  if [[ $INSTALL_CODEX -eq 1 ]]; then
    copy_skills_into "$TARGET_DIR/.agents/skills"
    echo "[OK] Installed ${#SKILLS[@]} skills -> $TARGET_DIR/.agents/skills"
  fi
fi
