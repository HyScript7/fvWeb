#!/bin/bash
# Run this script to download boostrap scss, this is required to run the server without using docker.
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
