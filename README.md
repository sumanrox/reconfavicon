# reconfavicon - Advanced Favicon Reconnaissance Tool
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) 

### Languages used
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](Python) 

**reconfavicon** is an advanced Favicon Investigation Toolkit designed to analyze and gather information about website favicons.
###### version - 2024 


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

**reconfavicon** is a powerful tool for investigating website favicons. It extracts and analyzes favicon data, including MD5 and MMH3 hashes. The tool allows searching for these hashes in online databases and provides queries for Shodan and ZoomEye to further investigate websites using these favicons.

### Features
- Extract MD5 and MMH3 hashes of favicons
- Search for favicon hashes in online databases
- Generate queries for Shodan and ZoomEye
- Multiple url support via files, generates mmh3 and md5 hashes for now (no analysis)
- Faster execution via multi-threading

## Getting Started

### Prerequisites

- To use **reconfavicon**, ensure you have the following prerequisites:

```
beautifulsoup4==4.9.3
mmh3==4.1.0
pandas==1.5.3
Requests==2.31.0
termcolor==1.1.0
tqdm==4.64.1
```

### Installation

- One line install command
```bash
curl -sL https://raw.githubusercontent.com/sumanrox/reconfavicon/main/install.sh | sudo bash
```

### Uninstall
- Very simple uninstallation process
```
sudo rm /usr/local/bin/reconfavicon -rf
```


