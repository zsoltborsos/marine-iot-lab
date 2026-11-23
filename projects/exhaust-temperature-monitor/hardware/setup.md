# Exhaust Temperature Monitor Hardware Setup

## Overview

> **Status: planned design, not built.** The parts, wiring and steps below are the plan and have not been tested.

This design monitors exhaust gas temperature on marine diesel engines using a MAX31855 thermocouple amplifier and K-type thermocouple probe.

## Components Required

### Core Components

| Component | Description | Supplier Links |
|-----------|-------------|----------------|
| **Raspberry Pi Pico** | RP2040 microcontroller | [Pimoroni](https://shop.pimoroni.com/products/raspberry-pi-pico), [The Pi Hut](https://thepihut.com/products/raspberry-pi-pico) |
| **MAX31855 Module** | Thermocouple amplifier with cold junction compensation | [Adafruit](https://www.adafruit.com/product/269), [SparkFun](https://www.sparkfun.com/products/13269) |
| **K-Type Thermocouple** | High-temperature probe (0-800°C range) | [RS Components](https://uk.rs-online.com), [CPC/Farnell](https://cpc.farnell.com) |
| **OLED Display** (optional) | 0.96" I2C OLED for local display | [Pimoroni](https://shop.pimoroni.com/products/0-96-oled-breakout) |
| **Buzzer** (optional) | 5V active buzzer for alarms | [CPC](https://cpc.farnell.com) |
| **Breadboard/PCB** | For connections | Any electronics supplier |
| **Jumper Wires** | F/F or F/M | Any electronics supplier |

### Thermocouple Probe Specifications

**Critical Requirements:**
- **Type**: K-type thermocouple
- **Temperature Range**: 0°C to 800°C minimum
- **Sheath Material**: Stainless steel (marine environment)
- **Probe Length**: 50-100mm (to reach exhaust)
- **Connector**: Standard thermocouple mini-connector or bare wires

**Recommended:**
- Industrial K-type with M6 or M8 threaded fitting
- High-temperature silicone cable
- Grounded junction for faster response

### Optional Components

| Component | Purpose | Notes |
|-----------|---------|-------|
| **Enclosure** | Weatherproof housing | IP65 or better |
| **Terminal Blocks** | Secure connections | 2-pin screw terminals |
| **Heat Shrink** | Wire protection | Marine grade |
| **Mounting Bracket** | Thermocouple mount | 3D printed or metal |

## Wiring Diagram

### Pico to MAX31855

```
┌─────────────────┐          ┌──────────────────────┐
│  Raspberry Pi   │          │  MAX31855 Module     │
│  Pico           │          │                      │
│                 │          │                      │
│  GPIO 2  (SCK)  ├─────────►│  CLK                 │
│  GPIO 4  (MISO) ◄─────────┤  DO                  │
│  GPIO 5  (CS)   ├─────────►│  CS                  │
│  3.3V (OUT)     ├─────────►│  VCC                 │
│  GND            ├─────────►│  GND                 │
│                 │          │                      │
│                 │          │  T+  ────► Thermocouple (+)
│                 │          │  T-  ────► Thermocouple (-)
└─────────────────┘          └──────────────────────┘
```

**Note:** The MAX31855 uses SPI only — it has no I2C interface. It is read-only (no MOSI/DI pin). CS is driven low by software before each read.

### Optional: OLED Display

```
┌─────────────────┐          ┌──────────────────────┐
│  Raspberry Pi   │          │  0.96" OLED          │
│  Pico           │          │  (I2C)               │
│                 │          │                      │
│  GPIO 26 (GP26) ├─────────►│  SDA                 │
│  GPIO 27 (GP27) ├─────────►│  SCL                 │
│  3.3V (OUT)     ├─────────►│  VCC                 │
│  GND            ├─────────►│  GND                 │
└─────────────────┘          └──────────────────────┘
```

**Note:** OLED uses I2C (separate from the MAX31855 SPI interface).

### Optional: Buzzer

```
┌─────────────────┐          ┌──────────────────────┐
│  Raspberry Pi   │          │  Active Buzzer       │
│  Pico           │          │                      │
│                 │          │                      │
│  GPIO 15 (GP15) ├─────────►│  + (Positive)        │
│  GND            ├─────────►│  - (Negative)        │
└─────────────────┘          └──────────────────────┘
```

## Complete Pin Mapping

| Function    | Pico Pin | GPIO | MAX31855 | OLED | Buzzer |
|-------------|----------|------|----------|------|--------|
| SPI SCK     | Pin 4    | 2    | ✓        | -    | -      |
| SPI MISO    | Pin 6    | 4    | ✓ (DO)   | -    | -      |
| SPI CS      | Pin 7    | 5    | ✓        | -    | -      |
| I2C SDA     | Pin 31   | 26   | -        | ✓    | -      |
| I2C SCL     | Pin 32   | 27   | -        | ✓    | -      |
| Buzzer      | Pin 20   | 15   | -        | -    | ✓      |
| 3.3V        | Pin 36   | -    | ✓        | ✓    | -      |
| GND         | Pin 38   | -    | ✓        | ✓    | ✓      |

## Thermocouple Mounting

### Mounting Options

#### 1. Exhaust Elbow (Recommended)

**Best Location:** After raw water cooling point

**Steps:**
1. Drill and tap exhaust elbow for thermocouple fitting
2. Use high-temperature anti-seize compound
3. Ensure good thermal contact
4. Route wiring away from hot surfaces

**Temperature Range:** 200-400°C (normal operation)

#### 2. Exhaust Riser

**Alternative Location:** Vertical section of riser

**Steps:**
1. Similar to elbow mounting
2. Ensure probe doesn't obstruct exhaust flow
3. Consider accessibility for maintenance

#### 3. Clamp-On Sensor (Easiest, Less Accurate)

**External Mounting:** Strap thermocouple to outside of exhaust

**Pros:**
- No drilling required
- Easy to install
- Non-invasive

**Cons:**
- Slower response time
- Lower accuracy
- Affected by ambient temperature

### Mounting Hardware

**For Threaded Installation:**
- M6 or M8 thermocouple boss (weld-on or compression fit)
- High-temperature gasket or sealant
- Thermocouple with matching thread

**For Clamp-On:**
- Stainless steel hose clamp
- Thermal paste for better contact
- Heat-resistant mounting bracket

## Enclosure

### Requirements

- **IP Rating:** IP65 minimum (splash proof)
- **Material:** Plastic or stainless steel
- **Size:** Large enough for Pico + MAX31855 + wiring
- **Cable Glands:** For thermocouple and power cables

### Candidate Enclosures

No enclosure has been chosen yet. Look for an IP65 (or better) ABS or polycarbonate box from a supplier such as [CPC](https://cpc.farnell.com), [RS Components](https://uk.rs-online.com) or [DigiKey](https://www.digikey.co.uk), sized for the Pico, the MAX31855 module and cable glands.

### Cable Entry

**Use cable glands for:**
- Thermocouple probe wire
- Power cable
- Optional: Display/buzzer wires

**Sealing:**
- Use marine-grade silicone sealant
- Heat shrink on all wire entries
- Drip loops on external cables

## Power Supply

### Input Requirements

- **Voltage:** 12V DC (marine system)
- **Current:** ~100mA (Pico + peripherals)
- **Protection:** Fuse (500mA recommended)

### Regulation

**Important:** Pico VBUS (pin 40) is the 5V USB power rail. The internal regulator accepts a maximum of ~5.5V on VBUS. **Do NOT connect 12V directly to VBUS — this will destroy the Pico.**

For a 12V marine system an external 5V regulator is required (e.g. L7805 or similar). This is the same approach used by the Battery Monitor Voltage Sentinel circuit in this repo.

**Options:**

1. **5V USB power bank or USB adapter:**
   - Cleanest option
   - USB cable to Pico micro-USB port

2. **External 5V regulator (L7805) from 12V:**
   - L7805 regulates 12V → 5V
   - Connect 5V output to Pico VBUS (Pin 40)
   - Add 100nF capacitors on input and output of L7805
   - Can also power buzzer/display from same regulated 5V

### Wiring for 12V Marine System

```
Boat 12V System
       │
       ├──► Fuse (500mA)
       │
       └──► L7805 (IN)
                │
                ├──► L7805 (OUT) ──► Pico VBUS (Pin 40)
                │
                └──► GND (Pin 38)
```

## Assembly Steps

### 1. Prepare Components

- [ ] Cut header pins to size
- [ ] Label wires for identification
- [ ] Test MAX31855 with example code
- [ ] Prepare thermocouple leads

### 2. Wire MAX31855

- [ ] Connect SPI lines (CLK, DO, CS)
- [ ] Connect power (3.3V, GND)
- [ ] Connect thermocouple (T+, T-)
- [ ] Verify connections with multimeter

### 3. Add Optional Components

- [ ] Wire OLED display (if using)
- [ ] Wire buzzer (if using)
- [ ] Add current-limiting resistor for buzzer

### 4. Test on Bench

- [ ] Connect USB power
- [ ] Run test script
- [ ] Verify temperature readings
- [ ] Test alarm thresholds

### 5. Install in Enclosure

- [ ] Mount Pico on standoffs
- [ ] Secure MAX31855 module
- [ ] Route cables through glands
- [ ] Seal all entries with silicone

### 6. Install on Boat

- [ ] Mount thermocouple on exhaust
- [ ] Route wiring to enclosure location
- [ ] Connect to 12V system (fused!)
- [ ] Test operation

## Testing & Calibration

### Bench Testing

**Ice Water Test (0°C):**
1. Immerse thermocouple tip in ice water
2. Reading should be 0°C ±2°C
3. Adjust offset if needed

**Boiling Water Test (100°C):**
1. Immerse in boiling water (at sea level)
2. Reading should be 100°C ±2°C
3. Verify linearity

### On-Engine Testing

**Cold Start:**
1. Record ambient temperature
2. Start engine
3. Monitor temperature rise

**Warm-Up:**
1. Track temperature over 10-15 minutes
2. Note stable operating temperature
3. Verify within normal range (200-400°C)

**Under Load:**
1. Test at various RPM
2. Monitor for temperature spikes
3. Verify alarm thresholds

### Temperature Thresholds

**Typical Diesel Engine:**

| Condition | Temperature | Action |
|-----------|-------------|--------|
| Cold | <100°C | Normal (warming up) |
| Normal | 200-400°C | OK |
| Warning | 400-500°C | Caution |
| Critical | >500°C | Alarm! |
| Danger | >600°C | Shut down! |

**⚠️ Important:** Consult your engine manual for specific thresholds!

## Troubleshooting

### No Reading / Sensor Error

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| "Something went wrong" | SPI wiring | Check CLK/DO/CS connections |
| Reading 0 or very low | Thermocouple disconnected | Check T+/T- connections |
| Random values | Loose connections | Resolder joints |
| Always max value | Short circuit | Check for shorts |

### Inaccurate Readings

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Reading too high | Poor calibration | Recalibrate |
| Reading too low | Bad thermal contact | Improve mounting |
| Slow response | Probe location | Move to better location |
| Fluctuating | Electrical noise | Add filtering capacitor |

### SPI Issues

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| No data / all zeros | Wrong pins | Verify GPIO 2 (CLK), 4 (DO), 5 (CS) |
| Always reads fault | CS not pulled low | Check CS wiring and Pin.OUT mode |
| Intermittent | Long wires | Shorten SPI cables |

## Safety Warnings

⚠️ **High Temperature:**
- Exhaust systems get extremely hot (500°C+)
- Allow engine to cool before installation
- Use heat-resistant gloves and tools
- Never touch hot exhaust components

⚠️ **Marine Environment:**
- Use marine-grade components
- Seal all enclosures properly
- Protect wiring from chafing
- Use tinned copper wire (corrosion resistant)

⚠️ **Engine Safety:**
- This is a monitoring device only
- Not a replacement for proper maintenance
- Don't rely solely on this device
- Have backup temperature monitoring

⚠️ **Electrical:**
- Fuse all 12V connections
- Use proper wire gauge
- Include reverse polarity protection
- Test on bench before installing

## Next Steps

Once hardware is assembled:

1. Upload firmware to Pico
2. Test with known temperature source
3. Install on engine
4. Set appropriate alarm thresholds
5. Monitor and log data

See [Firmware README](../firmware/README.md) for software setup.

## Related Projects

- **Battery Monitor System** - Another marine monitoring project
- **Utilities** - Reusable MicroPython modules

## References

- [MAX31855 Datasheet](https://www.maximintegrated.com/en/products/analog/sensors-and-sensor-interface/MAX31855.html)
- [K-Type Thermocouples](https://www.omega.co.uk/prodinfo/thermocouples.html)
- [Marine Electrical Standards](https://www.abycinc.org/)
