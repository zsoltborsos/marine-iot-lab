# Image Converter for E-Paper Photo Album

## Overview

This folder contains documentation for converting images to the Python module format required by the E-Paper Photo Album firmware.

## Available Tool

A working image converter script is available in the main utilities folder:

**[`../../../../utilities/image-tools/README.md`](../../../../utilities/image-tools/README.md)**

**Original Source**: [st7789_mpy by russhughes](https://github.com/russhughes/st7789_mpy)

```bash
# Convert image to 1-bit black/white
python ../../../../utilities/image-tools/imgtobitmap.py photo.jpg 1 > IMG_0000_gs_d.py
```

See [`../../../../utilities/image-tools/README.md`](../../../../utilities/image-tools/README.md) for complete usage instructions and examples.

## Image Format Specification

### Output File Structure

Each converted image is a Python module with the following structure:

```python
width = 400
height = 280
img_bw = bytearray(b'\xf7\xfd\xff\xff\xab\xfe...')  # Required: Black/white data
# Optional for grayscale with red channel:
# img_red = bytearray(b'\x00\x12\xab\xff...')  # Red channel data
```

### Technical Details

**Display Resolution**: 400 × 280 pixels

**Pixel Format**: MONO_HLSB (Most Significant Bit, Horizontal, Least Significant Byte)
- 1 bit per pixel (black/white)
- 8 pixels per byte
- MSB first within each byte
- Rows stored sequentially

**Byte Layout**:
```
Byte 0: [P7 P6 P5 P4 P3 P2 P1 P0]  - First 8 pixels of row
Byte 1: [P15 P14 ... P8]            - Next 8 pixels
...
```

Where:
- `1` (bit set) = White pixel
- `0` (bit clear) = Black pixel

### File Naming Convention

```
IMG_XXXX_gs_d.py
```

Where:
- `IMG_` - Prefix
- `XXXX` - 4-digit sequence number (0000, 0001, etc.)
- `_gs_d` - Suffix (grayscale display)

**Examples**:
- `IMG_0000_gs_d.py`
- `IMG_0182_gs_d.py`
- `IMG_0999_gs_d.py`

## Converter Implementation Guide

### Required Libraries

```python
from PIL import Image  # Pillow
import numpy as np     # Optional, but helpful
```

### Basic Converter Structure

```python
from PIL import Image

def convert_image(input_path, output_path, output_width=400, output_height=280):
    """
    Convert an image to e-paper display format.
    
    Args:
        input_path: Path to source image (JPEG, PNG, etc.)
        output_path: Path for output .py file
        output_width: Target width (default: 400)
        output_height: Target height (default: 280)
    """
    # Open and convert image
    img = Image.open(input_path)
    img = img.convert('L')  # Convert to grayscale
    
    # Resize to display resolution
    img = img.resize((output_width, output_height), Image.LANCZOS)
    
    # Convert to 1-bit black/white
    img = img.convert('1', dither=Image.FLOYDSTEINBERG)
    
    # Convert to bytearray in MONO_HLSB format
    img_bw = bytearray()
    for y in range(output_height):
        for x in range(0, output_width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < output_width:
                    pixel = img.getpixel((x + bit, y))
                    # White pixel = 1, Black pixel = 0
                    if pixel > 128:
                        byte |= (1 << (7 - bit))
            img_bw.append(byte)
    
    # Generate Python file
    with open(output_path, 'w') as f:
        f.write(f"width = {output_width}\n")
        f.write(f"height = {output_height}\n")
        f.write(f"img_bw = bytearray({repr(img_bw)})\n")
    
    print(f"Converted {input_path} -> {output_path}")
    print(f"  Size: {output_width}x{output_height}")
    print(f"  Data size: {len(img_bw)} bytes")
```

### Batch Converter

```python
import os
from pathlib import Path

def batch_convert(input_folder, output_folder, start_index=0):
    """
    Convert all images in a folder.
    
    Args:
        input_folder: Folder containing source images
        output_folder: Folder for output .py files
        start_index: Starting sequence number
    """
    # Supported image formats
    extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    # Get all image files
    image_files = []
    for ext in extensions:
        image_files.extend(Path(input_folder).glob(f'*{ext}'))
        image_files.extend(Path(input_folder).glob(f'*{ext.upper()}'))
    
    # Sort for consistent ordering
    image_files.sort()
    
    # Convert each image
    for i, img_path in enumerate(image_files):
        index = start_index + i
        output_filename = f"IMG_{index:04d}_gs_d.py"
        output_path = Path(output_folder) / output_filename
        
        convert_image(str(img_path), str(output_path))
        print(f"Processed {i+1}/{len(image_files)}: {img_path.name}")
```

### Usage Example

```python
if __name__ == '__main__':
    # Single image conversion
    convert_image('photo.jpg', 'IMG_0000_gs_d.py')
    
    # Batch conversion
    batch_convert(
        input_folder='photos/',
        output_folder='sd_card/img_bw/',
        start_index=0
    )
```

## Grayscale with Red Channel

For displays supporting black, white, gray, and red:

### Two-Buffer Approach

```python
def convert_with_red(input_path, output_bw_path, output_red_path):
    """
    Convert image with separate red channel.
    
    Args:
        input_path: Source image
        output_bw_path: Output for black/white/gray data
        output_red_path: Output for red channel data
    """
    img = Image.open(input_path)
    img = img.resize((400, 280), Image.LANCZOS)
    
    # Extract red channel
    r, g, b = img.split()[:3]
    
    # Create red mask (pixels that are predominantly red)
    red_mask = Image.new('1', img.size)
    for x in range(img.width):
        for y in range(img.height):
            r_val = r.getpixel((x, y))
            g_val = g.getpixel((x, y))
            b_val = b.getpixel((x, y))
            # Pixel is "red" if red component dominates
            is_red = (r_val > g_val + 30) and (r_val > b_val + 30)
            red_mask.putpixel((x, y), 255 if is_red else 0)
    
    # Convert main image to grayscale
    gray = img.convert('L')
    bw = gray.convert('1', dither=Image.FLOYDSTEINBERG)
    
    # Generate both bytearrays
    img_bw = image_to_bytearray(bw)
    img_red = image_to_bytearray(red_mask)
    
    # Write output files
    write_image_module(output_bw_path, 400, 280, img_bw)
    write_image_module(output_red_path, 400, 280, img_red, is_red_channel=True)
```

## Optimization Tips

### 1. Dithering

Use Floyd-Steinberg dithering for better grayscale representation:

```python
img = img.convert('1', dither=Image.FLOYDSTEINBERG)
```

### 2. Contrast Enhancement

Enhance contrast before conversion:

```python
from PIL import ImageEnhance

enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(1.2)  # 20% contrast boost
```

### 3. Cropping

Auto-crop to focus on subject:

```python
# Center crop to aspect ratio
def center_crop(img, target_ratio=400/280):
    width, height = img.size
    current_ratio = width / height
    
    if current_ratio > target_ratio:
        # Image is too wide - crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        return img.crop((left, 0, left + new_width, height))
    else:
        # Image is too tall - crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        return img.crop((0, top, width, top + new_height))
```

### 4. Memory Efficiency

For large batches, generate files incrementally:

```python
def convert_and_save_incremental(input_path, output_path):
    img = Image.open(input_path)
    # ... process ...
    
    # Write file incrementally
    with open(output_path, 'w') as f:
        f.write("width = 400\n")
        f.write("height = 280\n")
        f.write("img_bw = bytearray(b'")
        
        # Write bytearray in chunks
        for i in range(0, len(img_bw), 32):
            chunk = img_bw[i:i+32]
            f.write(chunk.decode('latin-1'))
            if i + 32 < len(img_bw):
                f.write("\\\n")  # Line continuation
        
        f.write("')\n")
```

## Testing Your Converter

### Verify Output

```python
# Test that generated file can be imported
import IMG_0000_gs_d as test_img

print(f"Width: {test_img.width}")
print(f"Height: {test_img.height}")
print(f"Data size: {len(test_img.img_bw)} bytes")
print(f"Expected size: {test_img.width * test_img.height // 8} bytes")

# Verify size matches
assert len(test_img.img_bw) == test_img.width * test_img.height // 8
```

### Visual Verification

Load and display a test image to verify conversion quality.

## SD Card Organization

After conversion, organize files on SD card:

```
/sd/
├── index.txt              # Start at 0
├── img_bw/
│   ├── IMG_0000_gs_d.py   # First image
│   ├── IMG_0001_gs_d.py   # Second image
│   └── ...
└── img_red/               # Optional
    └── ...
```

## Future Improvements

Potential enhancements for the converter:

- [ ] GUI interface for easy conversion
- [ ] Preview converted images
- [ ] Automatic rotation/orientation
- [ ] Color to grayscale presets
- [ ] Batch rename and renumber
- [ ] Direct SD card writing
- [ ] Image optimization/compression

## References

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Waveshare e-Paper Documentation](https://www.waveshare.com/wiki/3.7inch_e-Paper_HAT)
- [MicroPython framebuf](https://docs.micropython.org/en/latest/library/framebuf.html)

## Contributing

If you create a working converter, consider contributing it back to this project!
