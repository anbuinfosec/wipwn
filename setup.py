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
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
reset = "\033[0m"

RED = red
GREEN = green
YELLOW = yellow
RESET = reset

SCRIPT_NAME = 'main.py'
MODULE_NAME = 'wipwn'
BIN_NAME = 'wipwn'

def print_banner():
    banner = f"""{green}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██╗    ██╗██╗██████╗ ██╗    ██╗███╗   ██╗                  ║
║  ██║    ██║██║██╔══██╗██║    ██║████╗  ██║                  ║
║  ██║ █╗ ██║██║██████╔╝██║ █╗ ██║██╔██╗ ██║                  ║
║  ██║███╗██║██║██╔═══╝ ██║███╗██║██║╚██╗██║                  ║
║  ╚███╔███╔╝██║██║     ╚███╔███╔╝██║ ╚████║                  ║
║   ╚══╝╚══╝ ╚═╝╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝                  ║
║                                                              ║
║              WiFi WPS PIN Attack Tool - Setup                ║
║                                                              ║
║  Version: 3.0.0 Enhanced Edition                            ║
║  Author: @anbuinfosec                                        ║
║  Platform: Termux (Android)                                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{reset}"""
    print(banner)

def is_termux():
    return os.getenv("PREFIX", "").startswith("/data/data/com.termux/files/usr")

def print_info(msg):
    print(f"{green}[+]{reset} {msg}")

def print_warn(msg):
    print(f"{yellow}[!]{reset} {msg}")

def print_error(msg):
    print(f"{red}[-]{reset} {msg}")

