Invoke-WebRequest -Method Get -Uri "https://unpkg.com/@popperjs/core@2.11.6/dist/umd/popper.min.js" -OutFile ".\popper.min.js"
Invoke-WebRequest -Method Get -Uri "https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js" -OutFile ".\bootstrap.min.js"
Move-Item ".\popper.min.js" "..\js\popper.min.js"
Move-Item ".\bootstrap.min.js" "..\js\bootstrap.min.js"
Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/bootstrap/archive/v5.2.2.zip" -OutFile ".\v5.2.2.zip"
Expand-Archive -LiteralPath .\v5.2.2.zip -DestinationPath .\
New-Item -Path '.\bootstrap' -ItemType Directory
Move-Item ".\bootstrap-5.2.2\scss" ".\bootstrap\scss"
Remove-Item -r -Force ".\bootstrap-5.2.2\"
Remove-Item ".\v5.2.2.zip"
Invoke-WebRequest -Method Get -Uri "https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip" -OutFile ".\bootstrap-icons-1.9.1.zip"
Expand-Archive -LiteralPath .\bootstrap-icons-1.9.1.zip -DestinationPath .\
New-Item -Path '..\css\icons' -ItemType Directory
Move-Item ".\bootstrap-icons-1.9.1\*" "..\css\icons"
Remove-Item -r -Force ".\bootstrap-icons-1.9.1"
Remove-Item ".\bootstrap-icons-1.9.1.zip"
Invoke-WebRequest -Method Get -Uri "https://code.jquery.com/jquery-3.6.1.min.js" -OutFile ".\jquery-3.6.1.min.js"
Move-Item ".\jquery-3.6.1.min.js" "..\js\"
