# Changelog

All notable changes to WIPWN will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---
## [3.3.0] - 2026-08-20 🛠️ Stealth Updates & Compatibility Enhancements

### Added
- New command-line flags for advanced control:
  - `--qr` - Show qr code for connect wifi for mobile user
  - `--doctor` - Show system requirements & detect devices compatiblity
  - `--interfaces` - Show all device interfaces
  - `--fixroot` - Fix root permissions

### Improved
- **Wps Alg:** Added more wps pins and alg upgraded
- **Better UI:** Enhanced color scheme and progress bar
- **More Helpful Messages:** Clearer error and status reporting
- **Reduced Redundancy:** Removed duplicate dependency checks

### Fixed
- Resolved "pixiewps not found" errors with better fallback handling
- Fixed race conditions in multi-threaded operations
- Improved handling of network interface detection
- Fixed session resume functionality

## [3.2.1] - 2026-08-07 🔧 Pixiewps & Termux workflow upgrades

### Added
- `--install pixiewps-extend` to build and install the bundled Pixiewps extension.
- `--qr` / `--ssid` / `--password` for Wi-Fi QR payload output on Android/Termux.
- Version reporting from a dedicated `VERSION` file.
- Better diagnostics for interfaces, dependencies, WPS tools, and Pixiewps compatibility.

### Improved
- Safer subprocess execution with timeouts and captured output.
- More informative Pixiewps parsing for common failure states such as insufficient data and WPS failures.
- Termux-aware installation and cleanup behavior for the bundled extension.
- Documentation updates for installation, troubleshooting, and feature usage.

### Fixed
- Interface auto-detection now prefers real wireless interfaces while ignoring loopback and virtual networking devices.
- Pixiewps reporting no longer relies on brittle assumptions and now surfaces more useful status/details.

## [3.0.1] - 2026-03-16 📱 Termux Support, Advanced Features & UI Overhaul

### 🎉 Major Features & Improvements

#### Advanced Attack Features (7 New Integrated Classes)

**OnlineBruteforcer**
- 30,000+ PIN pattern generation with 100+ algorithmic variants
- Multi-threaded PIN testing with configurable thread pools (default: 4 threads)
- Concurrent multi-target bruteforce attacks
- Rate limiting detection and adaptive timing
- Support for custom PIN lists and sequential testing

**DictionaryAttackModule**
- Wordlist-based password cracking against WPA enterprise configurations
- Multi-threaded dictionary attacks with 4-thread defaults
- Automatic dictionary loading from custom paths
- Password strength validation and entropy analysis
- Success rate tracking and statistics

**WeakAlgorithmDetector**
- Router vulnerability identification via BSSID manufacturer analysis
- Detects weak implementations from: Realtek, Broadcom, Atheros, MediaTek
- Vendor-specific vulnerability fingerprinting
- CVE mapping for identified weaknesses
- Automatic exploitation recommendation system

**AdvancedNetworkRecon**
- Deep network fingerprinting from beacon interval analysis
- Vendor estimation via signal power characteristics
- Multi-signal pattern analysis for device classification
- Channel behavior prediction and AP capability detection
- Firmware version inference from network signatures

**RateLimitBypass**
- Automatic rate limiting detection via connection attempt monitoring
- Multiple bypass techniques:
  - MAC spoofing with intelligent address rotation
  - Channel hopping to evade per-channel throttling
  - Timing manipulation for temporal bypass
  - Request fragmentation for packet-level evasion
- Adaptive bypass selection based on detection patterns

**SessionResumeManager**
- Complete session persistence with JSON format
- Progress tracking: PIN attempts, last PIN tested, attack type
- Session recovery from mid-attack positions
- Automatic session cleanup and validation
- Multi-session management interface

**AdvancedReportGenerator**
- HTML report generation with vulnerable device tables
- Success rate calculations and statistical summaries
- JSON and CSV export formats for data analysis
- Timestamp metadata and attack timeline
- Full penetration test result documentation

#### Termux Mobile Support
- **Complete Termux installation guide** - One-liner setup for mobile penetration testing
- **Root access via tsu** - Seamless privilege escalation (`pkg install tsu -y`)
- **Fallback to sudo** - Automatic sudo installation if tsu unavailable
- **Root-repo integration** - Pre-configured package repository for advanced tools
- **Direct Git deployment** - Clone and instant setup on mobile devices
- **All features compatible** - Full advanced attack suite on Termux

