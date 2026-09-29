# dsa

My DSA practice repo, plus the small workflow I use to make solving problems fast:
one command scaffolds a problem, VS Code lays out the panes, and one shortcut runs
the solution against `input.txt` without opening a terminal.

## The workflow

```
$ new two-sum
```

This creates the folder in your **current directory** (so `cd problems/arrays && new two-sum`
puts it in `problems/arrays/`) and opens it in a three-pane layout:

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
| `solution.py` | A `Solution` class plus one `run(...)` call. Paste just the class into LeetCode. |
| `input.txt` | One value per line, one line per argument, LeetCode style. |
| `expected.txt` | Optional. One value per test case. If present, the run is checked against it. |
| `output.txt` | What your solution returned, for reading. Git-ignored. |

`solution.py` imports `run` from the `dsa` package (`dsa/` in this repo, installed into
the venv by the install script), which does all the file handling, parsing, printing and
checking. Rename `solve` to the method name and add its parameters.

Example, `rotateArray(nums, k)`:

```
input.txt        expected.txt
[1, 2, 3, 4, 5]  [3, 4, 5, 1, 2]
2
```

```python
from dsa import run

class Solution:
    def rotateArray(self, nums, k): ...

if __name__ == '__main__':
    run(Solution().rotateArray, in_place=True)
```

### How a run behaves

- **Pass:** silent. `output.txt` holds the answer.
- **Fail:** every failing case is printed with its input, the expected value and what it got,
  and the script exits with an error. The run task reveals the terminal on a non-zero exit,
  so failures pop up on their own.
- **No `expected.txt`** (or an empty one): just run and write `output.txt`.
- **Several test cases** in one file: separate them with a blank line in `input.txt`, and
  put one line per case in `expected.txt`. All cases run, and all failures are reported.
- **Input values** are read as JSON first (`null`, `true`), then Python literals, then as a
  bare string, so `abcba` works unquoted. Quote a string that looks like a literal
  (`"123"` stays a string, `123` is an int).
- **Expected values** use the same syntax as input, so a matrix is `[[1,2],[3,4]]`.
  `output.txt` shows it human-readably instead (one row per line).

### `run()` options by problem type

| Problem | Call |
|---|---|
| Ordinary function | `run(Solution().solve)` |
| Edits its first argument, returns nothing | `run(..., in_place=True)`. A method that legitimately returns `None` needs no flag. |
| Order of results doesn't matter (3Sum, Group Anagrams) | `run(..., unordered=True)`, sorts lists recursively before comparing |
| Several valid answers | `run(..., check=lambda args, out: ...)`, verify instead of matching; `expected.txt` not needed |
| Floating point answers | `run(..., tol=1e-5)` |
| Linked list / tree arguments | `run(..., parse=[to_linked, None])` or `to_tree`; import them from `dsa`. `ListNode`/`TreeNode` results are converted back to lists automatically |
| Design problems (LRUCache, MinStack) | `run_design(LRUCache)`. Line 1 of `input.txt` is the operations, line 2 the arguments; `expected.txt` is the results list with `null` |

Not supported: interactive problems, Codeforces-style stdin, SQL. Adding a new structure
or comparison mode means editing `dsa/` once; every problem gets it.

Tests for the package: `.venv/bin/python -m unittest discover -s tests`.

## Pieces

### `new.sh` / `new.ps1`
Two equivalent scripts, one per platform. Each scaffolds `<slug>/solution.py` (copied from `template/solution.py`), `input.txt`, `expected.txt`, `output.txt`. The name is slugified
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

The install script installs uv if needed, creates `.venv` with `uv venv`, installs the
`dsa` package into it (`uv pip install -e .`), and installs the layout extension (`code --install-extension dist/dsa-layout-1.0.0.vsix`; if `code`
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

1. `uv venv .venv`, then `uv pip install -e . -C editable_mode=compat`
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
dsa/                 the Python package solutions import (run, list/tree helpers)
tests/               tests for dsa/
pyproject.toml       makes dsa/ installable into the venv
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
