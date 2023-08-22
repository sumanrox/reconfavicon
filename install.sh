#!/bin/bash

# Define the name of your script
SCRIPT_NAME="reconfavicon"

# Define the installation directory (where the script will be placed)
INSTALL_DIR="/usr/local/bin"

# Check if the user has root privileges (sudo)
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root using sudo."
    exit 1
fi

# Check if Python3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Installing..."
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Check if Python 'requests' package is installed
if ! python3 -c "import requests" &>/dev/null; then
    echo "Python 'requests' package is not installed. Installing..."
    sudo pip3 install requests
fi

# Check if Python 'mmh3' package is installed
if ! python3 -c "import mmh3" &>/dev/null; then
    echo "Python 'mmh3' package is not installed. Installing..."
    sudo pip3 install mmh3
fi

# Check if 'lolcat' is installed
if ! command -v lolcat &>/dev/null; then
    echo "'lolcat' is not installed. Installing..."
    gem install lolcat
fi

# Copy the script to the installation directory
sudo cp "$SCRIPT_NAME" "$INSTALL_DIR"

# Set executable permissions for the script
sudo chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

echo "Installation complete. You can now use the script by typing:"
echo "$SCRIPT_NAME"
