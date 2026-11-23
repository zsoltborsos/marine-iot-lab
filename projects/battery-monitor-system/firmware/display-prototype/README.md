# Display Prototype Firmware

**Status**: ✅ Built and working

**Hardware**: Raspberry Pi Pico W + LCD display + buttons + voltage divider

**Description**: This is the firmware for the display-equipped prototype. It was built to tune the voltage divider correction factors and also works as a standalone battery voltmeter.

## Features

- Real-time battery voltage monitoring
- LCD display output
- Button controls for calibration (offset/multiplier adjustment)
- Async operation with uasyncio

## Main Files

- `main.py` - Entry point
- `batterymonitor.py` - Main monitoring logic
- `adcmonitor.py` - ADC reading with calibration
- `display.py` - LCD display handler
- `buttons.py` - Button input handling
- `color_setup.py` - Display configuration

## Usage

Run `main.py` to start monitoring. Use the buttons to:
- **+** - Increase calibration multiplier
- **-** - Decrease calibration multiplier
- **Start** - Begin monitoring
- **Stop** - Pause monitoring

## Hardware Connections

- ADC input: GPIO 26
- Reference input: GPIO 27
- Display: SPI interface (see `color_setup.py`)
- Buttons: GPIO 15, 17, 2, 3, 19

## Notes

This prototype demonstrated the voltage divider tuning challenge - different correction factors are needed at different voltage levels (10V vs 12V vs 14V).
