
$root = Split-Path $PSScriptRoot -Parent

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 "$root/scripts/deploy.py" --rollback @args
} else {
    & python "$root/scripts/deploy.py" --rollback @args
}
