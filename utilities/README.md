# MicroPython Utilities

Reusable utility modules for MicroPython projects on Raspberry Pi Pico and similar boards.

## Overview

This is a collection of **general-purpose utility modules** that can be used across multiple MicroPython projects. Each module provides specific functionality that's commonly needed in embedded projects.

## Available Utilities

### **buttons/** - Button Input Handling

Button and switch input utilities with debouncing and event handling.

**Features**:
- Software debouncing
- Event-driven callbacks
- Multiple button support
- Long-press detection

---

### **displays/** - Display Utilities

General display utilities for SPI and other display interfaces.

**Files**:
- `spitest.py` - SPI display test patterns
- `spi2.py` - SPI communication helpers
- `clearscreen.py` - Screen clearing utilities

---

### **image-tools/** - Image Conversion Tools

Tools for converting images for MicroPython display projects.

**Tools**:
- `imgtobitmap.py` - Convert images to Python bitmap modules

**Based on**: [st7789_mpy by russhughes](https://github.com/russhughes/st7789_mpy) - This is a very useful tool that I found and use for image conversion.

**Usage**:
```bash
python imgtobitmap.py image.jpg 1 > output.py
```

---

### **sdcard/** - SD Card Interfaces

SD card mounting and file system utilities.

**Features**:
- SPI SD card interface
- FAT filesystem mounting
- File read/write examples

---

### **spi-debug/** - SPI Debugging Tools

Logic analyzer and debugging utilities for SPI development.

**Contents**:
- `spi debug1` - Sigrok/logic analyzer commands
- Debug procedures for SPI troubleshooting

**Use Cases**:
- SPI bus debugging
- Protocol analysis
- Timing verification

---

### **uart/** - UART Communication

UART serial communication utilities.

**Files**:
- `myuart.py` - UART wrapper class
- `readuart.py` - UART reading examples
- `uart-test.py` - UART testing utilities

---

### **wifi/** - WiFi Connectivity

WiFi connection and access point utilities for Pico W.

**Features**:
- Station mode (connect to AP)
- Access Point mode
- Connection status handling
- Network utilities

**⚠️ Security Note**: All WiFi credentials have been removed from these files. Replace placeholders with your actual credentials:

```python
# In wifi.py or accesspoint.py
ssid = '<your_ssid>'       # Change this
password = '<your_password>'  # Change this
```

---

## Project Structure

```
Utilities/
├── README.md              # This file
├── buttons/
│   └── buttons.py         # Button handling
├── displays/
│   ├── clearscreen.py     # Screen utilities
│   ├── spi2.py            # SPI helpers
│   └── spitest.py         # Test patterns
├── image-tools/
│   ├── README.md          # Usage guide
│   └── imgtobitmap.py     # Image converter
├── sdcard/
│   ├── mountsd.py         # SD card mounting
│   ├── mysd.py            # SD card wrapper
│   ├── mysd_new.py        # Alternative version
│   └── sdcard.py          # SD card driver
├── spi-debug/
│   ├── README.md          # Debug guide
│   └── spi debug1         # Analyzer commands
├── uart/
│   ├── myuart.py          # UART wrapper
│   ├── readuart.py        # UART reader
│   └── uart-test.py       # Test utility
└── wifi/
    ├── accesspoint.py     # AP mode
    ├── mywifi.py          # Station mode
    └── wifi.py            # WiFi utilities
```

---

## Usage Examples

### Button Handling

```python
from buttons import Buttons

buttons = Buttons()

async def on_button_press(value):
    print(f"Button {value} pressed")

await buttons.start()
```

---

### WiFi Station Mode

```python
from mywifi import connect_wifi

# Edit mywifi.py with your credentials first!
connect_wifi()
```

---

### SD Card Mounting

```python
from mysd import mySd

sd = mySd()
# SD card mounted at /sd

# Read a file
with open('/sd/data.txt', 'r') as f:
    data = f.read()
```

---

### UART Communication

```python
from myuart import myUart

uart = myUart()
uart.send("Hello via UART!")
```

---

### Image Conversion

```bash
# Convert image to 1-bit bitmap
python imgtobitmap.py photo.jpg 1 > photo.py

# Convert with more colors
python imgtobitmap.py photo.jpg 4 > photo_16color.py
```

---

## Integration with Projects

These utilities are used by:

- **BatteryMonitorSystem** - WiFi, buttons, displays
- **EPaperPhotoAlbum** - SD card, UART
- **NeoPixelDisplay** - General utilities
- **LCDDisplays** - Display utilities
- **ExhaustTemperatureMonitor** - UART, displays (planned)

---

## Adding Your Own Utilities

To add a new utility module:

1. Create a folder with the utility name
2. Add your Python modules
3. Include a README.md with usage examples
4. Update this main README

---

## Credits

### External Sources

- **imgtobitmap.py**: Based on [st7789_mpy by russhughes](https://github.com/russhughes/st7789_mpy) - a very useful image converter tool
- **Async/Event handling**: Uses [micropython-async by peterhinch](https://github.com/peterhinch/micropython-async) - excellent async utilities for MicroPython
- **Display drivers**: Uses code from peterhinch's display libraries

---

## License

MIT License - see the main repository [LICENSE](../LICENSE).

**Note**: Some utility modules come from other projects under their own licences: `sdcard/sdcard.py` (micropython-lib, MIT), `image-tools/imgtobitmap.py` (st7789_mpy, MIT) and the Waveshare-based display test in `displays/`. See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
