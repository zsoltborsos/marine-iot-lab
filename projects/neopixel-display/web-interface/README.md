# NeoServer - NeoPixel Web Interface

A web-based visual editor for designing NeoPixel LED patterns.

## Overview

NeoServer is a Node.js web application that provides a visual interface for designing LED patterns. You select pixels and colors on a grid, and it generates MicroPython code that you can copy to your Raspberry Pi Pico.

## Features

- **Visual Grid Editor**: 20×11 pixel matrix (220 LEDs)
- **RGB Color Picker**: Three sliders for precise color selection
- **Serpentine Mapping**: Accounts for alternating row wiring
- **Code Generation**: Outputs ready-to-use MicroPython code
- **Responsive UI**: Bootstrap 5 design

## Technology Stack

- **Backend**: Node.js + Express.js
- **Frontend**: Vue.js 3 + Bootstrap 5
- **Template**: EJS

## Installation

### Prerequisites
- Node.js (v14 or later)
- npm (comes with Node.js)

### Setup

```bash
cd web-interface
npm install
```

### Running

```bash
npm start
```

Then open your browser to: `http://localhost:3000`

## Usage

### 1. Select Pixels

Click on grid cells to select them. Selected pixels will have a green border.

### 2. Choose Color

Use the RGB sliders to select your desired color:
- **Red**: 0-255
- **Green**: 0-255
- **Blue**: 0-255

The preview box shows the selected color.

### 3. Apply Color

Click on selected pixels to apply the current color. The pixel will show its RGB values.

### 4. Generate Code

Click **"Generate neopixel list"** to create MicroPython code.

### 5. Copy and Use

Copy the generated code and paste it into your MicroPython file:

```python
from machine import Pin
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
np = NeoPixel(pin, 300)

# Paste generated code here
np[0] = (25, 10, 5)
np[1] = (30, 15, 8)
np[2] = (22, 12, 6)
# ... etc

np.write()
```

## Interface Layout

```
┌─────────────────────────────────────────┐
│  NeoServer                              │
├─────────────────────────────────────────┤
│                                         │
│  Color Picker                           │
│  ┌─────────────────────────────────┐   │
│  │  Red   │  Green │  Blue         │   │
│  │   0    │   0    │   0           │   │
│  │  ████  │  ████  │  ████         │   │
│  │ ─────  │ ─────  │ ─────         │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │      Color Preview Box          │   │
│  └─────────────────────────────────┘   │
│                                         │
│  Pixel Grid (20 rows × 11 columns)     │
│  ┌─────────────────────────────────┐   │
│  │ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○           │   │
│  │ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○           │   │
│  │ ... (click to select)           │   │
│  └─────────────────────────────────┘   │
│                                         │
│  [Generate neopixel list]              │
│                                         │
│  Neopixel list:                        │
│  np[0] = (25, 10, 5)                   │
│  np[1] = (30, 15, 8)                   │
│  ...                                   │
└─────────────────────────────────────────┘
```

## File Structure

```
web-interface/
├── app.js                 # Express app configuration
├── package.json           # Node.js dependencies
├── bin/
│   └── www              # Server startup script
├── routes/
│   ├── index.js         # Home page route
│   └── users.js         # (unused)
├── views/
│   ├── index.ejs        # Main Vue.js app
│   └── error.ejs        # Error page
└── public/
    ├── stylesheets/
    │   └── style.css    # Custom styles
    ├── javascripts/
    │   └── (empty)      # (Vue.js is inline)
    └── images/
        └── (empty)
```

## Customization

### Changing Grid Size

Edit `views/index.ejs`:

```javascript
// In the template section
<div v-for="row in 20">      <!-- Change row count -->
  <my-pixel v-for="col in 11">  <!-- Change column count -->

// In the data() function
columns: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],  // Update array
rows: [1, 2, 3, ... 20],                        // Update array
```

### Changing LED Mapping

The `getNeopixelId()` function handles serpentine mapping:

```javascript
getNeopixelId(row, col) {
  if (row % 2 === 0) {
    // Even rows: right to left
    return (10 + (row - 2) * 11) + (12 - col)
  } else {
    // Odd rows: left to right
    if (row === 1) {
      return col - 1
    } else {
      return (10 + (row - 2) * 11) + col
    }
  }
}
```

Modify this function to match your physical LED wiring.

### Brightness Scaling

The generated code divides colors by 10:

```javascript
const r = Math.ceil(pixel.color.r / 10)
const g = Math.ceil(pixel.color.g / 10)
const b = Math.ceil(pixel.color.b / 10)
```

Adjust the divisor for different brightness levels.

## Styling

Custom CSS is in `public/stylesheets/style.css`:

```css
.field {
  border-width: 4px;
  border-color: black;
  border-style: solid;
  height: 40px;
  margin: 1px;
}

.selected {
  border-color: rgb(13, 155, 44);  /* Green border */
}
```

## Development

### Adding New Routes

1. Create route handler in `routes/`
2. Import in `app.js`
3. Use with `app.use()`

### Adding Stylesheets

Add to `public/stylesheets/` and link in `views/index.ejs`:

```html
<link rel="stylesheet" href="/stylesheets/your-style.css" />
```

### Adding JavaScript

Inline Vue.js is used. For external scripts, add to `public/javascripts/` and link in the view.

## Troubleshooting

**Issue**: Server won't start
```bash
# Check Node.js version
node --version

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Issue**: Page shows errors
- Check browser console (F12)
- Verify Vue.js loaded from CDN
- Check network tab for failed requests

**Issue**: Generated code doesn't work
- Verify LED count matches your hardware
- Check GPIO pin number
- Ensure power is adequate

## Tips

1. **Save Your Designs**: Copy generated code to a file for later use
2. **Test Incrementally**: Start with few pixels, then expand
3. **Use Preset Colors**: Note down RGB values you like
4. **Browser Zoom**: Adjust zoom for better visibility

## Future Enhancements

Potential improvements:
- Save/load designs
- Animation support
- Multiple color presets
- Export/import patterns
- Real-time preview (with WebSocket to Pico)

## Related Documentation

- [Main README](../README.md) - Project overview
- [Firmware](../firmware/) - MicroPython code
- [Hardware Setup](../hardware/setup.md) - Wiring guide
