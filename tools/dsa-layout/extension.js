const vscode = require('vscode');
const fs = require('fs');
const path = require('path');

// new.sh writes a problem folder path into <dsa root>/.open-request;
// this watches for it and lays out: solution.py | input.txt / output.txt
const REQUEST = '.open-request';

async function handle(file) {
  let dir;
  try { dir = fs.readFileSync(file, 'utf8').trim(); } catch { return; }
  if (!dir || !fs.existsSync(path.join(dir, 'solution.py'))) return;
  fs.writeFileSync(file, '');

  await vscode.commands.executeCommand('workbench.action.closeAllEditors');
  await vscode.commands.executeCommand('vscode.setEditorLayout', {
    orientation: 0,
    groups: [{ size: 0.5 }, { size: 0.5, groups: [{}, {}] }],
  });
  const open = async (name, col, focus) => {
    const doc = await vscode.workspace.openTextDocument(path.join(dir, name));
    await vscode.window.showTextDocument(doc, { viewColumn: col, preserveFocus: !focus });
  };
  await open('input.txt', 2, false);
  await open('output.txt', 3, false);
  await open('solution.py', 1, true);
}

function activate(context) {
  for (const folder of vscode.workspace.workspaceFolders || []) {
    const pattern = new vscode.RelativePattern(folder, REQUEST);
    const w = vscode.workspace.createFileSystemWatcher(pattern);
    const run = (uri) => handle(uri.fsPath);
    w.onDidCreate(run); w.onDidChange(run);
    context.subscriptions.push(w);
  }
}
exports.activate = activate;
