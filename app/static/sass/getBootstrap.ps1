Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/bootstrap/archive/v5.0.2.zip" -OutFile ".\v5.0.2.zip"
Expand-Archive -LiteralPath .\v5.0.2.zip -DestinationPath .\
New-Item -Path '.\bootstrap' -ItemType Directory
Move-Item ".\bootstrap-5.0.2\scss" ".\bootstrap\scss"
Remove-Item -r -Force ".\bootstrap-5.0.2\"
Remove-Item ".\v5.0.2.zip"