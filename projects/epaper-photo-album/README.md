# E-Paper Photo Album

A digital photo frame powered by Raspberry Pi Pico and a 3.7" e-paper display. The album cycles through photos stored on an SD card, displaying each for 5 minutes before entering deep sleep for ultra-low power consumption.

## Overview

This project transforms a Pico and e-paper display into a battery-friendly digital photo frame. Images are stored on an SD card in a special Python module format, and the system automatically cycles through them, waking every 5 minutes to display the next image.

## Features

- **3.7" E-Paper Display** - Sharp, low-power display
- **SD Card Storage** - Store hundreds of converted images
- **Automatic Cycling** - Advances to next image every 5 minutes
- **Deep Sleep** - Ultra-low power between updates
- **UART Logging** - Serial debug output
- **Index Tracking** - Remembers which image to show next

## Project Structure

```
EPaperPhotoAlbum/
├── README.md              # This file
├── firmware/
│   ├── main.py            # Main photo cycler (entry point)
│   ├── main_2.py          # Alternative version
│   ├── epaper.py          # 3.7" e-paper display driver
│   ├── myepaper.py        # E-paper controller class (phoreglad's driver, see below)
│   ├── mysd.py            # SD card interface
│   ├── myuart.py          # UART logging utility
│   └── logger.py          # Debug logging helper
├── hardware/
│   └── setup.md           # Wiring and hardware setup
└── utils/
    └── image_converter/   # Image conversion tools
        └── README.md      # Converter documentation
```

## How It Works

1. **Boot**: Pico wakes from deep sleep
2. **Read Index**: Opens `sd/index.txt` to get current image number
3. **Load Image**: Imports the corresponding `.py` file from `sd/img_bw/`
4. **Display**: Renders image on e-paper display
5. **Update Index**: Increments `index.txt` for next wake
6. **Deep Sleep**: Sleeps for 5 minutes (300 seconds)
7. **Repeat**: Cycle continues indefinitely

## Image Format

Images must be converted to Python modules with the following structure:

```python
width = 400
height = 280
img_bw = bytearray(b'\xf7\xfd\xff...')  # Black/white bitmap data
# Optional for grayscale with red:
# img_red = bytearray(b'...')  # Red channel data
```

**File naming**: `IMG_xxxx_gs_d.py` (e.g., `IMG_0182_gs_d.py`)

**Storage location**: `/sd/img_bw/` folder on SD card

## Image Conversion

⚠️ **Note**: The image converter script is not included in this repository. You'll need to create or recreate a Python script that:

1. Reads JPEG/PNG images using PIL/Pillow
2. Converts to black & white or grayscale
3. Generates Python bytearray format
4. Outputs `.py` files compatible with the firmware

See [`utils/image_converter/README.md`](utils/image_converter/README.md) for format specifications.

### Basic Converter Structure (Example)

```python
from PIL import Image
import numpy as np

def convert_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert('1')  # Convert to 1-bit black/white
    img = img.resize((400, 280))
    
    # Convert to bytearray in MONO_HLSB format
    # Generate .py file with width, height, img_bw
    
    with open(output_path, 'w') as f:
        f.write(f"width = {width}\n")
        f.write(f"height = {height}\n")
        f.write(f"img_bw = bytearray({bytearray_data})\n")
```

## Hardware Setup

### Components

- **Raspberry Pi Pico** (or Pico W)
- **3.7" E-Paper Display** (Waveshare or compatible)
- **MicroSD Card Module** (SPI interface)
- **MicroSD Card** (FAT32 formatted)
- **3.3V Power** (Pico can power display)

### Wiring

#### E-Paper Display (SPI)

```
Pico          E-Paper 3.7"
────          ────────────
GPIO 12  ──►  BUSY
GPIO 13  ──►  RST
GPIO 14  ──►  DC
GPIO 15  ──►  CS
GPIO 18  ──►  SCK
GPIO 19  ──►  MOSI
3.3V     ──►  VCC
GND      ──►  GND
```

#### SD Card Module (SPI)

```
Pico          SD Card Module
────          ──────────────
GPIO 16  ──►  MISO
GPIO 18  ──►  SCK
GPIO 19  ──►  MOSI
GPIO 14  ──►  CS
3.3V     ──►  VCC
GND      ──►  GND
```

**Note**: Pin configurations can be customized in the firmware.

### SD Card Setup

1. **Format**: FAT32 filesystem
2. **Create folders**:
   - `/img_bw/` - Store converted image files here
   - (Optional) `/img_red/` - For red channel data
3. **Create index file**: `index.txt` with starting number (e.g., `0`)
4. **Copy images**: Place converted `.py` files in `/img_bw/`

## Usage

### First Time Setup

1. Wire display and SD card module to Pico
2. Format SD card as FAT32
3. Create folder structure on SD card
4. Convert and copy images to `/sd/img_bw/`
5. Create `index.txt` with `0`
6. Copy firmware to Pico

### E-Paper Driver

`myepaper.py` is based on `Pico_ePaper.py` from phoreglad's
[pico-epaper](https://github.com/phoreglad/pico-epaper), an earlier version lightly modified for
this project. Credit for the driver goes to its author. The upstream repository publishes no
licence, so this file is not covered by this repository's MIT licence.

### Running

1. Power on Pico
2. `main.py` runs automatically
3. First image displays
4. System enters deep sleep for 5 minutes
5. Repeats from step 3

### Changing Images

Add new converted `.py` files to `/sd/img_bw/` on the SD card. The system will automatically cycle through all images.

### Resetting Cycle

Delete or reset `sd/index.txt` to `0` to start from the beginning.

## Debugging

### UART Output

The system sends debug information via UART:

- Startup messages
- Current image index
- Image loading status
- Memory usage
- Errors

**UART Settings**:
- Baudrate: 115200
- TX: GPIO 0 (or as configured)
- RX: GPIO 1 (or as configured)

### Common Issues

**Issue**: "Could not open file"
- Check image file exists in `/sd/img_bw/`
- Verify filename matches index
- Check SD card is mounted properly

**Issue**: Display shows garbage
- Verify wiring connections
- Check power supply
- Confirm display initialization

**Issue**: Won't wake from sleep
- Check deep sleep implementation
- Verify RTC or timer configuration
- Ensure adequate power

## Power Consumption

- **Active (displaying)**: ~50-100mA
- **Deep Sleep**: ~0.1-1mA
- **Average (5-min cycle)**: Very low, suitable for battery operation

## Customization

### Change Display Time

Edit `main.py`:
```python
machine.deepsleep(300000)  # 300000ms = 5 minutes
# Change to desired time in milliseconds
```

### Change Display Size

Update dimensions in the e-paper driver (`myepaper.py`) and image converter.

### Add Red Channel Support

Modify `main.py` to handle `img_red` data and update `showImage()` function.

## Future Enhancements

- [ ] Include image converter script
- [ ] WiFi sync for remote image updates
- [ ] Real-time clock for scheduled updates
- [ ] Multiple display modes (slideshow, clock, etc.)
- [ ] Web interface for image management
- [ ] Motion sensor wake-up

## Related Documentation

- [Hardware Setup](hardware/setup.md) - Detailed wiring and components
- [Image Converter](utils/image_converter/README.md) - Format specifications and tool usage

## License

MIT License - see the main repository [LICENSE](../../LICENSE). The e-paper driver code is adapted from Waveshare's example; see [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).
