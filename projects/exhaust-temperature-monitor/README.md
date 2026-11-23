# Exhaust Temperature Monitor

A design for a marine safety system to monitor exhaust gas temperature while motoring.

> **Status: design and plan, not built.** No hardware has been built and the firmware has not been run on hardware. Everything below describes the intended design.

## The Story: Why This Matters

When you're **motoring** (not sailing) on a boat, exhaust temperature is one of the **most crucial pieces of information** you need to monitor.

### The Problem

While sailing, the engine is off and everything is fine. But when you switch to motor power:
- The engine runs for extended periods
- Cooling systems work harder
- Exhaust temperatures can climb dangerously high
- **Overheating can cause serious engine damage** - potentially leaving you stranded at sea

### The Planned Solution

A dedicated exhaust temperature monitor that would:
- Continuously monitors exhaust gas temperature
- Alerts you before critical overheating occurs
- Logs temperature data for troubleshooting
- Runs independently from the boat's main electrical system

### Marine Environment Challenges

This isn't just a temperature sensor - it's designed for the marine environment:
- **Vibration**: Engine mounting creates constant vibration
- **Heat**: Exhaust systems get extremely hot
- **Moisture**: Salt water, humidity, condensation
- **EMI**: Engine electronics create electrical noise
- **Power**: Must work from boat's 12V system

---

## Project Status

**Current Phase**: 📐 Design and plan

### What Exists
- A MAX31855 driver sketch (`firmware/max31855.py`), untested on hardware
- A basic temperature reading script (`firmware/checktemp.py`), untested on hardware
- Wiring and installation notes

### What's Needed
- [ ] Thermocouple probe selection (high-temperature rated)
- [ ] Exhaust mounting hardware design
- [ ] Waterproof enclosure
- [ ] Display/interface (TBD)
- [ ] Alarm system (visual + audible)
- [ ] Data logging
- [ ] Marine-grade wiring and connectors

---

## Hardware

### Temperature Sensor

**Chip**: MAX31855 Thermocouple Amplifier
**Interface**: SPI (CLK, CS, DO — read-only, no MOSI)
**Sensor Type**: K-type thermocouple

**Why MAX31855**:
- Cold junction compensation built-in
- High accuracy (±2°C typical)
- Wide temperature range (-270°C to +1372°C)
- Digital output (noise immune)
- Simple interface

### Wiring

```
Raspberry Pi Pico    MAX31855 Module
─────────────────    ───────────────
GPIO 2  (SCK)   ──►  CLK
GPIO 4  (MISO)  ──►  DO
GPIO 5  (CS)    ──►  CS
3.3V            ──►  VCC
GND             ──►  GND
```

**Note**: The MAX31855 is SPI-only and read-only (no MOSI/DI pin needed).

### Thermocouple Probe

**Requirements**:
- **Temperature Range**: 0°C to 800°C (exhaust can get very hot!)
- **Probe Type**: K-type thermocouple
- **Sheath Material**: Stainless steel (marine environment)
- **Length**: Sufficient to reach from mounting point
- **Connector**: Standard thermocouple connector

**Mounting Location**:
- Exhaust elbow or riser
- After raw water cooling point (cooler, safer)
- Accessible for maintenance
- Away from direct water spray

---

## Firmware

### File Structure

```
ExhaustTemperatureMonitor/
├── firmware/
│   ├── max31855.py          # Thermocouple amplifier driver
│   └── checktemp.py         # Main temperature reader
├── hardware/
│   └── setup.md             # Planned hardware and installation guide
└── README.md                # This file
```

### Usage

```python
from machine import Pin, SPI
from max31855 import MAX31855
import time

# MAX31855 is SPI-only (CLK, CS, DO — no MOSI)
spi = SPI(0, baudrate=5_000_000, polarity=0, phase=0, sck=Pin(2), miso=Pin(4))
cs = Pin(5, Pin.OUT)

# Create sensor instance
maxi = MAX31855(spi, cs)

# Main loop
while True:
    try:
        temp = maxi.read_celsius()
        print("Exhaust Temperature: %s °C" % temp)
        
        # Alarm thresholds (adjust for your engine)
        if temp and temp > 400:
            print("WARNING: High exhaust temperature!")
        if temp and temp > 500:
            print("CRITICAL: Shut down engine!")
            
        time.sleep(1)
    except Exception as e:
        print("Sensor error:", e)
        time.sleep(1)
```

