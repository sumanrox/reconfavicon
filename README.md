# reconfavicon - Yet Another Favicon Recon Tool :)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Shell Script](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)](Shell) [![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](Python) 

**reconfavicon** is a Favicon Investigation Toolkit that allows you to analyze and gather information about website favicons.

![Product-Video](./images/product-video.gif)


## Table of Contents

- [About](#about)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Uninstall](#uninstall)
- [License](#license)
- [Contributions](#contributions)
- [Acknowledgements](#acknowledgements)

## About

**reconfavicon** is a powerful tool for investigating website favicons. It helps you extract and analyze favicon data, including MD5 and MMH3 hashes, and allows you to search for these hashes in online databases. Additionally, it provides queries for Shodan and ZoomEye to further investigate websites using these favicons.

### Features
- Extract MD5 and MMH3 hashes of favicons
- Search for favicon hashes in online databases
- Generate queries for Shodan and ZoomEye

## Getting Started

### Prerequisites

To use **reconfavicon**, you need the following prerequisites:

- Python 3
- Python `requests` library
- Python `mmh3` library
- Ruby (for `lolcat`)

### Installation

Follow these steps to install **reconfavicon**:

```bash
# Clone the reconfavicon repository
git clone https://github.com/sumanrox/reconfavicon.git

# Navigate to the project directory
cd reconfavicon

# Run the installation script
sudo ./install_script.sh
```

### Usage
```bash
reconfavicon "https://www.example.com/favicon.ico"
```
### Uninstall
```bash
sudo rm /usr/local/bin/reconfavicon
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributions
Contributions to ***reconfavicon*** are welcome!

### Acknowledgements
Thanks to https://github.com/sansatart for providing a lookup table
