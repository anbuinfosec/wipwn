# Installation

## Termux

On Android/Termux, install the available packages:

```bash
pkg update
pkg install -y python git iw iproute2 make clang
```

If the project should build the bundled Pixiewps extension, use:

```bash
python3 main.py --install pixiewps-extend
```

The installer builds the bundled binary, installs it into the appropriate user bin directory, and removes the temporary source tree on Termux after a successful install.

## Running from source

```bash
cd /path/to/wipwn
python3 main.py --help
```

## Diagnostics before use

```bash
python3 main.py --doctor
python3 main.py --dependencies
python3 main.py --interfaces
python3 main.py --pixiewps-info
```

## Dependencies

The project checks for the following tools when present:

- `python`
- `iw`
- `ip`
- `pixiewps`
- ~~aircrack-ng~~
- ~~reaver~~
- ~~wash~~
- ~~bully~~

Missing tools are reported without attempting to install them automatically.
