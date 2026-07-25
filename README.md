# WIPWN - WiFi WPS Penetration Testing Tool

Fast and automated WiFi WPS PIN cracking tool with advanced attack features.

> **⚠️ Note**: WIPWN is optimized for **Termux From F-Dorid** on Android. For best results and compatibility, use Termux. Kali/Debian support is legacy.

---

<p align="center">
  <a href="https://m.me/j/AbbEqWUTxCqdYG8j/?send_source=gc%3Acopy_invite_link_c">
    <img src="https://img.shields.io/badge/Messenger%20Community-0084FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Community">
  </a>
  <span>&nbsp;&nbsp;</span>
  <a href="https://t.me/AnbuSoft">
    <img src="https://img.shields.io/badge/Telegram-@AnbuSoft-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram Channel">
  </a>
</p>

## 📦 Installation

### Prerequisites
- Python 3.8+
- aircrack-ng suite
- wpa_supplicant
- pixiewps
- Termux


### Install (Termux)

```bash
pkg update && pkg upgrade -y
pkg install root-repo -y
pkg install git python wpa-supplicant pixiewps iw openssl -y
pkg install tsu -y || pkg install sudo -y
git clone https://github.com/anbuinfosec/wipwn
cd wipwn
chmod +x main.py
```

---

## 🗑️ Uninstall

```bash

# Remove wipwn
rm -rf /path/to/wipwn
```

```bash

# Remove sessions/data (optional)
rm -rf ~/.Wipwn/
```

---

## 🚀 Basic Commands

### Start WiFi Scanning
```bash
sudo python3 main.py -i wlan0
```

### Pixie Dust Attack
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K
```

### Brute Force Attack
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -B
```

### Dictionary Attack
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF --dictionary-attack --wordlist /path/to/wordlist.txt
```

### With Results Saving
```bash
sudo python3 main.py -i wlan0 -K -w
```

### Auto-add to Vulnerability List
```bash
sudo python3 main.py -i wlan0 -K --auto-vuln-list
```

### Resume Session
```bash
sudo python3 main.py -i wlan0 --resume-session mysession
```

---

## 📋 Command Examples

### 1. Basic Target Attack
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K
```
- `-i wlan0` : WiFi interface
- `-b AA:BB:CC:DD:EE:FF` : Target BSSID
- `-K` : Pixie Dust attack

### 2. Multi-threaded Bruteforce
```bash
sudo python3 main.py -i wlan0 --online-bruteforce --bruteforce-threads 8 --pin-limit 5000
```

### 3. Detect Weak Algorithms
```bash
sudo python3 main.py -i wlan0 --detect-weak-algo
```

### 4. Advanced Reconnaissance
```bash
sudo python3 main.py -i wlan0 --advanced-recon --signal-analysis
```

### 5. Bypass Rate Limiting
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K --detect-rate-limit --bypass-rate-limit
```

### 6. Full Penetration Test
```bash
sudo python3 main.py -i wlan0 \
    -K \
    --advanced-recon \
    --detect-weak-algo \
    --spoof-mac \
    --html-report \
    --auto-vuln-list
```

### 7. Session Management
```bash
# Create session
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K -s session1

# Resume session
sudo python3 main.py -i wlan0 --resume-session session1

# List sessions
sudo python3 main.py --list-sessions
```

### 8. Generate Reports
```bash
sudo python3 main.py -i wlan0 --html-report --detailed-report --report-dir ./reports
```

### 9. Custom PIN Testing
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -p 12345678
```

### 10. Push Button Connect
```bash
sudo python3 main.py -i wlan0 --pbc
```

---

## 🛠️ Common Options

### Attack Options
```bash
-K, --pixie-dust           Pixie Dust attack
-B, --bruteforce           Online bruteforce
-F, --pixie-force          Pixiewps force mode
--pbc                      Push button connect
--pin PIN                  Use specific PIN
--dictionary-attack        Dictionary password attack
```

