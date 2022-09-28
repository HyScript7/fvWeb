Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip" -OutFile ".\bootstrap-icons-1.9.1.zip"
Expand-Archive -LiteralPath .\bootstrap-icons-1.9.1.zip -DestinationPath .\
New-Item -Path '.\icons' -ItemType Directory
Move-Item ".\bootstrap-icons-1.9.1\*" ".\icons"
Move-Item ".\icons\fonts" ".\"
Remove-Item -r -Force ".\bootstrap-icons-1.9.1"
Remove-Item ".\bootstrap-icons-1.9.1.zip"