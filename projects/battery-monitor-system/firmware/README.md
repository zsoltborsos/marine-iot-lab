# Battery Monitor System - Firmware

This folder contains all firmware for the Battery Monitor System projects.

## Firmware Versions

### 1. Display Prototype

**Location:** [`display-prototype/`](display-prototype/)

**Status:** ✅ Built and working

A standalone battery voltmeter with LCD display and button controls for calibration. It was built to tune the voltage divider and works as a voltmeter on its own.

**Features:**
- Real-time voltage display
- Button calibration controls
- Offset and multiplier adjustment
- LCD display

**[→ View Display Prototype Firmware](display-prototype/)**

---

### 2. Screenless Prototype

**Location:** [`screenless-prototype/`](screenless-prototype/)

**Status:** 🚧 Hardware built; firmware is work in progress (no monitoring loop or Wi-Fi sending yet)

Minimal "headless" design for distributed deployment at multiple monitoring points.

**Features:**
- Voltage monitoring (ADC)
- Minimal power consumption
- No display, no buttons, no LEDs
- WiFi transmission (to be implemented)

**Planned deployments:**
- Alternator output
- Fridge battery
- Solar panel input/output

**[→ View Screenless Prototype Firmware](screenless-prototype/)**

---

### 3. Dashboard (E-Paper Server)

**Location:** [`dashboard/`](dashboard/)

**Status:** 🚧 Prototype: receives and shows messages; no node sends readings yet

Central display unit, planned to show readings from all battery monitor nodes. Today it shows the message from an incoming HTTP request.

**Features:**
- WiFi Access Point mode
- HTTP server that accepts messages
- 3.7" e-paper display (low power)
- Partial refresh support
- Web interface for configuration

**[→ View Dashboard Firmware](dashboard/)**

---

## Calibration

The voltage divider requires calibration at multiple points:

1. **Display Prototype** - Used for initial calibration
   - Real-time adjustment of offset and multiplier
   - Visual feedback on LCD
   - Button controls for fine-tuning

2. **Software Correction**
   - Different correction factors at 10V, 12V, and 14V
   - Stored in `config.py` or `config_local.py`
   - See individual firmware READMEs for details

---

## Common Libraries

All firmware versions use shared libraries:

- **NanoGUI** - Display GUI framework (peterhinch)
- **micropython-async** - Async utilities (peterhinch)
- **Display drivers** - ePaper and LCD drivers

See individual folders for specific dependencies.

---

## Getting Started

1. **Choose your firmware version:**
   - Display Prototype - For bench testing and calibration
   - Screenless Prototype - For permanent installation
   - Dashboard - For central monitoring

2. **Install MicroPython** on your Pico

3. **Copy firmware files** to your Pico

4. **Configure WiFi credentials** in the appropriate config file

5. **Calibrate** using the display prototype

See the [Hardware Build Guide](../hardware/voltage-sentinel/BUILD_GUIDE.md) for complete setup instructions.

---

## Troubleshooting

### Display Issues
- Check SPI wiring
- Verify display driver matches your hardware
- See display-specific README

### WiFi Issues
- Check credentials in config file
- Verify Pico W model for WiFi capability
- See dashboard README for AP mode setup

### ADC Reading Issues
- Check voltage divider wiring
- Verify calibration values
- See screenless prototype README

---

## License

MIT License - See main repository LICENSE file

**Note:** This firmware includes code from peterhinch's micropython-async and NanoGUI libraries (MIT License) and a Waveshare e-paper driver. See [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md) and the individual source files.
