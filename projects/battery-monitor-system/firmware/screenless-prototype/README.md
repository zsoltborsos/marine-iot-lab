# Screenless Prototype Firmware

**Status**: 🚧 Work in progress

**Hardware**: Raspberry Pi Pico W + voltage divider only (no display, no buttons, no LEDs)

**Description**: This is the minimal firmware for the "headless" BatteryMonitor nodes designed for distributed deployment around the boat.

## Features

- Battery voltage monitoring (ADC readings)
- Minimal power consumption (no display, no LEDs)
- Designed for periodic sleep/wake operation
- Ready for WiFi client integration

## Main Files

- `main.py` - Entry point
- `batterymonitor.py` - Monitoring logic (no display code)
- `adcmonitor.py` - ADC reading with calibration
- `color_setup.py` - Configuration (display stubs retained)

## Current Limitations

This version is derived from the display prototype with the display and buttons disabled. It sets up the ADC inputs but does not yet:
- Run a monitoring loop on start-up
- Send data via WiFi to the dashboard
- Enter deep sleep between readings

These features are planned for the next iteration.

## Hardware Connections

- ADC input: GPIO 26
- Reference input: GPIO 27

## Deployment Locations (Planned)

- Alternator output
- Fridge battery
- Solar panel input
- Solar panel output

## Next Steps

1. Integrate WiFi client code to send readings to dashboard
2. Implement periodic sleep/wake cycle
3. Optimize for minimal standby power consumption
