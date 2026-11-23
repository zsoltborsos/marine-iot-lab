# NeoPixel Display System

A web-based visual programming tool for creating NeoPixel LED matrix patterns, plus a collection of NeoPixel lighting effects.

## Overview

This project consists of two components:

1. **NeoServer Web Interface** - Design LED patterns visually in your browser
2. **NeoPixel Firmware** - MicroPython code to run the patterns on your hardware

## How It Works

1. Open the web interface in your browser
2. Click on grid cells to select LEDs (20×11 matrix = 220 LEDs)
3. Use RGB sliders to choose colors
4. Click "Generate neopixel list" to get MicroPython code
5. Copy the generated code to your Pico and run it

```
┌─────────────────┐     Generated      ┌──────────────────┐
│   NeoServer     │  ───────────────►  │  MicroPython     │
│  Web Interface  │    Python code     │  Firmware        │
│  (Browser)      │                    │  (Pico + LEDs)   │
└─────────────────┘                    └──────────────────┘
```

## Project Structure

```
NeoPixelDisplay/
├── README.md              # This file
├── firmware/              # MicroPython code
│   ├── neopixel1.py       # Basic strip control
│   ├── colors.py          # Color testing
│   ├── falling.py         # Falling light effect
│   ├── randomstrip1.py    # Random patterns
│   ├── randomstrip2.py
│   ├── warm1.py           # Warm lighting
│   ├── infra.py           # IR receiver control
│   ├── infrarcv.py        # IR decoder
│   ├── tester1.py         # Testing utility
│   ├── xmas.py            # Christmas effects
│   └── [more effects...]
├── web-interface/         # NeoServer web app
│   ├── app.js             # Express backend
│   ├── routes/
│   ├── views/
│   │   └── index.ejs      # Vue.js pixel editor
│   └── public/
│       ├── stylesheets/
│       └── javascripts/
└── hardware/              # Hardware documentation
    └── setup.md
```

## Hardware Setup

### NeoPixel Matrix
- **Total LEDs**: 220 (20 rows × 11 columns)
- **Data pin**: GPIO 4
- **Layout**: Serpentine pattern (alternating direction rows)
- **Power**: Appropriate for 220 NeoPixels (consider 5V, high current)

### IR Remote Control (Optional)
- **IR Receiver**: GPIO 14
- **Protocol**: NEC (decoded by `infrarcv.py`)

### Wiring
```
Pico          NeoPixel
────          ────────
GPIO 4   ──►  Data In
5V (VBUS) ──►  +5V
GND      ──►  GND
```

**Note**: For 220 LEDs, use external 5V power supply with common ground.

## Firmware Usage

### Basic Strip Control (`neopixel1.py`)
```python
from machine import Pin
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 300)  # Adjust count for your setup
np[0] = (100, 100, 100)  # RGB color
np.write()
```

### Using Generated Code
Copy the output from the web interface:
```python
from machine import Pin
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 300)

# Paste generated code here
np[0] = (25, 10, 5)
np[1] = (30, 15, 8)
# ... etc

np.write()
```

### IR Remote Control
```python
from infrarcv import infraGetCMD

rec = infraGetCMD(14)  # GPIO 14
while True:
    irValue = rec.ir_read()
    if irValue:
        print(irValue)  # Process IR command
```

## Web Interface

### Running NeoServer

```bash
cd web-interface
npm install
npm start
```

Then open: `http://localhost:3000`

### Features

- **Visual Grid Editor**: 20×11 pixel matrix
- **RGB Color Picker**: Sliders for precise colors
- **Serpentine Mapping**: Accounts for alternating row directions
- **Code Generation**: Outputs ready-to-use MicroPython code
- **Bootstrap UI**: Responsive design

### Interface Layout

1. **Color Picker Section**
   - RGB value displays
   - Three sliders (Red, Green, Blue)
   - Live color preview

2. **Pixel Grid**
   - 20 rows × 11 columns
   - Click to select/deselect pixels
   - Selected pixels show current color

3. **Code Output**
   - Generated MicroPython code
   - Copy-paste ready format

## Effects Library

The `firmware/` folder includes various lighting effects:

| File | Effect |
|------|--------|
| `colors.py` | Solid color testing |
| `falling.py` | Falling light animation |
| `warm1.py` | Warm yellow lighting |
| `randomstrip1.py` | Random LED patterns |
| `randomstrip2.py` | Alternative random patterns |
| `xmas.py` | Christmas lighting effects |
| `infra.py` | IR remote control demo |

## Customization

### Changing LED Count
Edit the `strip` variable in firmware files:
```python
strip = 300  # Change to your LED count
```

### Changing Data Pin
```python
pin = Pin(4, Pin.OUT)  # Change GPIO number
```

### Web Interface Grid Size
Modify in `web-interface/views/index.ejs`:
```javascript
// Change rows/cols in the template
<div v-for="row in 20">  <!-- Change row count -->
  <my-pixel v-for="col in 11">  <!-- Change column count -->
```

## Applications

- **Signage**: Custom LED text/pattern displays
- **Art Installations**: Programmable light art
- **Holiday Decorations**: Seasonal lighting effects
- **Ambient Lighting**: Mood lighting with patterns
- **Prototyping**: Quick visual pattern testing

## Tips

1. **Power**: NeoPixels draw significant current - use adequate power supply
2. **Capacitor**: Add 1000μF capacitor across power/ground near LEDs
3. **Resistor**: 330-470Ω resistor on data line reduces noise
4. **Ground**: Always connect Pico GND to LED strip GND
5. **Testing**: Start with few LEDs before scaling up

## Troubleshooting

**Issue**: LEDs not lighting up
- Check power connections (5V, GND)
- Verify data pin matches code
- Ensure common ground between Pico and LEDs

**Issue**: Wrong colors
- NeoPixel types differ (WS2812 vs SK6812)
- Check color order (RGB vs GRB)

**Issue**: Flickering/unstable
- Add capacitor across power rails
- Check power supply capacity
- Add resistor on data line

## Related Projects

- Battery Monitor System - Voltage monitoring with display
- E-Paper Display - Low-power display alternative
