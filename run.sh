#!/bin/bash

base_dir=$(dirname $0)
"$base_dir/venv/bin/python" "$base_dir/src/server/server.py"
