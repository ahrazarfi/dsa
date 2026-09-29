# Scaffold a new DSA problem folder in the current directory and open it in VS Code (Windows counterpart of new.sh).
# Usage: new.ps1 [problem-name]   (prompts if no name is given)
param([Parameter(ValueFromRemainingArguments = $true)] [string[]] $NameParts)
$ErrorActionPreference = 'Stop'

$root = $PSScriptRoot
$name = ($NameParts -join ' ').Trim()
if (-not $name) { $name = Read-Host 'Problem name' }

# "Two Sum" -> "two-sum"
$slug = ($name.ToLower() -replace '[^a-z0-9]+', '-').Trim('-')
if (-not $slug) { Write-Error 'Invalid problem name'; exit 1 }

$dir = Join-Path (Get-Location).Path $slug
$utf8 = New-Object System.Text.UTF8Encoding($false)
if (Test-Path $dir) {
    Write-Host "'$slug' already exists, opening it."
} else {
    New-Item -ItemType Directory -Path $dir | Out-Null
    $template = [System.IO.File]::ReadAllText((Join-Path $root 'template\solution.py')) -replace "`r`n", "`n"
    [System.IO.File]::WriteAllText((Join-Path $dir 'solution.py'), $template, $utf8)
    [System.IO.File]::WriteAllText((Join-Path $dir 'input.txt'), '', $utf8)
    [System.IO.File]::WriteAllText((Join-Path $dir 'output.txt'), '', $utf8)
    Write-Host "Created $dir"
}

# The "DSA layout" VS Code extension watches this file and arranges the panes.
# Falls back to plain tabs if the extension isn't loaded.
$request = Join-Path $root '.open-request'
[System.IO.File]::WriteAllText($request, $dir, $utf8)
Start-Sleep -Seconds 1
if ((Get-Item $request).Length -gt 0 -and (Get-Command code -ErrorAction SilentlyContinue)) {
    [System.IO.File]::WriteAllText($request, '', $utf8)
    & code -r (Join-Path $dir 'solution.py') (Join-Path $dir 'input.txt') (Join-Path $dir 'output.txt')
}
