Write-Output "Starting Installation of Panthium's requirements... `n-------------------------------------------------------"

try {
    $downloadUrl = 'https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe'
    $installerPath = Join-Path $env:TEMP "python-installer.exe"

    $webClient = New-Object System.Net.WebClient

    $webClient.DownloadFile($downloadUrl, $installerPath)

    Write-Output "Python installer downloaded successfully to: $installerPath, please follow the instructions on the Panthium documentation: https://panthiums-organization.gitbook.io `n-------------------------------------------------------"

    $animationChars = @('/', '\', '|')
    $animationDelay = 300 # milliseconds
    $iterationCount = 15

    for ($i = 0; $i -lt $iterationCount; $i++) {
        $animationIndex = $i % $animationChars.Length
        $animationChar = $animationChars[$animationIndex]
        Write-Host -NoNewline $animationChar

        Start-Sleep -Milliseconds $animationDelay
        Write-Host -NoNewline "`b"
}

    Start-Process -FilePath $installerPath -Wait

    $pythonProcess = Get-Process -Name python-installer -ErrorAction SilentlyContinue


    while ($null -ne $pythonProcess) {
        Write-Output "Waiting for Python setup to complete..."
        Start-Sleep -Seconds 1
        $pythonProcess = Get-Process -Name python-installer -ErrorAction SilentlyContinue
    }

    Write-Output "Python installer executed successfully, please follow the instructions on the screen to complete the installation."
}
catch {
    throw "An error occurred while downloading the Python installer: $_"
    exit 1
}

$requirementsFile = "requirements.txt"

Write-Output "Panthium's requirements are being installed on your computer, this won't take long..."

$pythonExecutable = "py"

Get-Content $requirementsFile | ForEach-Object {
    Write-Output "installing: $_"
    & $pythonExecutable -m pip install $_
}

Write-Output "Done :D"

Write-Output "You are free to press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyUp")