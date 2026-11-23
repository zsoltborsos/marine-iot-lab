# Battery Monitor System

A distributed battery monitoring system for marine environments, built with Raspberry Pi Pico W and MicroPython.

## Overview

This project is designed to monitor battery voltage at several points on a boat and show the readings on a central e-paper dashboard. Today the display prototype works as a standalone voltmeter; the nodes do not yet send readings to the dashboard.

## System Architecture (planned)

```
┌─────────────────────┐
│ BatteryMonitor 1    │ ──┐
│ (Alternator)        │   │
└─────────────────────┘   │
                          │      ┌─────────────────────┐
┌─────────────────────┐   │      │  E-Paper Dashboard  │
│ BatteryMonitor 2    │ ──┼─────►│  (WiFi AP + Display)│
│ (Fridge)            │   │      │                     │
└─────────────────────┘   │      └─────────────────────┘
                          │
┌─────────────────────┐   │
│ BatteryMonitor 3    │ ──┘
│ (Solar)             │
└─────────────────────┘
```

## Project Structure

```
BatteryMonitorSystem/
├── README.md                    # This file
├── CONFIG.md                    # Configuration guide
├── docs/
│   ├── hardware/                # Hardware documentation
│   │   ├── README.md
│   │   ├── voltage-sentinel-components.txt
│   │   └── voltage-sentinel-circuit.png
│   └── software/                # Software documentation
│       └── README.md
├── firmware/
│   ├── display-prototype/       # Working standalone voltmeter
│   │   ├── README.md
│   │   └── (source code)
│   ├── screenless-prototype/    # Headless node, work in progress
│   │   ├── README.md
│   │   └── (source code)
│   └── dashboard/               # E-paper display and HTTP server prototype
│       ├── README.md
│       └── (source code)
└── hardware/
    └── voltage-sentinel/        # Circuit design files
        ├── README.md
        ├── components.txt
        └── circuit.png
```

## Components

### Display Prototype

**Status**: ✅ Built and working

A standalone battery voltmeter with LCD display and button controls for calibration. It was built to tune the voltage divider and works as a voltmeter on its own.

**Features:**
- Real-time voltage display
- Button calibration controls
- Offset and multiplier adjustment

**Firmware**: [`firmware/display-prototype/`](firmware/display-prototype/)

---

### Screenless Prototype

**Status**: 🚧 Hardware built; firmware is work in progress

Minimal "headless" design for distributed deployment at multiple monitoring points. The firmware is derived from the display prototype: it sets up the ADC inputs but does not yet run a monitoring loop or send readings.

**Design goals:**
- Voltage monitoring (ADC)
- Minimal power consumption
- No display, no buttons, no LEDs

**Planned deployments:**
- Alternator output
- Fridge battery
- Solar panel input/output

**Firmware**: [`firmware/screenless-prototype/`](firmware/screenless-prototype/)

---

### E-Paper Dashboard

**Status**: 🚧 Prototype: receives and shows messages; no node sends readings yet

Central display unit, planned to show readings from all battery monitor nodes. Today it runs a Wi-Fi access point and an HTTP server, saves the query parameters of an incoming request, and shows them on the e-paper display.

**Features:**
- WiFi Access Point mode
- HTTP server that accepts messages
- 3.7" e-paper display (low power)
- Partial refresh support

**Firmware**: [`firmware/dashboard/`](firmware/dashboard/)

---

### Voltage Sentinel Circuit

Custom voltage regulator and divider design.

**Specifications:**
- Input: 8-16V (marine battery range)
- Output: 5V (Pico power) + divided voltage (ADC)
- L7805 regulator
- Calibration-friendly design

**Hardware**: [`hardware/voltage-sentinel/`](hardware/voltage-sentinel/)

## How It Works

The planned flow (steps 1 and 2 are not implemented yet):

1. **BatteryMonitor nodes** periodically read battery voltage via ADC
2. **WiFi transmission** sends readings to the dashboard
3. **Dashboard** receives data and updates e-paper display (works today for messages sent by hand)
4. **Refresh rate**: ~20 seconds (suitable for battery monitoring)

## Current Status

### Completed ✅

- [x] Voltage Sentinel circuit designed and built
- [x] Display prototype firmware (working standalone voltmeter)
- [x] Screenless prototype hardware built
- [x] Dashboard prototype: HTTP server that shows received messages on e-paper
- [x] WiFi AP infrastructure

### In Progress 🚧

- [ ] Screenless node monitoring loop
- [ ] WiFi client integration for battery monitors
- [ ] Dashboard multi-node data handling

### Future Enhancements 💡

- [ ] Bluetooth alternative to WiFi
- [ ] Deep sleep for battery monitors
- [ ] Historical data logging
- [ ] Voltage alert system

## Documentation

- **[Hardware Docs](docs/hardware/)** - Circuit diagrams and component lists
- **[Software Docs](docs/software/)** - Protocol and architecture
- **[Configuration Guide](CONFIG.md)** - How to configure WiFi credentials

## Related Projects

- [Exhaust Temperature Monitor](../exhaust-temperature-monitor/) - Another marine monitoring design
- [Utilities](../../utilities/) - Shared MicroPython modules
