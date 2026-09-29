# One-time setup for the DSA workflow on Windows: uv, venv, VS Code extension, next-step hints.
# Usage (from the repo folder): powershell -ExecutionPolicy Bypass -File .\install.ps1
$ErrorActionPreference = 'Stop'

$root = $PSScriptRoot
$vsix = Join-Path $root 'dist\dsa-layout-1.0.0.vsix'

# 1. uv (Python env manager), installed if missing
$uvBin = Join-Path $env:USERPROFILE '.local\bin'
if ($env:Path -notlike "*$uvBin*") { $env:Path = "$uvBin;$env:Path" }
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host 'uv not found, installing it ...'
    powershell -NoProfile -ExecutionPolicy Bypass -Command 'irm https://astral.sh/uv/install.ps1 | iex'
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Error 'uv installed but not on PATH; open a new terminal and rerun.'; exit 1
    }
}
Write-Host "Using $(uv --version)"

# 2. Python venv used by the run-current-python task
if (-not (Test-Path (Join-Path $root '.venv\Scripts\python.exe'))) {
    Write-Host 'Creating .venv ...'
    uv venv (Join-Path $root '.venv')
} else {
    Write-Host '.venv already exists.'
}

# 3. The dsa package (run(), list/tree helpers) used by every solution.py
uv pip install -e $root --python (Join-Path $root '.venv\Scripts\python.exe') -C editable_mode=compat

# 4. Layout extension
if (Get-Command code -ErrorAction SilentlyContinue) {
    Write-Host 'Installing the DSA Layout extension ...'
    & code --install-extension $vsix --force
} else {
    Write-Host "'code' not found on PATH. In VS Code run 'Extensions: Install from VSIX...' and pick:"
    Write-Host "  $vsix"
}

@"

Almost done. Two manual steps remain:

1. Add this function to your PowerShell profile (run 'notepad `$PROFILE' to open it), then open a new terminal:
     function new { powershell -NoProfile -ExecutionPolicy Bypass -File '$root\new.ps1' @args }

2. Add this to VS Code's keybindings.json (Preferences: Open Keyboard Shortcuts (JSON)):
     { "key": "ctrl+'", "command": "workbench.action.tasks.runTask", "args": "run-current-python" }
   (on some layouts the key is stored as "ctrl+oem_7")

Then reload VS Code (Developer: Reload Window), open $root as the workspace, and run: new two-sum
"@ | Write-Host
