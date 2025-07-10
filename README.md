<h1 align="center">⚡ WIPWN - WiFi Pentesting Framework</h1>

<p align="center">
  <img src="assets/image.png" alt="WIPWN Logo" width="120" />
</p>

<p align="center">
  <strong>Crack WPS. Audit WiFi. Learn Cybersecurity.</strong><br>
  <i>Built for Termux • Root Required • Ethical Use Only</i>
</p>

<p align="center">
  <a href="https://github.com/anbuinfosec/wipwn/stargazers">
    <img src="https://img.shields.io/github/stars/anbuinfosec/wipwn?color=gold&style=for-the-badge" />
  </a>
  <a href="https://github.com/anbuinfosec/wipwn/network/members">
    <img src="https://img.shields.io/github/forks/anbuinfosec/wipwn?color=blue&style=for-the-badge" />
  </a>
  <a href="https://github.com/anbuinfosec">
    <img src="https://img.shields.io/github/followers/anbuinfosec?label=Follow%20Me&style=for-the-badge&logo=github" />
  </a>
  <a href="https://github.com/anbuinfosec/wipwn/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/anbuinfosec/wipwn?style=for-the-badge&color=green" />
  </a>
</p>

---

> ⚠️ **Disclaimer:**  
> This tool is for **educational and authorized penetration testing** only.  
> Do **NOT** use on unauthorized networks.  
> The author is **not responsible** for any misuse.

---

## ✨ Features

- 🔍 Scan WPS-enabled WiFi networks  
- ⚡ Pixie Dust attack automation  
- 🔓 Online WPS PIN bruteforce  
- 💾 Auto-save cracked PINs and config  
- 🧪 Bash launcher for quick access  
- 🐧 Built for rooted Android + Termux

---

<details>
<summary><strong>📦 Requirements & Packages</strong></summary>

- ✅ Rooted Android device  
- ✅ Termux installed ([Download here](https://termux.com/))  
- ✅ WiFi chipset with monitor mode  
- ✅ Internet connection for setup  

### 📥 Required Termux Packages

| Package | Description | Link |
|---------|-------------|------|
| [`python`](https://wiki.termux.com/wiki/Python) | To run the main script | [Termux Wiki](https://wiki.termux.com/wiki/Python) |
| [`tsu`](https://wiki.termux.com/wiki/Termux-sudo) | Root privileges in Termux | [Termux Wiki](https://wiki.termux.com/wiki/Termux-sudo) |
| [`iw`](https://linux.die.net/man/8/iw) | Wireless device management | [Linux man page](https://linux.die.net/man/8/iw) |
| [`pixiewps`](https://tools.kali.org/wireless-attacks/pixiewps) | Pixie Dust WPS attack tool | [Kali Tools](https://tools.kali.org/wireless-attacks/pixiewps) |
| [`openssl`](https://wiki.termux.com/wiki/OpenSSL) | Crypto operations | [Termux Wiki](https://wiki.termux.com/wiki/OpenSSL) |
| [`wpa_supplicant`](https://wiki.archlinux.org/title/wpa_supplicant) | WiFi authentication | [Arch Wiki](https://wiki.archlinux.org/title/wpa_supplicant) |
| [`git`](https://wiki.termux.com/wiki/Git) | Clone repository | [Termux Wiki](https://wiki.termux.com/wiki/Git) |

</details>

---

## ⚙️ Installation

```bash
pkg update && pkg upgrade -y
pkg install root-repo -y
pkg install git python wpa-supplicant pixiewps iw openssl -y
# Install tsu for root access. If tsu not working, install sudo instead:
pkg install tsu -y || pkg install sudo -y
````

```bash
git clone https://github.com/anbuinfosec/wipwn
cd wipwn
chmod +x main.py
```

---

## 🚀 Usage

| Command                                              | Description                 |
| ---------------------------------------------------- | --------------------------- |
| `sudo python main.py --help`                         | Show help options           |
| `sudo python main.py -i wlan0 -K`                    | Scan and auto attack        |
| `sudo python main.py -i wlan0 -b <BSSID> -K`         | Attack specific BSSID       |
| `sudo python main.py -i wlan0 -b <BSSID> -B -p 1234` | Bruteforce using PIN prefix |
| `bash wipwn.sh`                                      | Use Bash launcher           |

---

## 🛠 Troubleshooting

| Issue                           | Fix                            |
| ------------------------------- | ------------------------------ |
| `Device or resource busy (-16)` | Toggle WiFi ON → OFF and retry |
| No networks found               | Turn on Hotspot + Location     |
| Permission error                | Use `tsu` or `sudo`            |

---

## 🖼️ Screenshots

| Scan                                                                                              | Cracked PIN                                                                                       | Saved Data                                                                                        | Config                                                                                            |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| ![](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/1.jpg) | ![](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/2.jpg) | ![](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/3.jpg) | ![](https://raw.githubusercontent.com/anbuinfosec/anbuinfosec/refs/heads/main/assets/wipwn/4.jpg) |

---

## 🗂️ File Structure

```txt
📁 wipwn/
├── assets/           → Logo and screenshots
├── colors.py         → Terminal color helper
├── config.txt        → Output config format
├── LICENSE           → MIT License
├── main.py           → Main WiFi attack script
├── README.md         → Project documentation
├── vulnwsc.txt       → Vulnerable BSSID database (sample)
└── wipwn.sh          → Bash launcher script
```

---

## 💬 Contact & Support

* 📧 Email: [anbuinfosec@gmail.com](mailto:anbuinfosec@gmail.com)
* 💬 Telegram: [@anbuinfosec](https://t.me/anbuinfosec)
* 💬 Facebook: [@anbuinfosec](https://facebook.com/anbuinfosec)
* 🌐 Website: [https://anbuinfosec.live](https://anbuinfosec.live)
* 🐞 Report issues: [GitHub Issues](https://github.com/anbuinfosec/wipwn/issues)

---

## 💚 Star & Follow

<div align="center" style="text-align: center; margin-top: 20px;">

  <a href="https://github.com/anbuinfosec/wipwn/stargazers" target="_blank">
    <img src="https://reporoster.com/stars/dark/anbuinfosec/wipwn" alt="Stargazers" style="max-width: 100%; height: auto; margin: 10px auto;" />
  </a>

  <a href="https://github.com/anbuinfosec/wipwn/network/members" target="_blank">
    <img src="https://reporoster.com/forks/dark/anbuinfosec/wipwn" alt="Forkers" style="max-width: 100%; height: auto; margin: 10px auto;" />
  </a>

</div>

---

## 📜 License

Licensed under the [MIT License](LICENSE).
You are free to use, modify, and distribute responsibly.

---

## 👤 Author

Made with ❤️ by **Mohammad Alamin**
GitHub: [@anbuinfosec](https://github.com/anbuinfosec)
Email: [anbuinfosec@gmail.com](mailto:anbuinfosec@gmail.com)

---

> 💡 *“Ethical hacking is not a crime — it's knowledge in defense.”*
