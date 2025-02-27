#!/bin/bash

base_dir=$(dirname $0)

pushd $base_dir

"$base_dir/venv/bin/python" "$base_dir/src/main.py" > /tmp/mediaremote.log 

popd