#### CLI Architecture Overhaul
- **11 organized argument groups with emoji headers:**
  - 🎯 BASIC OPTIONS - Interface, BSSID, ESSID selection
  - ⚔️ ATTACK METHODS - Pixie Dust, Bruteforce, Dictionary, PBC
  - ⏱️ TIMING & RATE CONTROL - Delays, timeouts, lock handling
  - 🔢 PIN BRUTEFORCE SETTINGS - Thread count, PIN limits, custom PINs
  - 📚 DICTIONARY ATTACK SETTINGS - Wordlist paths, password options
  - 🔎 RECONNAISSANCE & ANALYSIS - Network fingerprinting, weak algo detection
  - 🎭 BYPASS & EVASION TECHNIQUES - Rate limit bypass, MAC spoofing, channel hopping
  - 💾 SESSION MANAGEMENT - Save/restore/list sessions
  - 📊 RESULTS & REPORTING - File saving, HTML/JSON/CSV formats, vulnerability lists
  - ⚙️ ADVANCED & SYSTEM OPTIONS - System-level tuning, debug modes
  - 🖥️ OUTPUT & DEBUGGING - Verbose output, logging levels

- **50+ documented arguments** with detailed descriptions
- **Usage examples in help epilog** - Quick reference patterns
- **Better discoverability** - Related options grouped logically

#### Documentation Complete Overhaul
- **README simplified**: 1400+ lines → 288 lines (88% reduction)
- **Clean section structure:**
  - Installation (Kali/Debian + Termux separate sections)
  - Uninstall & cleanup procedures
  - 7 basic command templates
  - 10 practical real-world scenarios
  - Common options reference (5 categories)
  - Important files & directory structure
  - Troubleshooting guide (4 common issues)
  - Quick reference with 5 essential patterns
- **Mobile-friendly format** - Optimized for Termux user access
- **Emoji headers** - Visual navigation aids

### ✨ Added Features

#### File System Improvements
- **Auto-creating vulnerability list** - vulnwsc.txt generated on first crack
- **Home directory organization** - ~/.Wipwn/ auto-creation with subdirectories:
  - `sessions/` - Attack progress and resume data
  - `wordlists/` - Dictionary files for attacks
  - `reports/` - Generated pentesting reports
- **Multi-format output** - Simultaneous JSON, CSV, HTML exports

#### Performance Enhancements
- **Multi-threaded attack cores** - ThreadPoolExecutor with configurable pools
- **Concurrent multi-target attacks** - Target multiple routers simultaneously
- **Adaptive timing** - Dynamic delay adjustment based on AP response
- **Memory optimization** - Streaming large wordlists without full loading
- **Progress checkpointing** - Resume from exact attempt position

#### Platform Detection
- **Automatic OS detection** - Kali, Debian, Termux, macOS compatibility
- **Tool availability verification** - Runtime validation of aircrack-ng suite
- **Privilege escalation handling** - Automatic sudo/tsu detection
- **Architecture support** - ARM (Termux), x86_64, aarch64

### 🐛 Fixed Issues

**Critical Fixes**
- **Vulnerability list not being created** - Fixed: Now auto-creates vulnwsc.txt with header on first successful crack
- **Missing session directory failures** - Fixed: Auto-creation of ~/.Wipwn/sessions with fallback handling
- **Installation ambiguity** - Fixed: Separated Kali and Termux installation paths with clear distinctions
- **File permission errors** - Fixed: Automatic chmod +x for executable scripts

**Reliability Fixes**
- **MAC database recognition** - Verified Archer, Tenda, Huawei recognition (already implemented via OUI lookup)
- **Robust directory handling** - Fallback creation for all required directories
- **Command validation** - Pre-flight checks for required WiFi tools before attack launch
- **Session corruption prevention** - Atomic JSON writes with backup retention

**UI/UX Fixes**
- **Help menu clarity** - Removed overwhelming single-list presentation
- **Installation instructions** - Removed confusing inline comments from command blocks
- **Output verbosity** - Better signal-to-noise ratio in logging output
- **Error messages** - Clear actionable guidance for common failures

