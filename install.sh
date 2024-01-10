#!/bin/bash

# Define the name of your script
SCRIPT_NAME="reconfavicon"

# Define the installation directory (where the script will be placed)
INSTALL_DIR="/opt/$SCRIPT_NAME"

# Check if the user has root privileges (sudo)
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root using sudo."
    exit 1
fi

# Check if Git is installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed. Installing..."
    apt-get update
    apt-get install -y git
fi

# Clone the repository
git clone https://github.com/sumanrox/reconfavicon "$INSTALL_DIR"

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Installing..."
    apt-get update
    apt-get install -y python3
fi

# Install required Python packages
pip3 install -r "$INSTALL_DIR/requirements.txt"

# make it executable
chmod +x "$INSTALL_DIR/reconfavicon.py"
chmod -x "$INSTALL_DIR/shared"
chmod +w "$INSTALL_DIR/shared"

echo "Installation complete"
