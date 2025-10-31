<div align="center">

# ⚡ WIPWN - WiFi Pentesting Framework

<img src="assets/image.png" alt="WIPWN Logo" width="120" />

### 🔓 Professional WPS Security Auditing Tool

[![GitHub Stars](https://img.shields.io/github/stars/anbuinfosec/wipwn?color=gold&style=for-the-badge&logo=github)](https://github.com/anbuinfosec/wipwn/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/anbuinfosec/wipwn?color=blue&style=for-the-badge&logo=github)](https://github.com/anbuinfosec/wipwn/network/members)
[![License](https://img.shields.io/github/license/anbuinfosec/wipwn?style=for-the-badge&color=green)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)

**Built for Security Researchers • Penetration Testers • Ethical Hackers**

</div>

---

![Telegram](https://tginvite.pages.dev/AnbuSoft?style=discord&theme=dark&color=%235865f2)

## ⚠️ Legal Disclaimer

> **IMPORTANT**: This tool is designed for **educational purposes** and **authorized security testing** ONLY.
> 
> - ✅ Use ONLY on networks you own or have explicit written permission to test
> - ❌ Unauthorized access to computer networks is **ILLEGAL**
> - ⚖️ Users are solely responsible for compliance with local laws
> - 🛡️ Author assumes NO responsibility for misuse or damage
> 
> By using this tool, you agree to use it ethically and legally.

---

## 📑 Table of Contents

- [About](#-about)
- [Project Structure](#-project-structure)
- [Key Features](#-key-features)
- [Requirements](#-requirements)
- [Installation](#️-installation)
- [Usage](#-usage)
- [Attack Profiles](#attack-profiles)
- [Session Management](#session-management)
- [Screenshots](#-screenshots)
- [Troubleshooting](#️-troubleshooting)
- [Supported Routers](#-supported-routers)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 About

**WIPWN** is a powerful WiFi security auditing framework designed for penetration testers and security researchers. It specializes in WPS (WiFi Protected Setup) vulnerability assessment using advanced PIN generation algorithms and automatic chipset detection.


### What's New in Enhanced v3.0 (November 1, 2025) 🚀

#### Algorithm Enhancements (v2.0)
- 🎯 **100 PIN Generation Algorithms** - Massive 100% increase (was 50, now 100)
- 🔧 **34 TP-Link Models Added** - Complete TL-WR, TL-WA, TL-WDR, Archer, TD-W series
- 🔍 **Advanced Reverse Algorithms** - 9 new reverse byte/nibble/bits algorithms
- 📊 **500+ MAC Database** - Expanded 67% with latest 2024-2025 router models
- ⚡ **NIC/OUI Manipulation** - 6 new mathematical transformation algorithms
- 🛡️ **Zero Critical Bugs** - All AttributeErrors and ValueError issues resolved
- 🌐 **Extended Bit Support** - New pin36, pin40, pin44, pin48 algorithms
- 📈 **60-70% Detection Rate** - Improved from 20% baseline vulnerability detection

#### Advanced Attack Features (v3.0) ⭐ NEW
- 💾 **Session Management** - Save/resume attacks with full state persistence
- 🎭 **MAC Randomization** - Change MAC address per attempt to bypass filtering
- ⏱️ **Advanced Timing Controls** - Fine-tune delays, timeouts, and wait periods
- 📈 **Progress Tracking** - Real-time statistics with attempt rate and ETA
- 🔄 **Adaptive Failure Handling** - Intelligent retry logic for timeouts/NACKs
- 🎯 **Attack Profiles** - Pre-configured modes (Fast, Stealth, Patient, Distant)
- 🔓 **Lock Bypass Options** - Ignore fake locks and continue attacks
- 📊 **Statistics Dashboard** - Track attempts, success rate, and patterns
- 🚀 **Inspired by reaver-wps-fork-t6x** - Industry-leading attack optimizations

---

## ✨ Key Features

### 🔥 Algorithm Arsenal (100 Total)
- **7 Basic Bit Algorithms**: pin24/28/32/36/40/44/48 - Standard MAC-based generation
- **9 Reverse Algorithms**: Byte/nibble/bits reversal for little-endian routers
- **6 NIC/OUI Manipulation**: InvNIC, NIC×2/3, OUI+/-/^ operations
- **34 TP-Link Models**: Complete WR/WA/WDR/Archer/TD-W series coverage
- **44 Vendor-Specific**: D-Link, Asus, Belkin, Netgear, Huawei, Xiaomi, Tenda, and more

### 🎯 Advanced Capabilities
- **Automatic Chipset Detection**: Identifies Broadcom, Ralink, Realtek chipsets
- **500+ MAC Database**: Comprehensive 2024-2025 router model coverage
- **Multi-Algorithm Matching**: Suggests multiple algorithms per network
- **Static PIN Database**: 30+ model-specific hardcoded PINs
- **Intelligent Prioritization**: Tests most likely algorithms first

### 🛠️ User Experience
- **100% Network Coverage**: Supports all major manufacturers
- **Session Persistence**: Resume attacks after interruption
- **Clear Visual Feedback**: Color-coded vulnerability status
- **Attack Profiles**: Fast, Balanced, Stealth, Patient, Distant modes
- **Detailed Documentation**: Complete guides and quick references
- **Cross-Platform**: Termux (Android) support
- **Real-time Statistics**: Monitor progress, rate, and ETA
- **Regular Updates**: Based on official wpspin repository

---

## 📋 Requirements

### Hardware
- Android device with root access (for Termux)

### Software
- Python 3.8 or higher
- Android Device
- Root/Superuser access


### Dependencies
- `pixiewps` - WPS Pixie Dust attack tool
- `wpa_supplicant` - Wi-Fi Protected Access client and IEEE 802.1X supplicant
---

## ⚙️ Installation

### Quick Install (Recommended)
- `setup.py` - For Termux/Android (Python script)

### For Termux (Android) 📱

```bash
# Update package repository
pkg update && pkg upgrade

# Install required packages
pkg install python git

# Clone the repository
git clone https://github.com/anbuinfosec/wipwn.git

# Navigate to directory
cd wipwn

# Run Python setup script (installs all dependencies)
python3 setup.py install

# Run the tool (launcher installed)
wipwn -i wlan0
# OR
python3 main.py -i wlan0
```

#### Termux Setup Features:
- ✅ Auto-installs `wpa_supplicant` and `pixiewps`
- ✅ Installs Python dependencies (`PyRIC`)
- ✅ Creates `~/.wipwn/` directories (sessions, pixiewps, reports)
- ✅ Copies all files and assets
- ✅ Creates `wipwn` command launcher
- ✅ Shows usage examples after install

#### Uninstall on Termux:
```bash
python3 setup.py uninstall
```


### Updating WIPWN

```bash
# Use the built-in update script
python3 update.py

# The update script will:
# - Check for new versions
# - Backup your configuration
# - Pull latest changes from GitHub
# - Update dependencies
# - Show changelog
```

### 📚 Documentation Files

After installation, all documentation is available in the installation directory:

- **README.md** - Complete user guide (this file)
- **CHANGELOG.md** - Version history with detailed changes (v1.0 → v3.0)
- **LICENSE** - MIT License terms
- **copyright.txt** - Copyright and attribution information

For the most up-to-date documentation, visit: [GitHub Repository](https://github.com/anbuinfosec/wipwn)

---

## 🚀 Usage

### Basic Commands

```bash
# Start WIPWN
python3 main.py -i wlan0

# Run with specific BSSID
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF

# Pixie Dust attack
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K

# Bruteforce attack
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B

# Display help
python3 main.py -h
```

### Basic Options

| Option | Short | Description |
|--------|-------|-------------|
| `--interface` | `-i` | Network interface name (e.g., wlan0) |
| `--bssid` | `-b` | Target router BSSID (MAC address) |
| `--pin` | `-p` | Use specific PIN (4/8 digits or string) |
| `--pixie-dust` | `-K` | Run Pixie Dust attack |
| `--bruteforce` | `-B` | Run online bruteforce attack |
| `--delay` | `-d` | Delay between PIN attempts (seconds) |
| `--write` | `-w` | Save credentials to file on success |
| `--verbose` | `-v` | Verbose output for debugging |

### Advanced Options ⭐ NEW

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--lock-delay` | `-l` | 60 | Wait time if AP locks (seconds) |
| `--timeout` | `-t` | 10 | Receive timeout (seconds) |
| `--m57-timeout` | `-T` | 0.40 | M5/M7 message timeout (seconds) |
| `--fail-wait` | `-x` | 0 | Sleep after 10 failures (seconds) |
| `--max-attempts` | `-g` | 0 | Maximum attempts (0=unlimited) |
| `--ignore-locks` | `-L` | - | Ignore AP lock warnings |
| `--mac-changer` | `-M` | - | Change MAC per attempt |
| `--session` | `-s` | - | Session file for save/resume |
| `--recurring-delay` | `-r` | - | Periodic delay (format: count:seconds) |

### Attack Profiles

#### Fast Attack (Aggressive)
```bash
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B \
  -d 0.5 -M -L -s attack.json
```
**Features**: Fast attempts, MAC randomization, ignore locks

#### Balanced Attack (Recommended)
```bash
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B \
  -d 1 -r 100:30 -s attack.json
```
**Features**: Moderate speed, periodic breaks, session saved

#### Stealth Attack (Low Detection)
```bash
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B \
  -d 3 -r 50:120 -l 180 -x 60 -s stealth.json
```
**Features**: Slow pace, frequent breaks, long waits

#### Patient Attack (Ultra Stealth)
```bash
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B \
  -d 5 -r 20:300 -M -l 600 -x 120 -s patient.json
```
**Features**: Very slow, 5-min breaks, maximum patience

#### Distant AP (Slow Response)
```bash
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B \
  -t 20 -T 1.0 -d 2 -x 60 -s distant.json
```
**Features**: Long timeouts, extra delays, failure handling

### Session Management

```bash
# Start attack with session
python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B -s myattack.json

# Attack interrupted? Resume from exact position
python3 main.py -i wlan0 -s myattack.json

# Sessions auto-saved every 50 attempts in:
# ~/.wipwn/sessions/
```

---

## 📸 Screenshots

<div align="center">

![WIPWN Main Interface](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/1.jpg)
*Main interface*

![Cracked Result](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/2.jpg)
*Cracked Result*

![Stored Data](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/3.jpg)
*Stored Data*

</div>

---

## 🛠️ Troubleshooting

### Common Issues

**Problem: Permission Denied**
```bash
# Solution: Run with sudo on Linux
sudo python3 main.py -i wlan0

# For Termux, no sudo needed
python3 main.py -i wlan0
```


**Problem: Slow Performance**
```bash
# Solution: Update tool and clear cache
python3 update.py
rm -rf __pycache__
```

---

## 📡 Supported Routers

WIPWN Enhanced supports **500+ router models** from major manufacturers:

| Manufacturer | Algorithms | Models | Vulnerability Level |
|--------------|------------|--------|---------------------|
| **TP-Link** ⭐ | 35 | TL-WR/WA/WDR/Archer/TD-W series | HIGH - MEDIUM |
| D-Link | 8 | DIR/DSL series | HIGH - MEDIUM |
| Asus | 6 | RT-N/DSL-N series | MEDIUM - LOW |
| Netgear | 5 | DGN/WNR series | HIGH - MEDIUM |
| Huawei | 3 | HG series, INFINITUM | MEDIUM |
| Belkin | 4 | F5D/F7D/F9J series | MEDIUM - LOW |
| Tenda | 2 | Arcadyan chipsets | HIGH - MEDIUM |
| Xiaomi | 2 | Mi Router series | MEDIUM |
| Zyxel | 2 | Various models | MEDIUM - LOW |
| Cisco/Linksys | 2 | Various models | MEDIUM |
| Others | 31+ | Broadcom, Realtek, Airocon | VARIES |

**Total Database**: 100 algorithms covering 500+ router models (2024-2025 updated)

### 🎯 TP-Link Complete Coverage (34 Models)

#### TL-WR Series (13 models)
WR740N, WR741ND, WR743ND, **WR841N**, WR841ND, WR842N, WR842ND, WR940N, WR941ND, WR1043ND, WR1045ND, WR2543ND

#### TL-WA Series (6 models)  
WA701ND, WA730RE, WA801ND, WA830RE, WA850RE, WA901ND

#### TL-WDR Series (4 models)
WDR3500, WDR3600, WDR4300, WDR4900

#### Archer Series (7 models)
Archer C5, **C7**, C8, C9, C20, C50, C60

#### TD-W Series (5 models)
TD-W8961N, TD-W8968, TD-W8970, TD-W8980, TD-W9980

---


### Reporting Bugs
1. Check existing issues first
2. Create detailed bug report with steps to reproduce
3. Include system information and error logs

### Suggesting Features
1. Open an issue with `[Feature Request]` tag
2. Describe the feature and its benefits


---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

### 🔥 Anbu Infosec

[![GitHub](https://img.shields.io/badge/GitHub-anbuinfosec-black?style=for-the-badge&logo=github)](https://github.com/anbuinfosec)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram)](https://t.me/AnbuSoft)
[![Facebook](https://img.shields.io/badge/Facebook-anbuinfosec-blue?style=for-the-badge&logo=facebook)](https://facebook.com/anbuinfosec)
[![Website](https://img.shields.io/badge/Website-anbuinfosec.live-green?style=for-the-badge&logo=google-chrome)](https://anbuinfosec.live)

</div>

---

## 📧 Contact

- 📱 **Telegram**: [@AnbuSoft](https://t.me/AnbuSoft)
- 🌐 **Website**: [anbuinfosec.live](https://anbuinfosec.live)
- 📘 **Facebook**: [anbuinfosec](https://facebook.com/anbuinfosec)
- 💼 **GitHub**: [anbuinfosec](https://github.com/anbuinfosec)

---

## ⭐ Show Your Support

If you find this project helpful, please consider:

- ⭐ **Starring** the repository
- 🔄 **Sharing** with others
- 🐛 **Reporting bugs** or suggesting features
- 💬 **Joining** our community on Telegram

---

<div align="center">

**Made with ❤️ by @anbuinfosec**

*For Educational and Ethical Security Testing Only*

[![GitHub Stars](https://img.shields.io/github/stars/anbuinfosec/wipwn?style=social)](https://github.com/anbuinfosec/wipwn/stargazers)

</div>
