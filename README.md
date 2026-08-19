# WIPWN

Fast and automated WiFi WPS PIN cracking tool with advanced attack features.

> **⚠️ Note**: WIPWN is optimized for **Termux From F-Droid** on Android. For best results and compatibility, use Termux. Kali/Debian support is legacy.

---

<p align="center">
  <a href="https://wipwn.pro.bd">
    <img src="https://img.shields.io/badge/Documentation-00A8FF?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Documentation">
  </a>
  <span>&nbsp;&nbsp;</span>
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
pkg install tsu -y
git clone https://github.com/anbuinfosec/wipwn
cd wipwn
chmod +x main.py
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

## 7. Session Management

#### Create session
```bash
sudo python3 main.py -i wlan0 -b AA:BB:CC:DD:EE:FF -K -s session1
```

### Resume session
```bash
sudo python3 main.py -i wlan0 --resume-session session1
```
### List sessions
```bash
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
