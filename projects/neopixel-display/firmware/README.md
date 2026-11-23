# NeoPixel Firmware

MicroPython code for controlling NeoPixel LED strips and matrices.

## Quick Start

```python
from machine import Pin
from neopixel import NeoPixel

# Setup
pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 300)  # Adjust LED count

# Set a pixel
np[0] = (100, 100, 100)  # RGB (0-255)
np.write()
```

## Files

### Core Effects

| File | Description |
|------|-------------|
| `neopixel1.py` | Basic strip control with gradient effect |
| `colors.py` | Solid color testing (warm yellow, white) |
| `falling.py` | Falling light animation |
| `warm1.py` | Warm yellow ambient lighting |

### Random Patterns

| File | Description |
|------|-------------|
| `randomstrip1.py` | Random LED positions with gradient |
| `randomstrip2.py` | Alternative random pattern |

### IR Remote Control

| File | Description |
|------|-------------|
| `infra.py` | Main IR receiver loop |
| `infrarcv.py` | IR command decoder module |

### Seasonal

| File | Description |
|------|-------------|
| `xmas.py` | Christmas lighting effects |
| `tester1.py` | Testing utility |

### Subfolders

- **`1/`** - Alternative versions of main effects
- **`xmas/`** - Christmas-specific effects
  - `tree_aio.py` - Christmas tree animation
  - `xmas.py` - Holiday patterns
  - `tester1.py` - Holiday light tester

## Usage

### Running an Effect

1. Copy the desired `.py` file to your Pico
2. Adjust LED count if needed (`strip = 300`)
3. Run the file

Example:
```bash
# On Pico
import neopixel1  # or whichever effect
```

### Using with Web Interface

1. Open NeoServer web interface
2. Design your pattern
3. Click "Generate neopixel list"
4. Copy the output
5. Paste into a new Python file:

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

## Customization

### Change LED Count
```python
strip = 300  # Change to your LED count
```

### Change Data Pin
```python
pin = Pin(4, Pin.OUT)  # Change GPIO number
```

### Adjust Brightness
Modify RGB values (0-255):
```python
# Dim (20% brightness)
np[i] = (20, 20, 20)

# Medium (50% brightness)
np[i] = (127, 127, 127)

# Full brightness
np[i] = (255, 255, 255)
```

## IR Remote Control

### Setup
```python
from infrarcv import infraGetCMD

rec = infraGetCMD(14)  # GPIO 14
```

### Reading Commands
```python
while True:
    irValue = rec.ir_read()
    if irValue:
        print(irValue)  # Process IR command
        # Add your logic here
```

### Changing Effects via IR
Modify `infra.py` to switch between effects based on button presses.

## Color Reference

### Warm Yellow (from `colors.py`)
```python
np[i] = (80, 50, 4)    # Warm yellow
np[i] = (26, 16, 2)    # Dimmer warm yellow
```

### White Variations
```python
np[i] = (100, 100, 100)  # Neutral white
np[i] = (50, 50, 50)     # Dim white
```

### RGB Values
```python
np[i] = (255, 0, 0)    # Red
np[i] = (0, 255, 0)    # Green
np[i] = (0, 0, 255)    # Blue
np[i] = (255, 255, 0)  # Yellow
np[i] = (0, 255, 255)  # Cyan
np[i] = (255, 0, 255)  # Magenta
```

## Tips

1. **Start Small**: Test with few LEDs before running full strip
2. **Power Off**: Always disconnect power before modifying wiring
3. **Current Limiting**: Use appropriate power supply for LED count
4. **Capacitor**: Add 1000μF across power/GND for stability
5. **Resistor**: 330-470Ω on data line reduces noise

## Troubleshooting

**Issue**: Effect doesn't run
- Check LED count matches your hardware
- Verify GPIO pin number
- Ensure power is connected

**Issue**: Wrong colors
- WS2812B uses GRB order, some use RGB
- Adjust color values accordingly

**Issue**: Flickering
- Add capacitor across power rails
- Check power supply capacity
- Verify ground connections

## Related Documentation

- [Main README](../README.md) - Project overview
- [Hardware Setup](../hardware/setup.md) - Wiring and setup
- [Web Interface](../web-interface/) - Visual pattern designer
