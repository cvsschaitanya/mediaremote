#!/bin/bash
script_path=$(dirname "${BASH_SOURCE[0]}")
venv_path="$script_path/venv"

rm -rf $venv_path 

virtualenv $venv_path 

. "$venv_path/bin/activate"

pip install -r "$script_path/requirements.txt"

