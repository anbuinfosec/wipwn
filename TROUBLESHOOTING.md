# Troubleshooting

## No wireless interface detected

Use `python3 main.py --interfaces` or `python3 main.py --doctor` to inspect your environment.

If your adapter is not recognized:

- verify the adapter is present and not disabled,
- confirm you are running on a supported Linux environment,
- check whether the adapter requires a different driver or firmware,
- on Android/Termux, confirm the environment is capable of exposing wireless tools.

## Missing dependencies

Run:

```bash
python3 main.py --dependencies
```

Install the missing tools for your platform following the instructions in [INSTALL.md](INSTALL.md).

## Pixiewps issues

Use:

```bash
python3 main.py --pixiewps-info
```

The diagnostic will report whether the binary is present, which version was found, and whether the build appears compatible.

If the bundled extension should be built locally, use:

```bash
python3 main.py --install pixiewps-extend
```

## Termux

Termux-specific behavior is reported by:

```bash
python3 main.py --doctor
```

The tool will report platform, architecture, Termux status, root availability, PATH, and required binaries without attempting to run remote fix scripts.

## QR output

If you want to generate a Wi-Fi QR payload for Android/Termux-assisted connection, run:

```bash
python3 main.py --qr --ssid "MyWiFi" --password "secret"
```

## Debug output

For verbose diagnostics, use:

```bash
python3 main.py --debug --doctor
```
