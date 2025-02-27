#!/bin/bash

./build.sh

# Create the directory
mkdir -p output/mediaremote

# Copy the files
cp -R ./src requirements.txt run.sh install.sh setup_venv.sh output/mediaremote/

# Zip the directory
cd output
zip -rq mediaremote.zip mediaremote/*

# Remove the directory
rm -rf mediaremote

cd ..