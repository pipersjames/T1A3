#!/bin/bash

# navigate to shell script directory
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"
# check if python is installed or not
# install it if not

# check if pip install or not
# install it if not

# create a virtual environment 
python3 -m venv venv

# activate
source venv/bin/activate
python3 --version

# install packages
pip install tabulate

# run python file
python3 main.py

# deactivate
deactivate

#remove virtual environment
rm -rf venv








