# Configuration Guide

## WiFi Credentials

This project contains WiFi configuration in the firmware files. **Do not commit real passwords to version control.**

### Dashboard (Access Point)

**File:** `firmware/dashboard/accesspoint.py`

```python
# Configure your WiFi credentials
ssid = "MyPiCoW"
password = "<your_password>"  # Change this to your password
```

### Battery Monitor (Station Mode)

If implementing WiFi client functionality, configure the station credentials in the respective firmware file.

## Best Practices

1. **Never commit real passwords** - Use placeholders like `<your_password>`
2. **Create a `config.py`** for your local credentials and add it to `.gitignore`
3. **Document required settings** without exposing actual values

## Example: Using a config file

Create `config.py` (add to `.gitignore`):

```python
WIFI_SSID = "YourNetworkName"
WIFI_PASSWORD = "YourSecurePassword"
AP_PASSWORD = "YourAPPassword"
```

Then import in your firmware:

```python
from config import WIFI_SSID, WIFI_PASSWORD
```

## Current Configuration Files

| File | Purpose | Contains Real Credentials? |
|------|---------|---------------------------|
| `firmware/dashboard/accesspoint.py` | AP configuration | ❌ Removed (placeholder) |
| `firmware/dashboard/mywifi.py` | Station example | ❌ Placeholder only |
| `firmware/dashboard/server.py` | LED server demo | ❌ Generic placeholders |
