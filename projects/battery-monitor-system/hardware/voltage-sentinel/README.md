# Hardware Documentation

## Voltage Sentinel

The voltage regulator and divider circuit designed for battery monitoring.

### Files

- **`components.txt`** - Component list and specifications
- **`circuit.png`** - Circuit diagram

### Description

The Voltage Sentinel is a custom circuit that:

1. **Regulates** 8-16V input down to 5V for the Pico
2. **Divides** the battery voltage to ADC-safe levels (0.7V-1.6V range)

### Components

**Voltage Regulator (L7805):**
- L7805 5V voltage regulator IC
- IN5819 1A Schottky diode
- Capacitors: 0.47uF, 100nF, 10uF (see schematic)

**Voltage Divider:**
- 2.2K + 6.8K resistors (equivalent to 9K)
- 1K resistor
- Variable resistor for fine-tuning

### Input/Output

- **Input**: 8-16V (marine battery range)
- **Output 1**: +5V (for Pico power)
- **Output 2**: 0.7V-1.6V divided voltage (for ADC measurement)

### Calibration Notes

The voltage divider requires calibration at multiple points:
- Different correction factors at 10V, 12V, and 14V
- Software correction compensates for non-linearity
- Use the display prototype for real-time calibration

### See Also

- [Display Prototype Firmware](../../firmware/display-prototype/) - Used for calibration
- [Screenless Prototype Firmware](../../firmware/screenless-prototype/) - Headless node, work in progress
