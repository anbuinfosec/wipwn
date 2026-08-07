# WIPWN - WiFi WPS Penetration Testing Tool 🎯

Fast and automated WiFi WPS PIN cracking tool with advanced attack features.

> **⚠️ Note**: WIPWN is optimized for **Termux From F-Droid** on Android. For best results and compatibility, use Termux. Kali/Debian support is legacy.

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

## 🚀 Features

### Core Capabilities
- **Advanced WPS Scanning:** Features a managed mode WPS scanner that does not strictly require monitor mode to find vulnerable APs.
- **Smart Interface Selection:** Automatically detects and selects the best wireless interface if `-i` or `--interface` is not provided.
- **Cross-Platform Diagnostics:** Native environment checks (`--doctor`, `--dependencies`, `--interfaces`) tailored for Linux and Android (Termux).

### Attack Methods
- **Pixie Dust Attack:** Exploits low entropy in some APs' PRNG (`-K`, `--pixie-dust`).
- **Pixie Force:** Runs Pixiewps with forced full-range bruteforcing (`-F`, `--pixie-force`).
- **Online Bruteforce:** Traditional WPS PIN bruteforce (`-B`, `--bruteforce`).
- **Dictionary Attack:** Fast password testing using a custom or default wordlist (`--dictionary-attack`).
- **Push Button Connect (PBC):** WPS push button connection simulation (`--pbc`).

### Reconnaissance & Intelligence
- **Vulnerability Checks:** Automatically detects weak WPS algorithms and compares targets against a known vulnerable devices database.
- **Signal Analysis:** Evaluates signal strength and patterns for better attack targeting.
- **Rate Limit Detection:** Proactively checks if the target AP implements rate-limiting.

### Evasion & Bypasses
- **MAC Spoofing:** Randomize MAC address on every attempt or use a custom MAC (`--spoof-mac`, `--custom-mac`).
- **Rate Limit Bypass:** Intelligent delays, sleep on failure, and channel hopping to evade detection and locks (`--bypass-rate-limit`, `--channel-hop`).
- **Ignore Locks:** Optionally continue attacking even when the AP announces a WPS lock (`-L`).

---

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

# Remove sessions/data (optional)
rm -rf ~/.Wipwn/
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
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF --online-bruteforce --bruteforce-threads 8 --pin-limit 5000
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

### 10. QR Code Output
```bash
sudo python3 main.py --qr --ssid "TargetWiFi" --password "CrackedSecret123"
```

---

## 🛠️ Common Options

### Attack Options
```bash
-K, --pixie-dust           Pixie Dust attack
-B, --bruteforce           Online bruteforce
-F, --pixie-force          Pixiewps force mode
--pbc                      Push button connect
-p, --pin PIN              Use specific PIN
--dictionary-attack        Dictionary password attack
```

### Network Options
```bash
-i, --interface            Interface (required)
-b, --bssid               Target BSSID
-s, --session ID          Save/restore session
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

### 💳 Donation Methods

<div align="center">
  <table>
    <tr>
      <td align="center"><b>💵 USDT (BEP20)</b></td>
      <td align="center"><b>📱 bKash</b></td>
      <td align="center"><b>💎 GRAM (TON)</b></td>
    </tr>
    <tr>
      <td align="center"><img src="./assets/donate/usdt.png" width="250" height="250" alt="USDT BEP20 QR"></td>
      <td align="center"><img src="assets/donate/bkash.png" width="250" height="250" alt="bKash QR"></td>
      <td align="center"><img src="assets/donate/gram.png" width="250" height="250" alt="GRAM TON QR"></td>
    </tr>
    <tr>
      <td align="center"><code>0x3ad5146f733ff16e2251<br>f5da45aeb06438f7bd48</code></td>
      <td align="center"><code>01615827704</code></td>
      <td align="center"><code>UQD4EaT4BWECPqZT16kt<br>BgfLY7oS0N_mBdVaKxms<br>t3tOOEQw</code></td>
    </tr>
    <tr>
      <td align="center">BNB Smart Chain</td>
      <td align="center">BanglaQr</td>
      <td align="center">The Open Network</td>
    </tr>
  </table>
</div>

---

## ⚖️ Legal Notice

**This tool is for authorized security testing ONLY.**
- Only test networks you own or have permission to test
- Unauthorized access is illegal
- User assumes all responsibility

---

**OneShot v0.0.2** | Modified by @anbuinfosec
