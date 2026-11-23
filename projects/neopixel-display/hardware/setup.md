# NeoPixel Display Hardware Setup

## Hardware Requirements

### Core Components
- **Raspberry Pi Pico** (or compatible RP2040 board)
- **NeoPixel LED Matrix** - 220 LEDs (20×11 arrangement)
  - Can be built from NeoPixel strip
  - Or WS2812B LED matrix panel
- **5V Power Supply** - High current (2-3A recommended for 220 LEDs)
- **Breadboard/PCB** - For connections

### Optional Components
- **IR Receiver Module** - VS1838B or compatible (for remote control)
- **Remote Control** - NEC protocol IR remote
- **Resistors** - 330-470Ω (data line), 10KΩ (pull-up)
- **Capacitor** - 1000μF electrolytic (power smoothing)

## Connections

### NeoPixel Matrix

```
Raspberry Pi Pico          NeoPixel Matrix
─────────────────          ───────────────
GPIO 4 (GP4)        ────►  Data In (DIN)
5V (VBUS)           ────►  +5V (Power)
GND                 ────►  GND
```

**Important**: For 220+ LEDs, use external 5V power:
```
External 5V Supply
───────────────────
+5V  ────────────────►  NeoPixel +5V
GND  ────────────────►  NeoPixel GND
GND  ────────────────►  Pico GND (common ground!)
```

### IR Receiver (Optional)

```
Raspberry Pi Pico          IR Receiver (VS1838B)
─────────────────          ─────────────────────
GPIO 14 (GP14)      ────►  OUT (Data)
3.3V (VOUT)         ────►  VCC
GND                 ────►  GND
```

## LED Matrix Layout

### Serpentine Pattern

The web interface uses a serpentine (boustrophedon) layout:

```
Row 1:  0   1   2   3   4   5   6   7   8   9  10   (left to right)
Row 2: 21  20  19  18  17  16  15  14  13  12  11   (right to left)
Row 3: 22  23  24  25  26  27  28  29  30  31  32   (left to right)
Row 4: 43  42  41  40  39  38  37  36  35  34  33   (right to left)
...
```

This accounts for how NeoPixel strips are typically wired in a back-and-forth pattern.

### Physical Arrangement

```
     ┌─────────────────────────────────┐
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 1
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 2
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 3
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 4
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 5
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 6
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 7
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 8
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 9
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 10
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 11
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 12
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 13
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 14
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 15
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 16
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 17
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 18
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 19
     │  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○  ○ │  Row 20
     └─────────────────────────────────┘
```

## Power Calculations

### Current Requirements

NeoPixel LEDs (WS2812B) current draw:
- **Per LED (white, full brightness)**: ~60mA
- **220 LEDs @ full white**: 220 × 60mA = **13.2A** (maximum!)
- **Typical usage (mixed colors)**: ~20mA per LED = **4.4A**
- **Dim usage (~20% brightness)**: ~12mA per LED = **2.6A**

### Recommendations

1. **Power Supply**: 5V, 3-5A minimum
2. **Wire Gauge**: 18-20 AWG for power lines
3. **Capacitor**: 1000μF across +5V/GND near LED matrix
4. **Fuse**: Consider 3-5A fuse for safety

## Building the Matrix

### From NeoPixel Strip

1. **Materials**:
   - NeoPixel strip (WS2812B, 60 LEDs/meter)
   - Mounting channel or frame
   - Diffuser (optional, for even lighting)

2. **Layout**:
   - Cut strip into 20 segments of 11 LEDs each
   - Connect segments in series
   - Mount in parallel rows with 180° turns

3. **Wiring**:
   - Solder data lines between segments
   - Use thick wires for power distribution
   - Inject power at multiple points for even brightness

### Pre-made Matrix

Alternatively, use a pre-made WS2812B matrix panel:
- Easier to install
- Better build quality
- More expensive
- Fixed resolution

## GPIO Pin Summary

| Function | GPIO Pin | Physical Pin | Notes |
|----------|----------|--------------|-------|
| NeoPixel Data | GPIO 4 | Pin 6 | Configurable |
| IR Receiver | GPIO 14 | Pin 19 | Optional |
| 5V Power | VBUS | Pin 40 | From USB or external |
| 3.3V Power | 3V3(OUT) | Pin 36 | For IR receiver |
| Ground | GND | Pin 38 | Common ground |

## Enclosure Options

1. **Picture Frame**: Mount matrix behind diffuser in frame
2. **Light Box**: 3D printed enclosure with diffuser
3. **Panel Mount**: Mount on wall or equipment rack
4. **Desktop Stand**: Angled stand for desk display

## Safety

⚠️ **High Current Warning**:
- NeoPixel matrices can draw significant current
- Use appropriate wire gauge
- Include fuse in power line
- Ensure good connections to prevent heating
- Never work on powered circuit

⚠️ **Power Sequence**:
1. Connect all data lines first
2. Connect ground
3. Apply power last

## Troubleshooting

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| No LEDs light up | No power | Check power supply, connections |
| First LED only | Bad data connection | Check GPIO 4, data line |
| Random colors | Insufficient power | Add capacitor, upgrade supply |
| Flickering | Loose connections | Resolder joints |
| Wrong pattern | Incorrect LED count | Update `strip` variable in code |

## Next Steps

1. Build or acquire your NeoPixel matrix
2. Connect to Pico following wiring diagram
3. Test with `colors.py` firmware
4. Use web interface to create custom patterns
5. Generate and upload your code