### Temperature Thresholds

**Typical Diesel Engine Exhaust**:
- **Normal**: 200-400°C
- **Warning**: 400-500°C
- **Critical**: >500°C
- **Danger**: >600°C (risk of damage)

⚠️ **Note**: Thresholds vary by engine. Consult your engine manual!

---

## Planned Features

### Phase 1: Basic Monitor
- [ ] Temperature reading (driver sketch written, untested)
- [ ] OLED/LCD display
- [ ] Visual warning LED
- [ ] Mounting bracket design

### Phase 2: Enhanced Alerts
- [ ] Audible alarm (buzzer)
- [ ] Multiple warning levels
- [ ] Silence button
- [ ] Peak temperature hold

### Phase 3: Data Logging
- [ ] SD card logging
- [ ] Temperature graphing
- [ ] USB download capability
- [ ] Time/date stamping

### Phase 4: Integration
- [ ] NMEA 2000 output (for chartplotters)
- [ ] WiFi alerts (to phone/tablet)
- [ ] Engine shutdown relay (emergency only)
- [ ] Multiple sensor support (raw water, oil, etc.)

---

## Installation Considerations

### Thermocouple Mounting

1. **Drill & Tap**: Exhaust elbow for thermocouple boss
2. **Use Existing**: Some engines have sensor ports
3. **Clamp-on**: External sensor (less accurate, easier)

### Waterproofing

- **Enclosure**: IP67 or better
- **Connectors**: Marine-grade, gold-plated
- **Wire**: Tinned copper (corrosion resistant)
- **Sealing**: Silicone or epoxy at entry points

### Power Supply

- **Input**: 12V DC (boat system)
- **Regulation**: 5V or 3.3V for Pico
- **Protection**: Fuse, reverse polarity protection
- **Backup**: Battery backup for alarm

---

## Testing & Calibration

### Before Installation

1. **Bench Test**: Verify readings with known temperature
2. **Ice Water**: Should read ~0°C
3. **Boiling Water**: Should read ~100°C (at sea level)
4. **Compare**: Against known-good thermometer

### After Installation

1. **Cold Start**: Verify ambient reading
2. **Warm Up**: Monitor temperature rise
3. **Under Load**: Check at various RPM
4. **Log Data**: Establish baseline for your engine

---

## Safety Warnings

⚠️ **High Voltage/Heat**: Exhaust systems are dangerous
- Never touch hot exhaust components
- Allow engine to cool before installation
- Use heat-resistant gloves and tools

⚠️ **Marine Safety**: This is a monitoring device, not a replacement for:
- Regular engine maintenance
- Temperature gauges
- Good seamanship
- Common sense

⚠️ **False Readings**: Sensor failure could give false security
- Regular testing recommended
- Don't rely solely on this device
- Have backup temperature monitoring

---

## Related Projects

- [Battery Monitor System](../battery-monitor-system/) - Another marine monitoring project
- [Utilities](../../utilities/) - Reusable MicroPython utilities

## The Story Behind This Project

This plan was inspired by a real incident at sea. While crewing on a passage from Liverpool to Penzance, the engine overheated in the dark waters around Land's End due to a loose raw water filter. The problem was discovered only because the captain's bunk was next to the engine compartment - from the helm, there was no indication anything was wrong.

Read the full story on [zsoltborsos.net](https://zsoltborsos.net).

---

## Credits & References

- **MAX31855 Datasheet**: Maxim Integrated
- **K-Type Thermocouples**: Omega Engineering
- **Marine Electrical Standards**: ABYC, ISO

---

## License

MIT License - see the main repository [LICENSE](../../LICENSE). The software comes with no warranty; use at your own risk.

**Safety First**: Always follow proper marine safety procedures when working on engine systems.