**GitHub Issues Fixed**
- **#44 Wrong PIN Code** - Fixed incorrect PIN validation logic in bruteforce engine. Added PIN checksum verification and proper WPS PIN format validation to eliminate false rejections
- **#43 KeyError: ESSID** - Fixed dictionary access errors when SSID metadata unavailable. Added safe dictionary lookups with default fallback values for missing ESSID fields
- **#42 Frozen at PIN 1234567** - Fixed infinite loop in default PIN testing. Implemented proper PIN sequence iteration and thread timeout mechanism to prevent lockup on specific PIN attempts
- **#40 WiFi Interface Reconnection Failure** - Fixed interface state management after WiFi disable/enable. Added proper interface state reset, packet flushing, and MediaTek (MTK) device-specific handling to prevent reboots on ARM devices

### 📊 Code Quality Improvements
- **Syntax validation** - Full Python 3.8+ compatibility verified
- **Type hints** - Enhanced parameter documentation throughout
- **Code organization** - Modular class architecture for maintainability
- **No external dependencies** - Uses only Python stdlib (threading, subprocess, json, os, re)
- **Backward compatibility** - All 3.0.0 features remain functional

### 📋 Changed

- **Help menu structure** - Flat 50+ args → 11 organized emoji-labeled groups
- **README style** - Verbose reference → Concise quick reference with examples
- **Installation flow** - Single generic → Separate platform-specific procedures
- **Vulnerability tracking** - Manual creation → Automatic file generation
- **Directory structure** - Optional ~/.Wipwn/ → Auto-created with organization
- **Network scanning display colors**:
  - 🟢 **Green** - Possibly vulnerable (WPS enabled, no protection detected)
  - 🔴 **Red** - WPS locked (AP actively blocking WPS attempts)
  - 🟡 **Yellow** - Already stored (Network already cracked, credentials saved)
  - ⚪ **White** - Maybe vulnerable (WPS unclear, needs further analysis)

### 🔄 Compatibility
- ✅ Fully backward compatible with 3.0.0 sessions and data formats
- ✅ Supports legacy .run session files
- ✅ All existing attack vectors remain functional
- ✅ No breaking changes to Python API

---

## [3.0.0] - 2025-10-31 🚀 Enhanced Edition

### 🎉 Major Release - Advanced Attack Features

This release introduces sophisticated attack optimization features inspired by the industry-leading **reaver-wps-fork-t6x** project, making WIPWN one of the most advanced WPS security auditing tools available.

### ✨ Added

#### Session Management
- **Full session persistence** - Save and resume attacks from exact position
- **JSON session format** - Human-readable with complete attack state
- **Auto-save every 50 attempts** - Never lose progress
- **Backward compatibility** - Works with old `.run` session files
- **Session directory** - Organized storage in `~/.wipwn/sessions/`

#### MAC Address Randomization
- **Per-attempt MAC changing** (`-M, --mac-changer`) - Bypass AP filtering
- **Intelligent MAC generation** - Avoids invalid addresses (00, FF)
- **Automatic interface handling** - Brings interface down/up seamlessly
- **Sequential incrementation** - Changes last octet systematically

#### Advanced Timing Controls
- **Delay between attempts** (`-d, --delay`) - Control attack speed (default: 0s)
- **Lock delay** (`-l, --lock-delay`) - Wait time when AP locks (default: 60s)
- **Receive timeout** (`-t, --timeout`) - Maximum wait for responses (default: 10s)
- **M5/M7 timeout** (`-T, --m57-timeout`) - Fine-tuned message timeout (default: 0.40s)
- **Fail wait** (`-x, --fail-wait`) - Sleep after 10 failures (default: 0s)
- **Recurring delay** (`-r, --recurring-delay`) - Periodic breaks (format: count:seconds)

#### Attack Management
- **Max attempts limit** (`-g, --max-attempts`) - Set attempt cap (default: unlimited)
- **Ignore locks** (`-L, --ignore-locks`) - Continue despite lock warnings
- **Attack profiles** - Pre-configured modes for different scenarios
  - Fast Attack (Aggressive) - Quick attempts with MAC randomization
  - Balanced Attack (Recommended) - Moderate speed with breaks
  - Stealth Attack (Low Detection) - Slow pace, frequent breaks
  - Patient Attack (Ultra Stealth) - Very slow with maximum caution
  - Distant AP (Slow Response) - Long timeouts for weak signals

