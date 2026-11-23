# Third-Party Notices

Marine IoT Lab is MIT-licensed (see [LICENSE](LICENSE)), but several projects bundle code written
by other people. That code stays under its authors' licences, listed below. Where a source file
carries its own copyright header, that header applies.

## Peter Hinch: micropython-nano-gui

- **Source:** https://github.com/peterhinch/micropython-nano-gui
- **Licence:** MIT, Copyright (c) 2018 Peter Hinch (some files also name Ihor Nehrutsa)
- **Files:** in each of `projects/battery-monitor-system/firmware/dashboard/`,
  `display-prototype/` and `screenless-prototype/`:
  - `gui/core/`, `gui/widgets/`: the nano-gui core and widgets
  - `gui/fonts/courier20.py` (dashboard): a bitmap font shipped with nano-gui, generated from
    Courier Prime with [micropython-font-to-py](https://github.com/peterhinch/micropython-font-to-py)
  - `drivers/boolpalette.py`
  - `drivers/st7789/st7789_4bit.py` (display prototypes), Copyright (c) 2021 Peter Hinch, Ihor Nehrutsa
  - `color_setup.py` in the display prototypes, adapted from nano-gui's example

## Peter Hinch: micropython-async

- **Source:** https://github.com/peterhinch/micropython-async
- **Licence:** MIT, Copyright (c) 2016 Peter Hinch
- **Files:** `primitives/` in `projects/battery-monitor-system/firmware/display-prototype/` and
  `screenless-prototype/`

## Bitmap font: arial35.py

- **Files:** `gui/fonts/arial35.py` in the display and screenless prototypes
- **Font:** generated from Liberation Sans Regular (SIL Open Font License 1.1, metric-compatible
  with Arial) with [micropython-font-to-py](https://github.com/peterhinch/micropython-font-to-py)
  (MIT). The file keeps its old name so the firmware imports are unchanged.

## Waveshare: Pico e-Paper 3.7 driver

- **Source:** https://github.com/waveshare/Pico_ePaper_Code
- **Licence:** the files carry Waveshare's MIT-style permission notice in their headers (kept in
  place). Note that the upstream repository as a whole is published under GPL-3.0.
- **Files:**
  - `projects/battery-monitor-system/firmware/dashboard/Pico-ePaper-3.7.py`
  - `projects/battery-monitor-system/firmware/dashboard/drivers/ePaper3in7.py` (adapted for nano-gui)
  - `projects/battery-monitor-system/firmware/dashboard/spitest.py` and `utilities/displays/spitest.py`
  - `projects/epaper-photo-album/firmware/epaper.py`

## phoreglad: pico-epaper

- **Source:** https://github.com/phoreglad/pico-epaper (`Pico_ePaper.py`)
- **Author:** phoreglad
- **Licence:** none published upstream. This file is not covered by this repository's MIT
  licence; all rights stay with its author.
- **Files:** `projects/epaper-photo-album/firmware/myepaper.py` (an earlier version of
  `Pico_ePaper.py`, lightly modified). Its look-up tables come from Waveshare's example.

## MicroPython: micropython-lib SD card driver

- **Source:** https://github.com/micropython/micropython-lib
  (`micropython/drivers/storage/sdcard/sdcard.py`)
- **Licence:** MIT, Copyright (c) 2013, 2014 micropython-lib contributors
- **Files:** `utilities/sdcard/sdcard.py`

## Russ Hughes: st7789_mpy image converter

- **Source:** https://github.com/russhughes/st7789_mpy (`utils/imgtobitmap.py`)
- **Licence:** MIT, Copyright (c) 2020, 2021, 2022 Russ Hughes, incorporating work
  Copyright (c) 2019 Ivan Belokobylskiy
- **Files:** `utilities/image-tools/imgtobitmap.py`

## MIT licence text

The MIT-licensed components above are distributed under these terms, with each component's own
copyright line:

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
