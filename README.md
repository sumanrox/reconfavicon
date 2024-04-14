![Banner](./images/carbon.svg)
# reconfavicon - Advanced Favicon Reconnaissance Tool
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) 

##### Languages used
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](Python) 

**reconfavicon** is an advanced Favicon Investigation Toolkit designed to analyze and gather information about website favicons.
[![asciicast](https://asciinema.org/a/630811.svg)](https://asciinema.org/a/630811)
###### version - 2024

## Table of Contents

- [About](#😎-about)
- [Features](#💯-features)
- [Getting Started](#getting-started)
  - [Installation](#🚀-installation)
  - [Caution](#⚠️-caution)
- [Usage](#📡-usage)
- [Uninstall](#🚧-uninstall)
- [License](#🪪-license)
- [Contributing](#🏗️-contributing)

## 😎 About

**reconfavicon** is a powerful tool for investigating website favicons. It extracts and analyzes favicon data, including MD5 and MMH3 hashes. The tool allows searching for these hashes in online databases and provides queries for Shodan and ZoomEye to further investigate websites using these favicons.

## 💯 Features
#### 🚀 🥵 Extract MD5 and MMH3 hashes of favicons
#### 🔥 👀 Search for favicon hashes in online databases
#### 🔐 🔑 Generate queries for Shodan and ZoomEye
#### 🥳 🎊 Multiple url support via files, generates mmh3 and md5 hashes for now (no analysis)
#### 🎉 🚀 Faster execution via multi-threading

## Getting Started


### 🚀 Installation

- ##### One line install command
```bash
curl -sL https://raw.githubusercontent.com/sumanrox/reconfavicon/main/install.sh | sudo bash
```
- ##### Or you can manually download the project repo and run the program
```bash
git clone https://github.com/sumanrox/reconfavicon.git
cd reconfavicon
python reconfavicon.py --url https://example.com
```
- ##### Make an alias ( zsh | bashrc )
```bash
# Create alias in ~/.zshrc or inside ~/.bashrc
alias reconfavicon="python3 /opt/reconfavicon/reconfavicon.py"
# Or if you have downloaded in a different path
alias reconfavicon="python3 /path/to_project/reconfavicon/reconfavicon.py"
```
- ##### Source it
```bash
source ~/.zshrc
# Or
source ~/.bashrc
```
### ⚠️ Caution
- The auto installer makes ```/var/opt/reconfavicon/shared``` folder writeable for everyone
- You may want to take the ownership rather than giving it root privileges
- ##### Remedy
```bash
sudo chown -R $(whoami) /opt/reconfavicon
chmod 700 /opt/reconfavicon/shared
```

### 📡 Usage
- ##### For doing recon on single target
```bash
reconfavicon -u https://example.com
```
- ##### For doing recon on multiple targets, (Generates a CSV File)
```bash
reconfavicon -f urls.txt
```
### Available Arguments

- `-h, --help`: show this help message and exit
- `--url URL, -u URL`: Server URL or IP, eg: http://example.com
- `--port PORT, -p PORT`: Server Port, eg: 8080
- `--no-banner, -n`: Prevents the Banner from loading
- `--file URLLISTS, -f URLLISTS`: File containing list of urls, fetches only hashes, will ignore other switches
- `--threads THREADS, -t THREADS`: Used with -f switch, will ignore other switches (Default 20 Threads)
- `--update, -up`: Update Lookup Table
- `--hash`: Capture All IP addresses associated with an organisation's favicon hash
- `--output FILENAME, -o FILENAME`: Filename for saving results
- `--apiKey API_KEY`: Shodan API Key or Environment Variable containing Shodan API Key (required)


### 🚧 Uninstall
- Very simple uninstallation process
```
sudo rm /usr/local/bin/reconfavicon -rf
```
- Remove the alias from bashrc
```
alias reconfavicon="python3 /usr/local/bin/reconfavicon/reconfavicon.py"
```
### 🏗️ Contributing
Contributions are welcome! If you have any improvements or suggestions, feel free to open an issue or create a pull request.

### 🪪 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### Made with ❤️ by Suman Roy
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sumanrox/)

