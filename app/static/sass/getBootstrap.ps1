Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/bootstrap/archive/v5.0.2.zip" -OutFile ".\v5.0.2.zip"
Expand-Archive -LiteralPath .\v5.0.2.zip -DestinationPath .\
New-Item -Path '.\bootstrap' -ItemType Directory
Move-Item ".\bootstrap-5.0.2\scss" ".\bootstrap\scss"
Remove-Item -r -Force ".\bootstrap-5.0.2\"
Remove-Item ".\v5.0.2.zip"
Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip" -OutFile ".\bootstrap-icons-1.9.1.zip"
Expand-Archive -LiteralPath .\bootstrap-icons-1.9.1.zip -DestinationPath .\
New-Item -Path '..\css\icons' -ItemType Directory
Move-Item ".\bootstrap-icons-1.9.1\*" "..\css\icons"
Remove-Item -r -Force ".\bootstrap-icons-1.9.1"
Remove-Item ".\bootstrap-icons-1.9.1.zip"
