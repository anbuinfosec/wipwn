#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: @anbuinfosec
GitHub: https://github.com/anbuinfosec/wipwn
License: MIT License
Disclaimer:
    This tool is for educational and authorized penetration testing only.  
    Do NOT use on unauthorized networks.  
    The author is not responsible for any misuse.
"""

import os
import sys
import subprocess
import colors

def print_info(msg):
    print(f"{colors.green}[+]{colors.reset} {msg}")

def print_warn(msg):
    print(f"{colors.yellow}[!]{colors.reset} {msg}")

def print_error(msg):
    print(f"{colors.red}[-]{colors.reset} {msg}")

def is_termux():
    return os.getenv("PREFIX", "").startswith("/data/data/com.termux/files/usr")

def main():
    if not is_termux():
        print_warn("You don't appear to be running inside Termux. Proceeding anyway.")

    if not os.path.isdir('.git'):
        print_error("This directory is not a Git repository (missing .git folder).")
        sys.exit(1)

    print_info("Pulling latest changes from Git repository...")
    try:
        result = subprocess.run(['git', 'pull'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        print_info("Update completed successfully.")
    except subprocess.CalledProcessError as e:
        print_error(f"Git pull failed:\n{e.stderr}")
        sys.exit(1)

if __name__ == '__main__':
    main()
