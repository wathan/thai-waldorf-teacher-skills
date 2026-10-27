#!/bin/bash
# SessionStart hook for Claude Code cloud sessions.
# Content-only repo (Markdown references + .docx/.pdf sources): ensure the
# tools agents use to read sources and work the GitHub issue tracker exist.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"

# CLI tools: pandoc (.docx -> Markdown), pdftotext (poppler-utils), gh (issues).
missing_pkgs=()
command -v pandoc >/dev/null 2>&1 || missing_pkgs+=(pandoc)
command -v pdftotext >/dev/null 2>&1 || missing_pkgs+=(poppler-utils)
if [ ${#missing_pkgs[@]} -gt 0 ]; then
  apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq "${missing_pkgs[@]}"
fi
command -v gh >/dev/null 2>&1 || echo "warning: gh CLI not found; issue tracker commands in docs/agents/issue-tracker.md will fail" >&2

# Python libraries for scripted inspection of the source documents.
if ! python3 -c "import docx, pypdf" >/dev/null 2>&1; then
  python3 -m pip install --quiet --break-system-packages python-docx pypdf
fi

# Pin gh to this repository so issue commands work without inference.
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  grep -qs '^export GH_REPO=' "$CLAUDE_ENV_FILE" || \
    echo 'export GH_REPO="wathan/thai-waldorf-teacher-skills"' >> "$CLAUDE_ENV_FILE"
fi
