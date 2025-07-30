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
  <a href="https://github.com/anbuinfosec/wipwn">
    <img src="https://img.shields.io/github/repo-size/anbuinfosec/wipwn?style=for-the-badge&color=informational" alt="Repo Size" />
  </a>
  <a href="https://github.com/anbuinfosec/wipwn/commits/main">
    <img src="https://img.shields.io/github/last-commit/anbuinfosec/wipwn?style=for-the-badge&color=success" alt="Last Commit" />
  </a>
  <a href="https://t.me/anbuinfosec_official">
    <img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" />
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
- ✅ Termux installed ([Download here](https://f-droid.org/en/packages/com.termux/))  
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

## ⚙️ Setup & Update

### Setup (Install launcher script)

After cloning and entering the repo folder, run:

```bash
python3 setup.py install
```

This will create a convenient launcher script `wipwn` in your Termux `~/../usr/bin/` directory, so you can run the tool by simply typing:

```bash
wipwn --help
```

---

### Uninstall launcher script

If you want to uninstall the launcher script:

```bash
python3 setup.py uninstall
```

---

### Update WIPWN to the latest version

To update your local repository to the latest commit from GitHub, use:

```bash
python3 update.py
```

Make sure you are inside the `wipwn` directory when running the update script.

---

### Notes

* Running the setup script requires root access in Termux.
* Ensure `git` is installed to use the update script.

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
├── setup.py          → Install/uninstall launcher script
├── update.py         → Git update helper script
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

## 📜 License

Licensed under the [MIT License](LICENSE).
You are free to use, modify, and distribute responsibly.

---

## 👤 Author

Made with ❤️ by **Mohammad Alamin**

Facebook: [@anbuinfosec](https://facebook.com/anbuinfosec)

GitHub: [@anbuinfosec](https://github.com/anbuinfosec)

Email: [anbuinfosec@gmail.com](mailto:anbuinfosec@gmail.com)

---

> 💡 *“Ethical hacking is not a crime — it's knowledge in defense.”*