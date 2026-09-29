# dsa

My DSA practice repo, plus the small workflow I use to make solving problems fast:
one command scaffolds a problem, VS Code lays out the panes, and one shortcut runs
the solution against `input.txt` without opening a terminal.

## The workflow

```
$ new two-sum
```

This creates a folder and opens it in a three-pane layout:

```
+---------------------+---------------+
|                     |  input.txt    |
|   solution.py       +---------------+
|                     |  output.txt   |
+---------------------+---------------+
```

Edit `input.txt`, press **Ctrl+'**, read the result in `output.txt`.

### Per-problem files

| File | Purpose |
|---|---|
| `solution.py` | A `Solution` class plus a small runner block. stdin/stdout are redirected to the two files below. |
| `input.txt` | One Python literal per line, one line per argument (LeetCode style). |
| `output.txt` | Whatever the solution prints. Git-ignored. |

Example `input.txt` for `rotateArray(nums, k)`:

```
[1, 2, 3, 4, 5]
2
```

The runner in `solution.py` parses every non-empty line with `ast.literal_eval`,
calls `Solution().<method>(*args)`, and prints the return value. If the method returns
`None` (in-place problems) it prints the first argument instead. Lists print
space-separated. Rename `solve` to your method name and add its parameters.

Because the algorithm lives in the class and the runner is separate, you can paste
just the class into LeetCode.

## Pieces

### `new.sh` / `new.ps1`
Two equivalent scripts, one per platform. Each scaffolds `<slug>/solution.py` (copied from `template/solution.py`), `input.txt`, `output.txt`. The name is slugified
(`"Two Sum"` becomes `two-sum`); with no argument it prompts. If the folder already
exists it just reopens it.

It then writes the folder path to `.open-request` and waits one second for the layout
extension to pick it up. If the extension didn't (the file is still non-empty), it
clears the file and falls back to `code -r` with three plain tabs.

### `tools/dsa-layout/` (VS Code extension)
A tiny local extension that watches `.open-request` in the workspace root. When a path
appears it closes all editors, sets the 2-column layout above, and opens the three
files. `.open-request` is just the handoff channel between the script and the
extension, so it stays in the repo folder (git-ignored).

### `.vscode/tasks.json`
Defines a task `run-current-python` that runs the open file with the venv's Python (`.venv/bin/python`, or `.venv\\Scripts\\python.exe` on Windows).
`reveal: silent` keeps the terminal hidden on success and opens it if the run fails,
so tracebacks aren't lost. The `$python` problem matcher also lists them in the
Problems panel.

## Setup

Works on Linux, macOS, WSL and native Windows. Environments are managed with
[uv](https://docs.astral.sh/uv/); the install script installs it if it's missing.

**Linux / macOS / WSL**

```
git clone git@github.com:ahrazarfi/dsa.git && cd dsa
./install.sh
```

**Windows (PowerShell)**

```
git clone git@github.com:ahrazarfi/dsa.git; cd dsa
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The install script installs uv if needed, creates `.venv` with `uv venv`, and installs
the layout extension (`code --install-extension dist/dsa-layout-1.0.0.vsix`; if `code`
isn't on PATH, the bash script copies it into the extensions folder and the PowerShell
script tells you to use *Extensions: Install from VSIX...*). It then prints the two
lines you still add by hand:

- **The `new` command.** Linux/macOS/WSL: `alias new='~/dsa/new.sh'` in `~/.zshrc`.
  Windows: a function in your PowerShell profile (`notepad $PROFILE`), which bypasses the
  default script execution policy:
  ```powershell
  function new { powershell -NoProfile -ExecutionPolicy Bypass -File 'C:\path\to\dsa\new.ps1' @args }
  ```
- **The shortcut**, in VS Code's `keybindings.json`:
  ```json
  {
      "key": "ctrl+'",
      "command": "workbench.action.tasks.runTask",
      "args": "run-current-python"
  }
  ```
  On some keyboard layouts VS Code stores the key as `ctrl+oem_7`.

Then reload VS Code (*Developer: Reload Window*) and open the repo folder as the
workspace, since the extension watches the workspace root. On WSL, run the installer
inside WSL, so the extension goes into the VS Code server.

`code` must be on PATH (it is inside a VS Code terminal) for the fallback in `new`.

### Manual setup

1. `uv venv .venv`
2. The `new` command, as above.
3. In VS Code run *Extensions: Install from VSIX...* and pick `dist/dsa-layout-1.0.0.vsix`.
4. The keybinding, as above.

### Rebuilding the extension

```
cd tools/dsa-layout && npx @vscode/vsce package --out ../../dist/dsa-layout-1.0.0.vsix
```

## Layout

```
new.sh / new.ps1     scaffold command (bash / PowerShell)
install.sh / .ps1    one-time setup (bash / PowerShell)
template/solution.py the file every new problem starts from
dist/                packaged .vsix of the extension
tools/dsa-layout/    VS Code layout extension
.vscode/tasks.json   run-current-python task
<problem-slug>/      one folder per problem
```

## Notes

- Codeforces-style problems (one long input stream, not one literal per line) don't fit
  the literal-per-line format. Replace the runner block with manual `input().split()`
  parsing for those.
- Tracebacks go to stderr, so they show in the terminal panel, not in `output.txt`.