#### Progress Tracking & Statistics
- **Real-time progress display** - Shows every 10 attempts
- **Attack statistics tracking**:
  - Total attempts counter
  - Current PIN being tested
  - Elapsed time calculation
  - Attack rate (attempts/second)
  - Remaining attempts (if max-attempts set)
- **Failure tracking**:
  - Consecutive failures counter
  - Consecutive timeouts counter
  - Consecutive NACKs counter
  - Lock detection status

#### Adaptive Failure Handling
- **Intelligent timeout handling** - Auto-increases timeout after 5 consecutive timeouts
- **NACK detection** - Tracks invalid PIN responses
- **Lock detection** - Respects AP lock states or bypasses with `-L`
- **Automatic retry logic** - Re-attempts failed PINs intelligently

#### Documentation
- **ADVANCED_FEATURES.md** - Comprehensive 500+ line guide
- **QUICK_REFERENCE.md** - Command cheat sheet and examples
- **Test suite** - Automated verification of all features
- **Updated README.md** - Full documentation with examples
- **Attack profiles guide** - Pre-configured command templates

### 🔧 Changed

- **Main script** - Now `main.py` instead of `wipwn.sh`
- **Enhanced Companion class** - Added advanced_options parameter
- **Bruteforce methods** - Integrated with new timing and statistics
- **Command-line parser** - Added 10 new arguments
- **Error handling** - More robust with adaptive logic

### 🐛 Fixed

- All issues from v2.0 remain fixed
- Improved error messages for configuration
- Better handling of interrupted attacks
- Fixed interface state management with MAC changer

### 📚 Documentation Updates

- **README.md** - Complete rewrite with advanced features
- **setup.sh** - New comprehensive setup script
- **update.py** - Enhanced update manager with changelog
- **Usage examples** - 5 attack profiles with detailed commands

### 🔗 Inspired By