### Network Options
```bash
-i, --interface            Interface (required)
-b, --bssid               Target BSSID
--session ID              Save/restore session
--channel-hop             Enable channel hopping
--spoof-mac               Spoof MAC address
```

### Detection & Bypass
```bash
--detect-rate-limit       Check for rate limiting
--bypass-rate-limit       Attempt bypass
--detect-weak-algo        Find weak algorithms
--advanced-recon          Network fingerprinting
```

### Results
```bash
-w, --write               Save credentials
--auto-vuln-list          Add to vulnerability list
--html-report             Generate HTML report
--json-output FILE        Save results as JSON
--csv-output FILE         Save results as CSV
```

### Performance
```bash
-t, --timeout SEC         Receive timeout
-d, --delay SEC           Delay between attempts
-l, --lock-delay SEC      Wait after lock
--bruteforce-threads N    Number of threads
```

---

## 📁 Important Files

```
~/.Wipwn/
├── sessions/              # Saved sessions & cracked networks
├── wordlists/             # Dictionary files
└── reports/               # Generated reports

vulnwsc.txt              # Vulnerability list
```

---

## ✅ Output Indicators

- `[+]` = Success
- `[i]` = Information
- `[!]` = Warning
- `[-]` = Error
- `[?]` = Question

---

## 🎨 Network Status Colors

Networks are marked with color indicators during scanning:

- 🟢 **Green** - Possibly vulnerable (WPS enabled, no protection detected)
- 🔴 **Red** - WPS locked (AP is actively blocking WPS attempts)
- 🟡 **Yellow** - Already stored (Network credentials cracked and saved in vulnwsc.txt)
- ⚪ **White** - Maybe vulnerable (WPS unclear, needs further analysis)

---

## 🔧 Troubleshooting

### Interface Not Found
```bash
iwconfig
sudo airmon-ng
```

### Permission Denied
```bash
sudo python3 main.py -i wlan0
```

### Target Not Responding
```bash
sudo python3 main.py -i wlan0 -b BSSID -K -t 20
```

### Rate Limited
```bash
sudo python3 main.py -i wlan0 -b BSSID -K --bypass-rate-limit
```

---

## 🔄 Quick Reference

```bash
# Scan only
sudo python3 main.py -i wlan0

# Quick attack (Pixie Dust + Save)
sudo python3 main.py -i wlan0 -b BSSID -K -w

# Full test with reports
sudo python3 main.py -i wlan0 --advanced-recon --html-report -w

# Bruteforce
sudo python3 main.py -i wlan0 -b BSSID -B --bruteforce-threads 8

# Dictionary attack
sudo python3 main.py -i wlan0 -b BSSID --dictionary-attack --wordlist wordlist.txt
```

---

## 💖 Support / Donations

If you find this project useful, consider supporting its development 🙌

---

## 🪙 Donate

### 🪙 Binance Pay (Recommended)

* **UID:** `1189173734`

---

### ⚡ USDT (TRC20)

```text
0x6b21c1acb94f83b52d1e33bb831527e10133a8e0f705b45cc23a644fa897e24c
```

---

### 🟠 Bitcoin (BTC)

```text
bc1puekadn2dnwc0vyzy0xwl6564geml2kt3ymhvcwvvkdxadpny2l4qy7xxa0
```

---

### 🪶 Litecoin (LTC)

```text
4AjFZj5hqjhTF18SJeDyFXHYaKrimHbjSKJok7MqizN6
```

---

### 📱 bKash (Merchant)

* **Number:** `01615827704`
* **Reference:** `Donation`

---

### 🙏 Thank You

Every contribution helps keep this project alive ❤️

---

## ⚖️ Legal Notice

**This tool is for authorized security testing ONLY.**
- Only test networks you own or have permission to test
- Unauthorized access is illegal
- User assumes all responsibility

---

**OneShot v0.0.2** | Modified by @anbuinfosec
