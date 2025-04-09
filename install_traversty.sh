#!/bin/bash

# Installer script for Traversty tool

echo "[*] Installing Traversty..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
  echo "[!] Please run as root (use sudo)"
  exit
fi

# Install required Python modules
echo "[*] Installing required Python modules..."
pip3 install requests --quiet

# Copy the script to /usr/local/bin
echo "[*] Copying traversty to /usr/local/bin..."
cp traversty.py /usr/local/bin/traversty

# Make it executable
chmod +x /usr/local/bin/traversty

echo "[+] Installation complete!"
echo "[+] Now you can run the tool by typing: traversty"
