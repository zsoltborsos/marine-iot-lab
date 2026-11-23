# Architecture Notes

*Technical architecture documentation for the Battery Monitor System*

---

## System Design Notes

### Network Topology

**Star Network** with E-Paper Dashboard as central hub:
- Dashboard runs WiFi Access Point
- Multiple BatteryMonitor nodes connect as WiFi clients
- Dashboard aggregates and displays all readings

### Power Management

**BatteryMonitor Nodes:**
- Periodic sleep/wake cycle
- Minimal standby consumption (no LEDs on prototype)
- Self-powering from monitored battery source

**Dashboard:**
- E-Paper display for low power consumption
- 20-second refresh target (acceptable for battery monitoring)
- Continuous operation while powered

### Communication Protocol

WiFi-based communication:
- BatteryMonitor nodes push readings to Dashboard
- Dashboard maintains running display of all nodes
- Potential for emergency quick-refresh commands

---

## Known Issues

### WiFi AP Timeout

Pico W Access Point stops working after 5-10 minutes. Requires:
- Investigation with newer MicroPython versions
- Possible workaround: periodic AP restart
- Alternative: Bluetooth mesh network

### Voltage Divider Non-Linearity

Correction factors vary across voltage range:
- 10V (discharged): Different correction than 12V
- 12V (nominal): Baseline calibration point
- 14V+ (charging): Different correction again

Requires multi-point calibration for accuracy.

---

## Future Enhancements

1. **Bluetooth Alternative** - Replace WiFi with Bluetooth if MicroPython support is mature
2. **Multi-Node Protocol** - Robust handling of multiple simultaneous nodes
3. **Emergency Refresh** - Command pathway for immediate readings
4. **Data Logging** - Historical data storage on dashboard
5. **Alert System** - Low/high voltage warnings

---

*This document will be expanded as the project develops*
