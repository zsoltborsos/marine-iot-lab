# Image Conversion Tools

Tools for converting images for use in MicroPython display projects.

## imgtobitmap.py

**Based on**: [st7789_mpy by russhughes](https://github.com/russhughes/st7789_mpy)

This is a very useful image converter tool that I found in the st7789_mpy repository. It converts image files to Python modules for use with display blit operations.

Convert image files to Python modules for use with display blit operations.

### Usage

```bash
python imgtobitmap.py image_file bits_per_pixel > output.py
```

**Arguments**:
- `image_file` - Path to source image (JPG, PNG, etc.)
- `bits_per_pixel` - Color depth (1-8 bits)
  - `1` = 2 colors (black/white)
  - `2` = 4 colors
  - `4` = 16 colors
  - `8` = 256 colors

### Examples

**Black and white (1-bit)**:
```bash
python imgtobitmap.py photo.jpg 1 > photo_bw.py
```

**4-color grayscale**:
```bash
python imgtobitmap.py photo.jpg 2 > photo_4color.py
```

**16-color**:
```bash
python imgtobitmap.py photo.jpg 4 > photo_16color.py
```

### Output Format

The script generates a Python module with:
```python
HEIGHT = 280
WIDTH = 400
COLORS = 2
BITS = 112000
BPP = 1
PALETTE = [0x0000, 0xffff]
_bitmap = b'\xff\xfd\xab\xfe...'
BITMAP = memoryview(_bitmap)
```

### For E-Paper Photo Album

The EPaperPhotoAlbum project uses a slightly different format. You'll need to adapt the output:

```python
# imgtobitmap.py output needs renaming:
width = WIDTH
height = HEIGHT
img_bw = bytearray(BITMAP)  # Convert memoryview to bytearray
```

---

## Rotated Images for Sideways Display

**Important**: The standard `imgtobitmap.py` script doesn't include rotation. If you're mounting your display sideways (like a mini TV), you have two options:

### Option 1: Pre-rotate Images (Recommended)

Pre-rotate your images 90° before conversion. This avoids runtime rotation which can crash the Pico due to memory constraints.

**Workflow:**
1. Rotate images 90° in your image editor (Photoshop, GIMP, etc.)
2. Resize to display dimensions (swapped for rotation)
3. Convert with imgtobitmap.py

**Example for 3.7" e-paper (400x280) mounted sideways:**
```bash
# 1. Rotate and resize in ImageMagick:
convert input.jpg -rotate 90 -resize 280x400! rotated_input.jpg

# 2. Convert to bitmap:
python imgtobitmap.py rotated_input.jpg 1 > rotated_image.py

# 3. In your MicroPython code, use swapped dimensions:
width = 280   # Swapped
height = 400  # Swapped
```

**Benefits:**
- ✅ No runtime rotation overhead
- ✅ No memory issues on Pico
- ✅ Faster image loading
- ✅ Simpler code

**Drawbacks:**
- ❌ Requires pre-processing step
- ❌ Original images must be re-rotated for each use

### Option 2: Runtime Rotation (Not Recommended)

You can rotate in code, but this has significant drawbacks:

```python
# This will likely CRASH the Pico due to memory constraints!
def rotate_bitmap(bitmap, width, height):
    # Requires creating a new buffer for rotated image
    # Very memory-intensive on embedded systems
    pass
```

**Why NOT to use runtime rotation:**
- ❌ **Out of Memory** - Pico only has 264KB RAM
- ❌ **Slow** - Rotation is CPU-intensive
- ❌ **Complex** - More code to maintain

**Recommendation:** Always pre-rotate images before conversion for embedded displays.

---

### Requirements

- Python 3
- Pillow (PIL)

Install dependencies:
```bash
pip install Pillow
```

### Related Tools

- **font2bitmap.py** - Convert fonts to bitmap format
- **hershey_to_py.py** - Convert Hershey fonts
- **sprites2bitmap.py** - Convert sprite sheets

## ImageMagick Alternative

For simple JPG conversion:

```bash
# Install ImageMagick
sudo apt-get install imagemagick  # Linux
brew install imagemagick          # macOS

# Convert SVG to JPG
convert input.svg -type TrueColor output.jpg

# Resize and convert
convert input.png -resize 400x280 output.jpg
```

See `howto-convert-to-jpg` for more details.

## Batch Conversion Script

Example bash script for batch conversion:

```bash
#!/bin/bash
for img in *.jpg; do
    python imgtobitmap.py "$img" 1 > "${img%.jpg}_bw.py"
done
```

## Notes

- Images are automatically quantized to the requested color depth
- Dithering is handled by Pillow's adaptive palette
- For e-paper displays, use 1-bit (black/white) for best results
- Consider pre-processing images for optimal contrast
