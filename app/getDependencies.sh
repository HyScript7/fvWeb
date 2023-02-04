#!/usr/bin/env sh
echo Downloading and installing CSS \& JS libraries and dependencies.

wget https://unpkg.com/@popperjs/core@2.11.6/dist/umd/popper.min.js
wget https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js
wget https://code.jquery.com/jquery-3.6.1.min.js
wget https://cdn.quilljs.com/1.3.6/quill.min.js
mv ./*.min.js ./static/js/

wget https://cdn.quilljs.com/1.3.6/quill.snow.css
mv ./quill.snow.css ./static/css/

wget https://github.com/twbs/bootstrap/archive/v5.2.2.zip
unzip ./v5.2.2.zip
mkdir ./static/sass/bootstrap
mv ./bootstrap-5.2.2/scss ./static/sass/bootstrap/scss
rm -frd ./bootstrap-5.2.2
rm ./v5.2.2.zip

wget https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip
unzip ./bootstrap-icons-1.9.1.zip
mkdir ./static/css/icons
mv ./bootstrap-icons-1.9.1/* ./static/css/icons
rm -frd ./bootstrap-icons-1.9.1
rm ./bootstrap-icons-1.9.1.zip

echo Done!
