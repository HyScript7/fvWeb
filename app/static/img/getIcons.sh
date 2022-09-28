#!/bin/bash
# Run this script to download boostrap icons, this is required to run the server without using docker.
wget https://github.com/twbs/icons/releases/download/v1.9.1/bootstrap-icons-1.9.1.zip
unzip ./bootstrap-icons-1.9.1.zip
mkdir icons
mv ./bootstrap-icons-1.9.1/* ./icons
mv ./icons/fonts ./
rm -frd ./bootstrap-icons-1.9.1
rm ./bootstrap-icons-1.9.1.zip
