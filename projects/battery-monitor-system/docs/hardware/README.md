# Hardware Documentation

This folder contains hardware design files for the Battery Monitor System.

## Contents

### Voltage Sentinel

The voltage regulator and divider circuit designed for battery monitoring.

**Files:**
- [`voltage-sentinel/`](../../hardware/voltage-sentinel/) - Complete hardware design
  - `components.txt` - Component list
  - `circuit.png` - Circuit diagram
  - `README.md` - Documentation

## Prototypes Built

Two hardware prototypes have been built and tested:

1. **Display Prototype** - With LCD and buttons for calibration
2. **Screenless Prototype** - Minimal design for distributed deployment

Both use the same Voltage Sentinel circuit for voltage regulation and division.
