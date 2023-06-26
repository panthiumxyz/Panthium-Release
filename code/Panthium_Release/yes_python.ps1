Write-Output "Starting Installation of Panthium's requirements..."

$requirementsFile = "requirements.txt"

Write-Output "Panthium's requirements are being installed on your computer, this won't take long..."

$pythonExecutable = "py"

Get-Content $requirementsFile | ForEach-Object {
    Write-Output "installing: $_ pythonExecutable $pythonExecutable"
    & $pythonExecutable -m pip install $_
}

Write-Output "Done :D"

Write-Output "You are free to press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyUp")