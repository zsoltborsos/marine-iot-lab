# E-Paper Photo Album Hardware Setup

## Components Required

### Core Components

| Component | Description | Notes |
|-----------|-------------|-------|
| **Raspberry Pi Pico** | RP2040 microcontroller | Pico W also works |
| **3.7" E-Paper Display** | Waveshare or compatible | 400×280 resolution, SPI interface |
| **MicroSD Card Module** | SPI interface | 3.3V compatible |
| **MicroSD Card** | 4GB-32GB recommended | FAT32 formatted |
| **Breadboard/PCB** | For connections | Perfboard or custom PCB |
| **Jumper Wires** | F/F or F/M | As needed for connections |

### Optional Components

| Component | Purpose | Notes |
|-----------|---------|-------|
| **RTC Module** | Real-time clock | DS3231, PCF8523 |
| **Motion Sensor** | Auto wake-up | PIR sensor |
| **Light Sensor** | Auto brightness | LDR or BH1750 |
| **Enclosure** | Protection | 3D printed or project box |
| **Battery** | Portable power | LiPo + charger module |

## Display Specifications

### 3.7" E-Paper (Waveshare)

- **Resolution**: 400 × 280 pixels
- **Colors**: Black, White, Gray (4 levels)
- **Interface**: SPI
- **Power**: 3.3V logic
- **Pins**: BUSY, RST, DC, CS, SCK, MOSI

### Alternative Displays

This firmware is written for the 3.7" display but can be adapted for:
- 2.7" e-paper (264×176)
- 4.2" e-paper (400×300)
- 7.5" e-paper (800×480)

Modify `myepaper.py` for different display sizes.

## Wiring Diagram

### Pico to E-Paper Display

```
┌─────────────────┐          ┌──────────────────────┐
│  Raspberry Pi   │          │  3.7" E-Paper        │
│  Pico           │          │  Display             │
│                 │          │                      │
│  GPIO 12 (GP12) ├─────────►│  BUSY                │
│  GPIO 13 (GP13) ├─────────►│  RST                 │
│  GPIO 14 (GP14) ├─────────►│  DC                  │
│  GPIO 15 (GP15) ├─────────►│  CS                  │
│  GPIO 18 (GP18) ├─────────►│  SCK                 │
│  GPIO 19 (GP19) ├─────────►│  MOSI                │
│  3.3V (OUT)     ├─────────►│  VCC                 │
│  GND            ├─────────►│  GND                 │
│                 │          │                      │
│                 │          │  MISO (not used)     │
└─────────────────┘          └──────────────────────┘
```

### Pico to SD Card Module

```
┌─────────────────┐          ┌──────────────────────┐
│  Raspberry Pi   │          │  MicroSD Card        │
│  Pico           │          │  Module              │
│                 │          │                      │
│  GPIO 16 (GP16) ├─────────►│  MISO                │
│  GPIO 18 (GP18) ├─────────►│  SCK                 │
│  GPIO 19 (GP19) ├─────────►│  MOSI                │
│  GPIO 14 (GP14) ├─────────►│  CS                  │
│  3.3V (OUT)     ├─────────►│  VCC                 │
│  GND            ├─────────►│  GND                 │
└─────────────────┘          └──────────────────────┘
```

### Complete Pin Mapping

| Function | Pico Pin | GPIO | Display | SD Card |
|----------|----------|------|---------|---------|
| SPI SCK  | Pin 24   | 18   | ✓       | ✓       |
| SPI MOSI | Pin 25   | 19   | ✓       | ✓       |
| SPI MISO | Pin 20   | 16   | -       | ✓       |
| Display CS | Pin 20 | 15   | ✓       | -       |
| SD CS    | Pin 19   | 14   | -       | ✓       |
| Display DC | Pin 19 | 14   | ✓       | -       |
| Display RST | Pin 18 | 13  | ✓       | -       |
| Display BUSY | Pin 17 | 12 | ✓       | -       |
| 3.3V     | Pin 36   | -    | ✓       | ✓       |
| GND      | Pin 38   | -    | ✓       | ✓       |

**Note**: SD card CS uses a different pin than display CS. Modify `mysd.py` if you change the CS pin.

## Power Considerations

### Current Requirements

| State | Display | Pico | Total |
|-------|---------|------|-------|
| **Active (refresh)** | ~50mA | ~100mA | ~150mA |
| **Active (idle)** | ~1mA | ~80mA | ~81mA |
| **Deep Sleep** | 0mA | ~0.1-1mA | ~0.1-1mA |

### Power Supply Options

1. **USB Power**
   - Simple, reliable
   - Requires USB cable/wall adapter
   - ~500mA recommended

2. **Battery Power**
   - LiPo battery (3.7V) + boost converter to 5V
   - 18650 cell + regulator
   - Consider capacity for desired runtime

3. **USB + Battery Backup**
   - USB power with automatic battery backup
   - Best of both worlds

### Power Saving Tips

- Use deep sleep between image updates
- Minimize active time
- Consider larger update intervals (10-15 min)
- Use partial refresh if supported

## SD Card Preparation

### Formatting

1. **Format as FAT32**
   - Windows: Use built-in formatter
   - Mac: Disk Utility (MS-DOS FAT)
   - Linux: `mkfs.vfat -F 32 /dev/sdX`

2. **Recommended Size**: 4GB-32GB
   - Larger cards may have compatibility issues
   - More than enough for hundreds of images

### Folder Structure

Create the following structure on the SD card:

```
/ (root)
├── index.txt           # Current image index (e.g., "0")
├── img_bw/             # Black/white images
│   ├── IMG_0000_gs_d.py
│   ├── IMG_0001_gs_d.py
│   └── ...
└── img_red/            # Optional: Red channel images
    ├── IMG_0000_gs_d.py
    └── ...
```

### Creating index.txt

Create a text file named `index.txt` containing a single number:
```
0
```

This tells the system which image to display first.

## Assembly Steps

### 1. Prepare Components

- Cut header pins to size
- Label wires for identification
- Test components before assembly

### 2. Connect Display

1. Solder or plug in display header
2. Connect SPI lines (SCK, MOSI)
3. Connect control lines (CS, DC, RST, BUSY)
4. Connect power (3.3V, GND)

### 3. Connect SD Card Module

1. Connect SPI lines (shared with display)
2. Connect CS to separate GPIO
3. Connect power (3.3V, GND)

### 4. Test Connections

- Check for shorts with multimeter
- Verify all connections match diagram
- Ensure good solder joints

### 5. Initial Test

1. Insert SD card with test image
2. Connect USB power
3. Observe display refresh
4. Check UART output for errors

## Enclosure Options

### 3D Printed Frame

- Design to fit display + Pico
- Include SD card access slot
- Mounting holes for wall hanging

### Project Box

- Standard electronics enclosure
- Cut window for display
- Drill holes for SD card access

### Picture Frame Conversion

- Use existing picture frame
- Mount display behind glass/acrylic
- Hide electronics in back box

## Troubleshooting

### Display Not Working

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No display | No power | Check 3.3V connection |
| Garbage display | Bad SPI connection | Check SCK, MOSI wiring |
| Partial display | Wrong initialization | Verify display driver |
| Flickering | Insufficient power | Add capacitor, check supply |

### SD Card Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Card not detected | Wrong wiring | Check MISO, MOSI, CS |
| Can't read files | Wrong format | Reformat as FAT32 |
| Missing images | Wrong path | Check folder structure |

### Sleep Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Won't sleep | Code error | Check deepsleep call |
| Won't wake | Power issue | Check battery/connection |
| Random wakes | Noise on GPIO | Add pull-down resistors |

## Testing Checklist

- [ ] All connections match wiring diagram
- [ ] SD card formatted as FAT32
- [ ] Folder structure created
- [ ] Test image converted and copied
- [ ] index.txt created
- [ ] USB power connected
- [ ] Display refreshes on boot
- [ ] Image displays correctly
- [ ] System enters deep sleep
- [ ] System wakes and advances to next image

## Next Steps

Once hardware is assembled and tested:

1. Convert your photos to the required format
2. Copy to SD card
3. Power up and enjoy!

See [Image Converter README](../../../utilities/image-tools/README.md) for photo conversion instructions.
