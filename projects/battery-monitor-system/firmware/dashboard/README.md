# E-Paper Dashboard Firmware

**Status**: 🚧 Prototype: shows messages received over HTTP; no node sends readings yet

**Hardware**: Raspberry Pi Pico W + 3.7" e-paper display

**Description**: This firmware runs the central dashboard, planned to display battery readings from all monitoring nodes. It operates as a WiFi Access Point and HTTP server, and shows the query parameters of each incoming request on the e-paper display.

## Features

- WiFi Access Point mode
- HTTP server on port 80
- E-paper display (low power, marine-suitable)
- Message display from incoming HTTP requests
- Planned: voltage data from BatteryMonitor nodes

## Main Files

- `dashboard.py` - Main application with display and server tasks
- `accesspoint.py` - WiFi AP configuration
- `server_own.py` - HTTP server for client connections
- `filehandler.py` - File-based message storage
- `Pico-ePaper-3.7.py` - E-paper display driver
- `drivers/` - Display driver dependencies
- `gui/` - GUI widget library

## Communication Protocol

The dashboard accepts HTTP GET requests:

```
GET /&voltage=12.5&node=1 HTTP/1.0
```

Parameters are saved to `message.txt` and displayed on the e-paper screen.

## Network Configuration

- **SSID**: `MyPiCoW`
- **Password**: (see `accesspoint.py`)
- **IP**: Assigned by AP (see serial output)

## Display Features

- Partial refresh support (5 refreshes before full clear)
- Debug display showing IP, memory, refresh counter
- Message display area for incoming data
- Power-saving sleep mode between updates

## Known Issues

- Pico W AP may timeout after 5-10 minutes (MicroPython limitation)
- Requires investigation with newer MicroPython versions

## Future Enhancements

1. Robust multi-node data handling
2. Historical data logging
3. Alert system for voltage anomalies
4. Bluetooth alternative to WiFi
