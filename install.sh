#!/usr/bin/env bash
# One-time setup for the DSA workflow: venv, VS Code extension, and next-step hints.
# Usage: ./install.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VSIX="$ROOT/dist/dsa-layout-1.0.0.vsix"

# 1. uv (Python env manager), installed if missing
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
if ! command -v uv >/dev/null; then
  echo "uv not found, installing it ..."
  if command -v curl >/dev/null; then
    curl -LsSf https://astral.sh/uv/install.sh | sh
  elif command -v wget >/dev/null; then
    wget -qO- https://astral.sh/uv/install.sh | sh
  else
    echo "Need curl or wget to install uv. See https://docs.astral.sh/uv/" >&2
    exit 1
  fi
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
  command -v uv >/dev/null || { echo "uv installed but not on PATH; open a new shell and rerun." >&2; exit 1; }
fi
echo "Using $(uv --version)"

# 2. Python venv used by the run-current-python task
if [[ ! -x "$ROOT/.venv/bin/python" ]]; then
  echo "Creating .venv ..."
  uv venv "$ROOT/.venv"
else
  echo ".venv already exists."
fi

# 3. The dsa package (run(), list/tree helpers) used by every solution.py
uv pip install -e "$ROOT" --python "$ROOT/.venv/bin/python" -C editable_mode=compat

# 4. Layout extension
if command -v code >/dev/null; then
  echo "Installing the DSA Layout extension ..."
  code --install-extension "$VSIX" --force
else
  echo "'code' not found on PATH, copying the extension into the extensions folder instead."
  for base in "$HOME/.vscode-server/extensions" "$HOME/.vscode/extensions"; do
    if [[ -d "$base" ]]; then
      rm -rf "$base/local.dsa-layout-1.0.0"
      cp -r "$ROOT/tools/dsa-layout" "$base/local.dsa-layout-1.0.0"
      echo "Copied to $base"
    fi
  done
fi

chmod +x "$ROOT/new.sh"

cat <<MSG

Almost done. Two manual steps remain:

1. Add this alias to ~/.zshrc (or ~/.bashrc), then open a new shell:
     alias new='$ROOT/new.sh'

2. Add this to VS Code's keybindings.json (Preferences: Open Keyboard Shortcuts (JSON)):
     { "key": "ctrl+'", "command": "workbench.action.tasks.runTask", "args": "run-current-python" }
   (on some layouts the key is stored as "ctrl+oem_7")

Then reload VS Code (Developer: Reload Window), open $ROOT as the workspace, and run: new two-sum
MSG
