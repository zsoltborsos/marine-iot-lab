# Exhaust Temperature Monitor - Firmware

Firmware sketch for the exhaust temperature monitor design. It has not been run on hardware; treat it as untested.

## Files

- **`max31855.py`** - MAX31855 thermocouple amplifier driver
- **`checktemp.py`** - Main temperature reading script

## Usage

### Basic Temperature Reading

The MAX31855 is SPI-only and read-only (CLK, CS, DO; no MOSI). The driver takes an SPI bus and a chip-select pin, as in `checktemp.py`:

```python
from machine import Pin, SPI
from max31855 import MAX31855
import time

# Wiring: GP2 -> CLK, GP4 -> DO (MISO), GP5 -> CS
spi = SPI(0, baudrate=5_000_000, polarity=0, phase=0, sck=Pin(2), miso=Pin(4))
cs = Pin(5, Pin.OUT)

# Create sensor instance
maxi = MAX31855(spi, cs)

# Main loop
while True:
    try:
        temp = maxi.read_celsius()
        print("Exhaust Temperature: %s °C" % temp)
        
        # Alarm thresholds
        if temp and temp > 400:
            print("WARNING: High exhaust temperature!")
        if temp and temp > 500:
            print("CRITICAL: Shut down engine!")
        
        time.sleep(1)
    except Exception as e:
        print("Sensor error:", e)
        time.sleep(1)
```

`read_celsius()` returns `None` when the chip reports a thermocouple fault.

## Temperature Thresholds

**Typical Diesel Engine Exhaust:**
- **Normal:** 200-400°C
- **Warning:** 400-500°C
- **Critical:** >500°C
- **Danger:** >600°C (risk of damage)

⚠️ **Note:** Thresholds vary by engine. Consult your engine manual!

## Hardware

See [Hardware Setup Guide](../hardware/setup.md) for:
- Wiring diagram
- Component list
- Installation instructions

## License

MIT License - See main repository [LICENSE](../../../LICENSE) file
