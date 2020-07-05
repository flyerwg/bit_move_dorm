#!/bin/sh

echo generating index files
chmod +x autogen.py
./autogen.py
echo committing changes
git add .
git commit -m "Index files updated by autogen"