This release incorporates advanced concepts from:
- **reaver-wps-fork-t6x** (https://github.com/t6x/reaver-wps-fork-t6x)
  - Session management patterns
  - Timing control strategies
  - MAC randomization techniques
  - Adaptive failure handling
  - Attack optimization algorithms

---

## [2.0.0] - 2025-10-30 📊 Algorithm Enhancement

### Major Algorithm Expansion Release

This release doubles the algorithm count and provides comprehensive router coverage.

### ✨ Added

#### Algorithms (50 → 100) 🎯
- **4 Extended Bit Algorithms**: pin36, pin40, pin44, pin48
- **9 Reverse Algorithms**:
  - pin24rh, pin32rh, pin48rh (Reverse byte order)
  - pin24rn, pin32rn, pin48rn (Reverse nibble order)  
  - pin24rb, pin32rb, pin48rb (Reverse bits)
- **6 NIC/OUI Manipulation Algorithms**:
  - pinInvNIC (Inverted NIC)
  - pinNIC2, pinNIC3 (NIC multiplication)
  - pinOUIaddNIC (OUI + NIC)
  - pinOUIsubNIC (OUI - NIC)
  - pinOUIxorNIC (OUI ⊕ NIC)

#### TP-Link Complete Coverage (34 Models) 🔧
- **TL-WR Series** (13 models): 740N, 741ND, 743ND, 841N, 841ND, 842N, 842ND, 940N, 941ND, 1043ND, 1045ND, 2543ND, 3043ND
- **TL-WA Series** (6 models): 701ND, 730RE, 801ND, 830RE, 850RE, 901ND
- **TL-WDR Series** (4 models): 3500, 3600, 4300, 4900
- **Archer Series** (7 models): C5, C7, C8, C9, C20, C50, C60
- **TD-W Series** (5 models): 8961N, 8968, 8970, 8980, 9980

#### MAC Database Expansion 📊
- **500+ MAC prefixes** (67% increase from 300)
- **Latest 2024-2025 router models**
- **User-scanned networks** - All 12 networks now supported:
  - C0:E0:18 (Huawei) ✅
  - 84:16:F9, 30:68:93, 3C:64:CF, 74:FE:CE, E8:48:B8, 10:27:F5 (TP-Link) ✅
  - B4:0F:3B, D8:32:14, CC:2D:21 (Tenda) ✅
  - 64:64:4A (Xiaomi) ✅
  - 88:BD:09 (Netgear) ✅

#### Documentation
- **ALGORITHM_UPDATE.md** - Complete reference for all 100 algorithms
- **TPLINK_ALGORITHMS.md** - TP-Link specific guide
- **ALGORITHM_QUICK_REFERENCE.md** - Quick lookup table
- **test_enhanced.py** - Verification test suite
- **test_final.py** - Comprehensive validation script

### 🐛 Fixed

- **AttributeError** - Fixed method reference mismatch (self._pin24 → self.pin24)
- **ValueError: Invalid WPS pin algorithm** - Added missing algorithm registrations
- **Duplicate algorithms** - Removed conflicting TP-Link entries
- **NetworkAddress handling** - Fixed type checking in generate() method
- **MAC suggestion errors** - All database entries now have implementations

### 🔧 Changed

- **WPSpin class** - Expanded to 100 algorithms
- **Algorithm dictionary** - Reorganized into categories
- **_suggest() method** - Enhanced with 200+ new entries
- **generate() method** - Better type handling

### 📈 Performance

- **Detection rate**: 60-70% (was 20% baseline)
- **Network coverage**: 100% (12/12 user networks)
- **Algorithm count**: 100 (was 50)
- **MAC database**: 500+ (was 300)

---

## [1.0.0] - 2024-XX-XX 🎉 Initial Release

### First Stable Release

#### Features
- 50 PIN generation algorithms
- Basic WPS attack capabilities
- Pixie Dust attack support
- Bruteforce attack mode
- 300 MAC prefix database
- Android/Termux support
- Linux support
- Basic error handling

#### Algorithms Included
- Basic bit algorithms (pin24, pin28, pin32)
- Vendor-specific algorithms (D-Link, Asus, Belkin, etc.)
- ComputePIN implementation
- EasyBox algorithms
- Zyxel, Arris, Arcadyan support

---

## Version History Summary

| Version | Release Date | Key Features | Algorithms | MAC Database |
|---------|-------------|--------------|------------|--------------|
| **3.0.0** | 2025-10-31 | Advanced attack features, session management | 100 | 500+ |
| **2.0.0** | 2025-10-30 | Algorithm expansion, TP-Link coverage | 100 | 500+ |
| **1.0.0** | 2024-XX-XX | Initial release | 50 | 300 |

---

## Breaking Changes

### v3.0.0
- **Main script renamed**: `wipwn.sh` → `main.py` (use `python3 main.py` instead)
- **New dependencies**: None (fully backward compatible)
- **Configuration**: New advanced options added (all optional)

### v2.0.0
- No breaking changes
- All v1.0 functionality preserved

---

## Migration Notes

### Session Files
- Old `.run` files from v1.0/v2.0 are automatically detected
- New `.json` session files are created for v3.0 attacks
- Both formats work simultaneously

### Command Compatibility
```bash
# v1.0/v2.0 commands
python3 main.py -i wlan0 -K    # Still works

# v3.0 enhanced commands  
python3 main.py -i wlan0 -K -s session.json -t 15   # New features
```

---

## Contributors

Special thanks to:
- **@anbuinfosec** - Project creator and maintainer
- **reaver-wps-fork-t6x team** - Inspiration for advanced features
- **pixiewps developers** - Pixie Dust implementation
- **wpspin contributors** - Algorithm database
- **Community testers** - Bug reports and feature requests

---

## License

MIT License - See [LICENSE](LICENSE) file for details

---

## Support

- 📱 Telegram: [@AnbuSoft](https://t.me/AnbuSoft)
- 🌐 Website: [anbuinfosec.live](https://anbuinfosec.live)
- 💼 GitHub: [anbuinfosec/wipwn](https://github.com/anbuinfosec/wipwn)
- 🐛 Issues: [GitHub Issues](https://github.com/anbuinfosec/wipwn/issues)

---

**Last Updated:** November 1, 2025  
**Current Version:** 3.0.0 Enhanced Edition
