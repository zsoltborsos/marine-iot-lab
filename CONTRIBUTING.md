# Contributing to Marine IoT Lab

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 How to Contribute

### Reporting Bugs

**Before submitting a bug report:**
- [ ] Check the [existing issues](https://github.com/zsoltborsos/marine-iot-lab/issues) to see if it's already reported
- [ ] Try to reproduce with the latest version
- [ ] Gather information (MicroPython version, Pico model, steps to reproduce)

**Submit a bug report:**
- [ ] Open a [new issue](https://github.com/zsoltborsos/marine-iot-lab/issues/new)
- [ ] Include clear reproduction steps
- [ ] Add expected vs actual behavior
- [ ] Include photos/videos if hardware-related

### Suggesting Features

**Before submitting a feature request:**
- [ ] Check existing feature requests
- [ ] Consider if it fits the project scope (marine/embedded IoT)

**Submit a feature request:**
- [ ] Open a [new issue](https://github.com/zsoltborsos/marine-iot-lab/issues/new)
- [ ] Explain the use case
- [ ] Describe the desired behavior
- [ ] Include examples if possible

### Pull Requests

**Before submitting a PR:**
- [ ] Test on actual hardware (if hardware changes)
- [ ] Update documentation
- [ ] Add comments for complex logic
- [ ] Ensure code follows existing style

**Submit a PR:**
- [ ] Fork the repository
- [ ] Create a feature branch (`git checkout -b feature/amazing-feature`)
- [ ] Make your changes
- [ ] Write clear commit messages
- [ ] Submit pull request with description

---

## 📋 Development Guidelines

### Code Style

**MicroPython Code:**
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable names
- Add docstrings to public functions and classes
- Comment complex logic
- Keep functions small and focused

**Example:**
```python
class BatteryMonitor:
    """
    Battery voltage monitoring system using ADC.
    
    Monitors battery voltage via voltage divider and displays
    readings on LCD or transmits via WiFi.
    
    Attributes:
        offset_multiplier (float): Calibration factor for ADC readings
        debug (bool): Enable debug output
    """
    
    def read_voltage(self):
        """
        Read battery voltage from ADC.
        
        Returns:
            float: Battery voltage in volts
        """
        # Implementation here
        pass
```

### Documentation

**README Files:**
- Every project folder must have a README.md
- Include: overview, features, components, wiring, setup instructions
- Use clear headings and lists
- Include photos/diagrams where helpful

**Code Comments:**
- Explain WHY, not WHAT
- Document non-obvious decisions
- Include warnings for dangerous operations

### Hardware Documentation

**Wiring Diagrams:**
- Use text-based diagrams (ASCII art) or images
- Include pin-by-pin connection tables
- Specify wire colors if relevant

**Component Lists:**
- Include supplier links (preferably UK-based)
- Add part numbers
- Include approximate costs

---

## 🔧 Development Setup

### Hardware Requirements

For development and testing:
- Raspberry Pi Pico (or Pico W)
- USB-C cable
- Project-specific components (see individual project docs)
- Breadboard and jumper wires
- Multimeter (for debugging)

### Software Requirements

- [Thonny IDE](https://thonny.org/) (recommended)
- Or: Python 3.x + command line tools
- Git for version control

---

## 🧪 Testing

### Hardware Testing

**Before submitting hardware-related changes:**
1. Build the circuit as documented
2. Upload the firmware
3. Verify all documented features work
4. Test edge cases (voltage extremes, WiFi dropouts, etc.)
5. Document any deviations from the guide

### Code Testing

**For utility modules:**
1. Test in isolation
2. Test with example code
3. Verify error handling
4. Check memory usage (Pico has limited RAM!)

---

## 📝 Documentation Standards

### README Structure

```markdown
# Project Name

Brief description (1-2 sentences)

## Overview

Longer explanation (2-3 paragraphs)

## Features

- Feature 1
- Feature 2
- Feature 3

## Components

| Component | Quantity | Links |
|-----------|----------|-------|
| Item | 1 | [Link](url) |

## Wiring

### Diagram

[ASCII art or image]

### Pin Connections

| Pico Pin | Component | Pin |
|----------|-----------|-----|
| GPIO X | Component | Pin Y |

## Setup

Step-by-step instructions

## Usage

How to use the project

## Troubleshooting

Common issues and solutions

## License

MIT License
```

### Comment Style

```python
# Single line comment

"""
Multi-line docstring for functions/classes
Explains purpose, parameters, return values
"""

# === Section divider for major code sections ===

# TODO: Add feature X
# FIXME: Fix bug Y
# WARNING: This could crash if Z happens
```

---

## 🚨 Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

**Summary:**
- Be respectful and inclusive
- Focus on constructive feedback
- Welcome newcomers
- No harassment or discrimination

---

## 📧 Getting Help

- **Questions:** Use [GitHub Discussions](https://github.com/zsoltborsos/marine-iot-lab/discussions)
- **Issues:** Use [GitHub Issues](https://github.com/zsoltborsos/marine-iot-lab/issues)
- **Email:** zsoltborsos@users.noreply.github.com

---

## 🎉 Recognition

Contributors will be acknowledged in:
- README.md (Contributors section)
- Release notes
- Documentation

**Thank you for contributing!** 🚢⚓

---

*Last Updated: March 16, 2026*
