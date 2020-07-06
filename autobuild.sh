#!/bin/sh

echo cleaning old files
rm -rf build

echo generating all pages
chmod +x autobuild.py
./autobuild.py
echo packaging all pages
cd build
zip -r full.zip bit_move_dorm
cd ..

echo packaging size reduced pages
./autobuild.py size
cd build
zip -r size_reduced.zip bit_move_dorm
cd ..

echo packaging image only pages
./autobuild.py img
cd build
zip -r image_only.zip bit_move_dorm
cd ..
