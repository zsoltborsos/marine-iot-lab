# Voltage Sentinel - Component List & Build Guide

## Overview

Voltage Sentinel is a custom voltage regulator and divider circuit for monitoring marine battery voltage with a Raspberry Pi Pico.

## What It Does

1. **Regulates** 8-16V input down to 5V for the Pico
2. **Divides** battery voltage to ADC-safe levels (0-3.3V range)

## Complete Component List

### Voltage Regulator Section

| Component | Value | Quantity | Purpose | UK Supplier Links |
|-----------|-------|----------|---------|-------------------|
| **Voltage Regulator** | L7805CV | 1 | 5V regulation | [Pimoroni](https://shop.pimoroni.com/products/l7805cv-voltage-regulator), [CPC](https://cpc.farnell.com/cpc/stmicroelectronics-l7805cv/linear-voltage-regulator-5v-1-5a-to-220-3/l/REG10079) |
| **Schottky Diode** | 1N5819 | 1 | Reverse polarity protection | [Rapid](https://www.rapidonline.com/1n5819-40v-1a-schottky-diode-47-0116), [CPC](https://cpc.farnell.com/multicomp-pro/1n5819/schottky-rectifier-40v-1a-do/di/3914966) |
| **Electrolytic Capacitor** | 22µF 25V | 1 | Input filtering | [Pimoroni](https://shop.pimoroni.com/products/electrolytic-capacitor-pack), [CPC](https://cpc.farnell.com/multicomp-pro/mceel025v226m5x11/cap-22-f-25v-20/dp/CA07676) |
| **Ceramic Capacitor** | 100nF (0.1µF) | 2 | High-frequency filtering | [Pimoroni](https://shop.pimoroni.com/products/ceramic-capacitor-pack), [Rapid](https://www.rapidonline.com/100nf-50v-multilayer-ceramic-capacitor-31-0062) |
| **Electrolytic Capacitor** | 10µF 16V | 1 | Output filtering | [CPC](https://cpc.farnell.com/multicomp-pro/mceel016v106m5x11/cap-10-f-16v-20/dp/CA07668) |

### Voltage Divider Section

| Component | Value | Quantity | Purpose | UK Supplier Links |
|-----------|-------|----------|---------|-------------------|
| **Resistor** | 2.2kΩ 0.25W | 1 | Voltage divider (R2) | [Pimoroni](https://shop.pimoroni.com/products/1-4w-resistor-pack), [Rapid](https://www.rapidonline.com/2k2-0-25w-1-metal-film-resistor-66-0604) |
| **Resistor** | 6.8kΩ 0.25W | 1 | Voltage divider (R1 part) | [Rapid](https://www.rapidonline.com/6k8-0-25w-1-metal-film-resistor-66-0828) |
| **Resistor** | 1kΩ 0.25W | 1 | Current limiting | [Rapid](https://www.rapidonline.com/1k-0-25w-1-metal-film-resistor-66-0252) |
| **Trimmer Potentiometer** | 10kΩ Multi-turn | 1 | Fine calibration | [Pimoroni](https://shop.pimoroni.com/products/10k-trimmer-potentiometer), [CPC](https://cpc.farnell.com/multicomp-pro/3362p-1-103lf/trimmer-pot-10k-11-turn-thru/dp/POT00039) |
| **Electrolytic Capacitor** | 10µF 16V | 1 | Divider filtering | [CPC](https://cpc.farnell.com/multicomp-pro/mceel016v106m5x11/cap-10-f-16v-20/dp/CA07668) |
| **Ceramic Capacitor** | 10nF (0.01µF) | 1 | High-frequency filtering | [Rapid](https://www.rapidonline.com/10nf-50v-multilayer-ceramic-capacitor-31-0054) |

### Additional Components

| Component | Value | Quantity | Purpose | UK Supplier Links |
|-----------|-------|----------|---------|-------------------|
| **Terminal Blocks** | 2-pin screw | 2 | Input/output connections | [Pimoroni](https://shop.pimoroni.com/products/screw-terminal-block-breakout), [Rapid](https://www.rapidonline.com/2-way-pcb-screw-terminal-block-82-0232) |
| **PCB** | Perfboard/Veroboard | 1 | Circuit construction | [Pimoroni](https://shop.pimoroni.com/products/solderable-breadboard), [Rapid](https://www.rapidonline.com/95x36mm-stripboard-85-0020) |
| **Header Pins** | 2.54mm male | 6 | Pico connection | [Pimoroni](https://shop.pimoroni.com/products/break-away-headers), [Rapid](https://www.rapidonline.com/40-way-2-54mm-single-row-pin-header-13-0396) |

### Tools Required

- Soldering iron and solder
- Wire cutters/strippers
- Multimeter
- Breadboard (for testing)
- Drill (for enclosure mounting)

## Circuit Theory

### Voltage Divider Calculation

The voltage divider reduces the battery voltage to ADC-safe levels:

```
V_out = V_in × (R2 / (R1 + R2))
```

**For our values:**
- R1 = 9kΩ (6.8kΩ + 2.2kΩ in series, adjusted with trimmer)
- R2 = 1kΩ

**Example:**
- At 12V input: V_out = 12 × (1k / 10k) = 1.2V
- At 14.4V input: V_out = 14.4 × (1k / 10k) = 1.44V
- At 16V max: V_out = 16 × (1k / 10k) = 1.6V (safe for Pico ADC)

### Why These Values?

**Input Range:** 8-16V (marine battery system)
- **8V** (discharged): V_out = 0.8V
- **14.4V** (charging): V_out = 1.44V
- **16V** (max safe): V_out = 1.6V

All values are well within the Pico's 0-3.3V ADC range.

### Power Dissipation

**Resistor Power Rating:**
```
P = V² / R = 16² / 10000 = 0.0256W
```

Standard 0.25W resistors are more than adequate (10x safety margin).

## Wiring Diagram (Text)

```
12V Marine System
       │
       ├──► Fuse (1A recommended)
       │
       ▼
    ┌──────┐
    │ IN5819│ Anode → Input, Cathode → Circuit
    └──────┘
       │
       ├──► C1 (22µF) → GND
       │
       ▼
    ┌────────┐
    │ L7805  │ IN → Input, OUT → 5V, GND → Ground
    └────────┘
       │
       ├──► C2 (100nF) → GND (close to regulator)
       ├──► C3 (10µF) → GND
       │
       ▼
    +5V Rail (for Pico VBUS)
    
    ──────────────────────────────
    
Battery Voltage (same 12V input)
       │
       ├──► R1 (9kΩ total)
       │
       ├──► Trimmer (10kΩ) → for fine adjustment
       │
       ├──► R2 (1kΩ) → GND
       │
       ├──► C4 (10µF) → GND (parallel with R2)
       ├──► C5 (10nF) → GND (parallel with R2)
       │
       ▼
    V_out → Pico GPIO 26 (ADC)
```

## Assembly Instructions

### Step 1: Plan Layout

1. Place components on perfboard
2. Ensure enough space for terminal blocks
3. Position Pico headers at edge
4. Mark hole locations

### Step 2: Solder Components

**Order:**
1. Start with lowest components (resistors)
2. Add capacitors
3. Mount voltage regulator (vertical or horizontal)
4. Add terminal blocks
5. Solder header pins for Pico

**Tips:**
- Keep high-voltage side away from low-voltage
- Place filtering capacitors close to regulator
- Use thick traces for power lines

### Step 3: Check Connections

**Before applying power:**

1. **Visual Inspection:**
   - [ ] All components oriented correctly
   - [ ] No solder bridges
   - [ ] Good solder joints

2. **Multimeter Tests:**
   - [ ] Input to GND: No short
   - [ ] 5V rail to GND: No short
   - [ ] V_out to GND: No short
   - [ ] Continuity on ground plane

### Step 4: Initial Test

**Bench Testing:**

1. **Power Supply Test:**
   - Connect 12V to input
   - Measure 5V output (should be 4.9-5.1V)
   - If wrong, check regulator wiring

2. **Voltage Divider Test:**
   - Measure input voltage (V_in)
   - Measure V_out (should be V_in × 0.1)
   - Adjust trimmer if needed

3. **Connect Pico:**
   - Power off
   - Connect to Pico headers
   - Power on
   - Verify Pico boots normally

### Step 5: Calibration

**Multi-Point Calibration:**

1. **Set Known Input Voltages:**
   - 10.0V → Adjust trimmer until ADC reads correctly
   - 12.0V → Verify reading
   - 14.4V → Verify reading

2. **Software Calibration:**
   - Note actual vs. measured values
   - Update offset and multiplier in firmware
   - See [Calibration Guide](../../firmware/README.md#calibration)

**Example Calibration Table:**

| Input Voltage | ADC Reading | Correction Factor |
|---------------|-------------|-------------------|
| 10.0V | 9.8V | 1.02 |
| 12.0V | 11.9V | 1.01 |
| 14.4V | 14.1V | 1.02 |

## Enclosure Mounting

### Recommended Enclosure

| Product | Size | Supplier |
|---------|------|----------|
| Hammond 1551MBK | 120×80×55mm | [CPC](https://cpc.farnell.com/hammond/1551mbk/enclosure-abs-black-120x/dp/EN00006638) |
| RS Pro ABS | 100×68×50mm | [RS](https://uk.rs-online.com/web/p/abs-enclosures/1245706) |

### Mounting Holes

**Drill for:**
- 2× cable glands (input/output)
- 4× mounting screws (PCB standoffs)
- Optional: ventilation holes

### Cable Glands

| Size | For | Supplier |
|------|-----|----------|
| M12 | Power cables | [RS](https://uk.rs-online.com) |
| M16 | Thermocouple (if used) | [RS](https://uk.rs-online.com) |

## Troubleshooting

### No 5V Output

| Symptom | Check | Solution |
|---------|-------|----------|
| 0V at 5V rail | Input voltage | Verify 12V at input |
| 0V at 5V rail | Diode orientation | Cathode (stripe) toward circuit |
| 0V at 5V rail | Regulator | Check L7805 wiring (IN, OUT, GND) |

### Wrong Output Voltage

| Symptom | Check | Solution |
|---------|-------|----------|
| <4.5V or >5.5V | Input voltage | Should be >7V for regulation |
| <4.5V or >5.5V | Regulator | May be faulty, replace |
| Unstable | Capacitors | Check C2, C3 are soldered |

### ADC Reading Incorrect

| Symptom | Check | Solution |
|---------|-------|----------|
| Always 0V | Divider wiring | Check R1, R2 connections |
| Always 3.3V | Short circuit | Check for solder bridges |
| Wrong values | Resistor values | Verify with multimeter |
| Noisy reading | Capacitors | Add/check C4, C5 |

## Safety

⚠️ **High Current:**
- Fuse input at 1A minimum
- Use appropriate wire gauge (18-20 AWG)
- Secure all connections

⚠️ **Heat:**
- L7805 can get warm under load
- Provide ventilation or heatsink if needed
- Don't touch when powered

⚠️ **Marine Environment:**
- Use conformal coating on PCB
- Seal enclosure properly (IP65+)
- Use tinned copper wire

## Cost Estimate

| Category | Cost (GBP) |
|----------|------------|
| Regulator components | £3-5 |
| Divider components | £2-3 |
| PCB & connectors | £3-5 |
| Enclosure | £5-10 |
| **Total** | **£13-23** |

**Compare to:** Commercial battery monitors £50-150

**You save:** £30-130 by building yourself!

## Next Steps

1. Build the circuit
2. Test on bench
3. Calibrate with known voltages
4. Install on boat
5. Connect to Battery Monitor System

See [Battery Monitor Firmware](../../firmware/README.md) for software setup.

## Photo Documentation

**Add your voltage divider photo here:**

Suggested photos:
- Top view of assembled PCB
- Bottom view showing solder joints
- Installed in enclosure
- Connected to battery system
- Display showing voltage reading

Simply place your photos in the `images/` folder and reference them here.

---

**Version:** 1.0  
**Last Updated:** March 16, 2026
