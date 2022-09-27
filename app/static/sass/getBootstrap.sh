#!/bin/bash
# Run this script to download boostrap scss, this is required to run the server without using docker.
wget https://github.com/twbs/bootstrap/archive/v5.0.2.zip
unzip ./v5.0.2.zip
mkdir bootstrap
mv ./bootstrap-5.0.2/scss ./bootstrap/scss
rm -frd ./bootstrap-5.0.2
rm ./v5.0.2.zip
