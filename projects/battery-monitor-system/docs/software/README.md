# Software Documentation

This folder contains software architecture and protocol documentation.

## Contents

### Firmware Components

1. **[Display Prototype](../../firmware/display-prototype/)** - Working voltmeter with calibration
2. **[Screenless Prototype](../../firmware/screenless-prototype/)** - Headless node, work in progress
3. **[Dashboard](../../firmware/dashboard/)** - E-paper display server

### Communication Protocol

The dashboard accepts HTTP GET requests from battery monitor nodes:

```
GET /&voltage=12.5&node=1 HTTP/1.0
```

**Parameters:**
- `voltage` - Battery voltage reading
- `node` - Node identifier (optional)

**Response:**
```json
{"msg":"OK"}
```

### File Structure

Each firmware folder contains:
- `main.py` - Entry point
- Core monitoring/server logic
- Hardware drivers
- Configuration files

### Dependencies

- MicroPython (Raspberry Pi Pico W)
- uasyncio - Async operation
- Custom GUI library (for display firmware)
- E-paper display drivers (for dashboard)
