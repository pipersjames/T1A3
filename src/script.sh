#!/bin/bash

# navigate to shell script directory
SCRIPT_DIR=$(dirname "$0")
cd "$SCRIPT_DIR"
# check if python is installed or not

# Check if Python 3 is already installed
if command -v python3 &>/dev/null; then
    echo "Python 3 is already installed."
else
    echo "Python 3 is not found. Installing Python 3..."

    # Install Python 3 using package manager
    if command -v apt-get &>/dev/null; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install python3
    elif command -v yum &>/dev/null; then
        # CentOS/RHEL
        sudo yum update
        sudo yum install python3
    elif command -v brew &>/dev/null; then
        # macOS (Homebrew)
        brew update
        brew install python3
    else
        echo "Unable to install Python 3. Please install it manually."
        exit 1
    fi

    echo "Python 3 installation completed."
fi

# Check if pip3 is already installed
if command -v pip3 &>/dev/null; then
    echo "pip3 is already installed."
else
    echo "pip3 is not found. Installing pip3..."

    # Download get-pip.py
    curl -O https://bootstrap.pypa.io/get-pip.py

    # Install pip3
    python3 get-pip.py

    # Remove get-pip.py
    rm get-pip.py

    echo "pip3 installation completed."
fi


# install virtual environment pip
if command -v virtualenv &>/dev/null; then
    echo "virtualenv is already installed."
else
    echo "virtualenv is not found. Installing virtualenv..."

    pip3 install virtualenv

    echo "virtualenv installation completed."

fi

#create virtual environment
python3 -m venv venv

# activate
source venv/bin/activate

# install pip
pip3 install tabulate

# run python file
clear
python3 main.py


# deactivate
deactivate

#remove virtual environment
rm -rf venv