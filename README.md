# Marine IoT Lab

🚢 **MicroPython projects for marine electronics and embedded systems**

A collection of open-source IoT projects designed for marine environments, built with Raspberry Pi Pico and MicroPython.

---

## 📦 Projects

### 🔋 Battery Monitor System

**Status:** 🚧 Partly built: the display prototype works; Wi-Fi reporting is planned

A battery voltage monitor for a boat, planned as several monitoring nodes reporting to an e-paper dashboard.

**Built:**
- Display prototype: a standalone voltmeter with a colour LCD and button calibration
- Voltage Sentinel circuit (regulator and voltage divider)
- Dashboard prototype: a Wi-Fi access point and HTTP server that shows received messages on a 3.7" e-paper display

**Planned:**
- Screenless nodes (alternator, fridge, solar) sending readings over Wi-Fi
- Dashboard handling of readings from several nodes
- Deep sleep between readings

**Estimated cost:** ~£50 for the planned system (3 nodes + dashboard)

**[→ View Project](projects/battery-monitor-system/)**

---

### 🌡️ Exhaust Temperature Monitor

**Status:** 📐 Design and plan, not built

A planned early warning system for a marine diesel engine, using thermocouple temperature sensing. The repository holds the design notes and an untested driver sketch; no hardware has been built.

**Planned features:**
- MAX31855 thermocouple amplifier
- K-type thermocouple probe
- Temperature alarms
- Data logging (optional)
- Marine-grade enclosure

**Estimated cost:** ~£25

**[→ View Project](projects/exhaust-temperature-monitor/)**

**The Story:** The plan was inspired by a real incident at sea. While crewing on a passage from Liverpool to Penzance, the engine overheated in the dark waters around Land's End due to a loose raw water filter. The problem was discovered only because the captain's bunk was next to the engine compartment - from the helm, there was no indication anything was wrong.

---

### 🖼️ E-Paper Photo Album

**Status:** ✅ Working prototype

Personalized e-paper photo frame - perfect gift project!

**Features:**
- 3.7" e-paper display (400×280)
- SD card storage
- Auto-cycling (5 min intervals)
- Freeze-frame mode
- Ultra-low power consumption
- Rechargeable battery option

**Cost:** ~£35

**[→ View Project](projects/epaper-photo-album/)**

---

### 🎨 NeoPixel Display

**Status:** ✅ Working prototype

20×11 LED matrix (220 LEDs) with web interface and visual programmer.

**Features:**
- Web-based pattern designer
- IR remote control
- Multiple built-in effects
- Custom pattern upload
- Real-time control

**Cost:** ~£60

**[→ View Project](projects/neopixel-display/)**

---

## 🛠️ Utilities

Shared utility modules used across all projects:

- **[WiFi](utilities/wifi/)** - Station and Access Point modes
- **[SD Card](utilities/sdcard/)** - SPI interface and file operations
- **[Buttons](utilities/buttons/)** - Debounced button handling
- **[UART](utilities/uart/)** - Serial communication
- **[Displays](utilities/displays/)** - SPI display drivers
- **[Image Tools](utilities/image-tools/)** - Image to bitmap conversion

---

## 🚀 Quick Start

### Prerequisites

- **Hardware:**
  - Raspberry Pi Pico (or Pico W for WiFi projects)
  - USB-C cable
  - Components for specific project (see individual project docs)

- **Software:**
  - [Thonny IDE](https://thonny.org/) (recommended for beginners)
  - Or any text editor + command line

### Install MicroPython

1. **Download MicroPython:**
   - Visit [micropython.org/download](https://micropython.org/download/PICO/)
   - Download the UF2 file for Raspberry Pi Pico

2. **Flash to Pico:**
   - Hold the BOOTSEL button on Pico
   - Connect USB cable to computer
   - Release BOOTSEL when "RPI-RP2" drive appears
   - Drag and drop the UF2 file onto the drive
   - Pico will reboot automatically

3. **Verify Installation:**
   - Open Thonny IDE
   - Select "MicroPython (Raspberry Pi Pico)" as interpreter
   - Type `print("Hello, Marine IoT!")` in the shell
   - You should see the output

### First Project

**Recommended starting order:**

1. **NeoPixel Display** - Easiest, instant visual feedback
2. **E-Paper Photo Album** - Great gift project
3. **Battery Monitor** - Most useful on the boat
4. **Exhaust Monitor** - A design to build from; not yet built or tested

---

## ⚠️ Safety

### Marine Electrical Safety

⚠️ **Working with 12V marine systems requires caution:**

1. **Always fuse connections** - Use appropriate fuses for wire gauge
2. **Use marine-grade components** - Salt water corrodes regular electronics
3. **Waterproof enclosures** - IP65 rating minimum for deck mounting
4. **Proper wire gauge** - Don't skimp on power cables
5. **Heat shrink everything** - Protect from moisture and corrosion
6. **Test on bench first** - Never install untested electronics on your boat

### Disclaimer

These projects are shared for educational purposes and come with no warranty; see the [LICENSE](LICENSE). Use at your own risk.

**Important:** Marine electronics failures can have serious consequences including:
- Battery damage
- Fire hazard
- Equipment failure at sea

Always have backup systems and proper marine safety equipment.

---

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

### Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Share your modifications
- 📸 Add photos of your builds

### Code of Conduct

Please be respectful and inclusive. See our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📄 License

**MIT License** - See [LICENSE](LICENSE) file for details.

**Summary:** You can use, modify, and share these projects freely. The software comes with no warranty.

**Third-party code:** Several projects bundle code from other authors under their own licences (mostly MIT). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/zsoltborsos/marine-iot-lab/issues)
- **Discussions:** [GitHub Discussions](https://github.com/zsoltborsos/marine-iot-lab/discussions)
- **Portfolio:** [zsoltborsos.net](https://zsoltborsos.net)
- **GitHub:** [@zsoltborsos](https://github.com/zsoltborsos)

---

## 🙏 Acknowledgments

### Libraries & Code Sources

- [MicroPython](https://micropython.org/) - The foundation of all these projects
- [russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy) - Image converter tool (imgtobitmap.py)
- [peterhinch/micropython-async](https://github.com/peterhinch/micropython-async) - Async utilities and primitives
- [peterhinch/micropython-nano-gui](https://github.com/peterhinch/micropython-nano-gui) - NanoGUI display framework, drivers and fonts
- [waveshare/Pico_ePaper_Code](https://github.com/waveshare/Pico_ePaper_Code) - Pico e-Paper 3.7 driver
- [micropython/micropython-lib](https://github.com/micropython/micropython-lib) - SD card driver

**Note**: Many projects use peterhinch's excellent MicroPython libraries extensively. Copyright and licence details are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and in the individual source files.

---

## 🗺️ Roadmap

Nothing below is built yet.

### Next

- [ ] Build and bench-test the exhaust temperature monitor
- [ ] Wi-Fi reporting from battery monitor nodes to the dashboard
- [ ] Mobile app for Battery Monitor System
- [ ] 3D printable enclosures for all projects
- [ ] Video tutorials for each project
- [ ] Kit availability (pre-built components)

### Under Consideration

- [ ] NMEA 2000 integration
- [ ] Solar charge controller monitoring
- [ ] Water tank level monitoring
- [ ] Engine hours tracker
- [ ] Anchor alarm system

---

## 📧 Contact

**Zsolt Borsos**
- GitHub: [@zsoltborsos](https://github.com/zsoltborsos)
- Portfolio: [zsoltborsos.net](https://zsoltborsos.net)

---

**Made with ⚓ and ☕ by Zsolt Borsos**

*Last Updated: November 2026*
