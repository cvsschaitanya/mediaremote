#!/bin/bash

base_dir=$(dirname $0)

./build.sh

"$base_dir/venv/bin/python" "$base_dir/src/server/app.py"
