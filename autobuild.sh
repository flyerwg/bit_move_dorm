#!/bin/sh

echo "input version string: (e.g. 1_0_2)"
read verstr

echo cleaning old files
rm -rf build

echo generating all pages
chmod +x autobuild.py
./autobuild.py
echo packaging all pages
cd build
zip -r bit_move_dorm_${verstr}_full.zip bit_move_dorm
cd ..

echo packaging size reduced pages
./autobuild.py size
cd build
zip -r bit_move_dorm_${verstr}_size_reduced.zip bit_move_dorm
cd ..

echo packaging image only pages
./autobuild.py img
cd build
zip -r bit_move_dorm_${verstr}_image_only.zip bit_move_dorm
cd ..
