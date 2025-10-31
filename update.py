#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WIPWN Update Script
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

# Colors
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
reset = "\033[0m"

def print_banner():
    print(f"{cyan}")
    print("╦ ╦╦╔═╗╦ ╦╔╗╔")
    print("║║║║╠═╝║║║║║║")
    print("╚╩╝╩╩  ╚╩╝╝╚╝")
    print("Update Manager v3.0")
    print(f"{reset}")

def print_info(msg):
    print(f"{green}[+]{reset} {msg}")

def print_warn(msg):
    print(f"{yellow}[!]{reset} {msg}")

def print_error(msg):
    print(f"{red}[-]{reset} {msg}")

def print_status(msg):
    print(f"{blue}[i]{reset} {msg}")

def is_termux():
    return os.getenv("PREFIX", "").startswith("/data/data/com.termux/files/usr")

def check_git_repo():
    """Check if current directory is a git repository"""
    if not os.path.isdir('.git'):
        print_error("This directory is not a Git repository (missing .git folder).")
        print_status("Clone the repository: git clone https://github.com/anbuinfosec/wipwn.git")
        sys.exit(1)

def get_current_version():
    """Get current git commit info"""
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--pretty=format:%h - %s (%cr)'],
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True
        )
        return result.stdout.strip()
    except:
        return "Unknown"

def check_for_updates():
    """Check if updates are available"""
    print_status("Checking for updates...")
    try:
        subprocess.run(['git', 'fetch'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD..origin/main'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        commits_behind = int(result.stdout.strip())
        return commits_behind
    except:
        return 0

def show_changelog():
    """Show recent commits"""
    print_status("Recent changes:")
    try:
        result = subprocess.run(
            ['git', 'log', '--oneline', '--decorate', '-5'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"{cyan}{result.stdout}{reset}")
    except:
        pass

def backup_config():
    """Backup user configuration files"""
    print_status("Backing up configuration...")
    config_files = [
        'store/wipwn_crack_data.txt',
        '.wipwn/sessions/',
    ]
    backed_up = []
    
    for path in config_files:
        if os.path.exists(path):
            backup_path = f"{path}.backup"
            try:
                if os.path.isfile(path):
                    import shutil
                    shutil.copy2(path, backup_path)
                    backed_up.append(path)
            except:
                pass
    
    if backed_up:
        print_info(f"Backed up {len(backed_up)} file(s)")
    return backed_up

def pull_updates():
    """Pull latest changes from repository"""
    print_info("Pulling latest changes from Git repository...")
    try:
        result = subprocess.run(
            ['git', 'pull', 'origin', 'main'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Git pull failed:\n{e.stderr}")
        return False

def update_dependencies():
    """Update Python dependencies"""
    print_status("Updating Python dependencies...")
    if os.path.exists('requirements.txt'):
        try:
            subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '--upgrade', '-r', 'requirements.txt'],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print_info("Dependencies updated")
            return True
        except:
            print_warn("Failed to update dependencies")
            return False
    return True

def show_whats_new():
    """Display what's new in latest version"""
    print(f"\n{cyan}{'='*60}{reset}")
    print(f"{cyan}What's New in WIPWN v3.0 Enhanced Edition{reset}")
    print(f"{cyan}{'='*60}{reset}\n")
    
    features = [
        ("🎯", "100 PIN Generation Algorithms", "(doubled from 50)"),
        ("💾", "Session Management", "Save/resume attacks"),
        ("🎭", "MAC Randomization", "Bypass AP filtering"),
        ("⏱️", "Advanced Timing Controls", "Fine-tune delays"),
        ("📈", "Progress Tracking", "Real-time statistics"),
        ("🔄", "Adaptive Failure Handling", "Intelligent retry logic"),
        ("🎯", "Attack Profiles", "Fast/Stealth/Patient modes"),
        ("📊", "Statistics Dashboard", "Track attempts & rate"),
        ("🔧", "34 TP-Link Models", "Complete coverage"),
        ("🌐", "500+ MAC Database", "2024-2025 routers"),
    ]
    
    for emoji, feature, desc in features:
        print(f"  {emoji} {green}{feature}{reset} - {desc}")
    
    print(f"\n{cyan}{'='*60}{reset}\n")

def main():
    print_banner()
    
    # Check if running in git repo
    check_git_repo()
    
    # Show current version
    current = get_current_version()
    print_status(f"Current version: {current}")
    print()
    
    # Check for updates
    commits_behind = check_for_updates()
    
    if commits_behind > 0:
        print_info(f"Updates available: {commits_behind} new commit(s)")
        show_changelog()
        
        # Ask for confirmation
        response = input(f"\n{yellow}[?]{reset} Update now? [Y/n]: ")
        if response.lower() in ['n', 'no']:
            print_status("Update cancelled")
            sys.exit(0)
        
        # Backup configuration
        backed_up = backup_config()
        
        # Pull updates
        if pull_updates():
            print_info("Update completed successfully!")
            
            # Update dependencies
            update_dependencies()
            
            # Show what's new
            show_whats_new()
            
            # Show new version
            new_version = get_current_version()
            print_info(f"Updated to: {new_version}")
            
            # Restore backed up files
            if backed_up:
                print_status("Your data files were preserved")
            
            print()
            print_info("Restart the tool to use the new features:")
            print(f"  {cyan}python3 main.py -i wlan0{reset}")
            print()
        else:
            print_error("Update failed. Your installation is unchanged.")
            sys.exit(1)
    else:
        print_info("You are already up to date!")
        print()
        show_whats_new()
        print_status("Run the tool: python3 main.py -i wlan0")
        print()

if __name__ == '__main__':
    main()