def install_dependencies():
    """Install required Python packages"""
    print_info("Installing dependencies...")
    
    packages = [
        'wpa_supplicant',
        'pixiewps',
    ]
    
    try:
        # Update package lists
        subprocess.run(['pkg', 'update', '-y'], check=True)
        
        # Install system packages
        for pkg in packages:
            print_info(f"Installing {pkg}...")
            subprocess.run(['pkg', 'install', '-y', pkg], check=True)
        
        # Install Python dependencies
        print_info("Installing Python packages...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'PyRIC'], check=True)
        
        print_info("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print_error(f"Failed to install dependencies: {e}")
        sys.exit(1)

def create_directories():
    """Create necessary directories"""
    dirs = [
        os.path.expanduser('~/.wipwn'),
        os.path.expanduser('~/.wipwn/sessions'),
        os.path.expanduser('~/.wipwn/pixiewps'),
        'reports',
        'store'
    ]
    
    for directory in dirs:
        try:
            os.makedirs(directory, exist_ok=True)
            print_info(f"Created directory: {directory}")
        except Exception as e:
            print_warn(f"Could not create {directory}: {e}")

def install_script():
    if not is_termux():
        print_warn("You don't appear to be running inside Termux. Paths may be incorrect.")
        print_warn("This setup script is designed for Termux on Android.")
        print_warn("For Linux/macOS, use: sudo bash setup.sh")
        sys.exit(1)

    prefix = sys.prefix
    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    python_bin = sys.executable
    
    bin_path = os.path.join(prefix, 'bin', BIN_NAME)
    lib_dir = os.path.join(prefix, 'lib', python_version)
    main_py_path = os.path.join(lib_dir, 'main.py')

    # Dynamic launcher code with correct Python version
    launcher_code = f'''#!{python_bin}
import runpy
import sys
if __name__ == "__main__":
    try:
        runpy.run_path("{main_py_path}", run_name="__main__")
    except Exception as e:
        print(f"Error running wipwn: {{e}}")
        sys.exit(1)
'''

    try:
        # Install dependencies first
        print_info("Step 1: Installing dependencies...")
        install_dependencies()
        
        # Create directories
        print_info("\nStep 2: Creating directories...")
        create_directories()
        
        # Install launcher script
        print_info("\nStep 3: Installing launcher script...")
        with open(bin_path, 'w') as f:
            f.write(launcher_code)
        os.chmod(bin_path, 0o775)
        print_info(f"Launcher script installed at {bin_path}")
        
        # Copy required files
        print_info("\nStep 4: Copying required files...")
        files_to_copy = [
            'main.py',
            'wipwn.py',
            'base.py',
            'vulnwsc.txt',
            'copyright.txt',
            '.flake8',
            'update.py',
            'CHANGELOG.md',
            'LICENSE',
            'README.md'
        ]

        for filename in files_to_copy:
            src_path = filename
            if not os.path.exists(src_path):
                print_warn(f"Source file not found, skipping: {filename}")
                continue
                
            dst_path = os.path.join(lib_dir, filename)
            try:
                with open(src_path, 'r', encoding='utf-8') as src:
                    content = src.read()
                with open(dst_path, 'w', encoding='utf-8') as dst:
                    dst.write(content)
                os.chmod(dst_path, 0o644)
                print_info(f"Copied {filename} to {dst_path}")
            except Exception as e:
                print_warn(f"Failed to copy {filename}: {e}")
        
        # Copy directories
        print_info("\nStep 5: Copying directories...")
        dirs_to_copy = ['assets']
        
        for dirname in dirs_to_copy:
            src_dir = dirname
            dst_dir = os.path.join(lib_dir, dirname)
            
            if not os.path.exists(src_dir):
                print_warn(f"Source directory not found, skipping: {dirname}")
                continue
            
            try:
                import shutil
                if os.path.exists(dst_dir):
                    shutil.rmtree(dst_dir)
                shutil.copytree(src_dir, dst_dir)
                print_info(f"Copied directory {dirname}/ to {dst_dir}/")
            except Exception as e:
                print_warn(f"Failed to copy directory {dirname}: {e}")

        print_info(f"\n{green}╔════════════════════════════════════════════════════════╗{reset}")
        print_info(f"{green}║  Installation completed successfully!                 ║{reset}")
        print_info(f"{green}╚════════════════════════════════════════════════════════╝{reset}")
        print_info(f"\nYou can now run the tool with: {yellow}{BIN_NAME}{reset}")
        print_info(f"Or use: {yellow}python3 main.py{reset}")
        print_info("\nShowing usage:\n")

        subprocess.run([bin_path, '--help'], check=False)
    except Exception as e:
        print_error(f"Installation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

def uninstall_script():
    import shutil
    prefix = sys.prefix
    python_version = f"python{sys.version_info.major}.{sys.version_info.minor}"

    bin_path = os.path.join(prefix, 'bin', BIN_NAME)
    lib_dir = os.path.join(prefix, 'lib', python_version)
    
    files_to_remove = [
        'main.py',
        'wipwn.py',
        'vulnwsc.txt',
        'base.py',
        'copyright.txt',
        '.flake8',
        'update.py',
        'CHANGELOG.md',
        'LICENSE',
        'README.md'
    ]
    
    dirs_to_remove = ['assets']

    print_info("Removing launcher script...")
    try:
        os.remove(bin_path)
        print_info(f"Removed: {bin_path}")
    except FileNotFoundError:
        print_warn(f"Launcher not found, skipping: {bin_path}")
    except Exception as e:
        print_error(f"Error removing launcher: {e}")
    
    print_info("\nRemoving installed files...")
    for filename in files_to_remove:
        path = os.path.join(lib_dir, filename)
        try:
            if os.path.exists(path):
                os.remove(path)
                print_info(f"Removed: {path}")
        except Exception as e:
            print_error(f"Error removing {path}: {e}")
    
    print_info("\nRemoving installed directories...")
    for dirname in dirs_to_remove:
        path = os.path.join(lib_dir, dirname)
        try:
            if os.path.exists(path):
                shutil.rmtree(path)
                print_info(f"Removed directory: {path}")
        except Exception as e:
            print_error(f"Error removing {path}: {e}")
    
    print_info(f"\n{green}Uninstallation completed!{reset}")
    print_warn("Note: User data in ~/.wipwn/ was preserved")
    print_info("To remove completely, run: rm -rf ~/.wipwn")

def main():
    print_banner()
    
    if len(sys.argv) != 2:
        print(f"{yellow}Usage: python3 setup.py [install | uninstall]{reset}\n")
        print(f"{green}Commands:{reset}")
        print(f"  {yellow}install{reset}     - Install wipwn for Termux")
        print(f"  {yellow}uninstall{reset}   - Remove wipwn from Termux\n")
        print(f"{green}Example:{reset}")
        print(f"  python3 setup.py install")
        print(f"  python3 setup.py uninstall\n")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    
    if cmd == 'install':
        print_info("Starting installation for Termux...\n")
        install_script()
    elif cmd == 'uninstall':
        print_info("Starting uninstallation...\n")
        response = input(f"{yellow}Are you sure you want to uninstall? (y/n): {reset}")
        if response.lower() in ['y', 'yes']:
            uninstall_script()
        else:
            print_info("Uninstallation cancelled.")
    else:
        print_error("Unknown command. Use 'install' or 'uninstall'.")
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{yellow}[!] Installation interrupted by user{reset}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)