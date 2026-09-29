#!/usr/bin/env bash
# Scaffold a new DSA problem folder and open it in VS Code.
# Usage: new.sh [problem-name]   (prompts if no name is given)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

name="${*:-}"
if [[ -z "$name" ]]; then
  read -rp "Problem name: " name
fi

# "Two Sum" -> "two-sum"
slug="$(echo "$name" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')"
[[ -n "$slug" ]] || { echo "Invalid problem name" >&2; exit 1; }

dir="$ROOT/$slug"
if [[ -e "$dir" ]]; then
  echo "'$slug' already exists, opening it."
else
  mkdir -p "$dir"
  cp "$ROOT/template/solution.py" "$dir/solution.py"
  : > "$dir/input.txt"
  : > "$dir/output.txt"
  echo "Created $dir"
fi

# The "DSA layout" VS Code extension watches this file and arranges the panes.
# Falls back to plain tabs if the extension isn't loaded.
echo "$dir" > "$ROOT/.open-request"
sleep 1
if [[ -s "$ROOT/.open-request" ]] && command -v code >/dev/null; then
  : > "$ROOT/.open-request"
  code -r "$dir/solution.py" "$dir/input.txt" "$dir/output.txt"
fi
