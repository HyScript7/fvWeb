#!/bin/bash
# Run this script to download boostrap scss, this is required to run the server without using docker.
wget https://unpkg.com/@popperjs/core@2.11.6/dist/umd/popper.min.js
wget https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.min.js
mv ./*.min.js ../js/
wget https://github.com/twbs/bootstrap/archive/v5.2.2.zip
unzip ./v5.2.2.zip
mkdir bootstrap
mv ./bootstrap-5.2.2/scss ./bootstrap/scss
rm -frd ./bootstrap-5.2.2
rm ./v5.2.2.zip
wget https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip
unzip ./bootstrap-icons-1.9.1.zip
mkdir ../css/icons
mv ./bootstrap-icons-1.9.1/* ../css/icons
rm -frd ./bootstrap-icons-1.9.1
rm ./bootstrap-icons-1.9.1.zip
