import socket
import network

# ============================================
# WiFi Access Point Configuration
# ============================================
# Configure your WiFi credentials below
ssid = "MyPiCoW"
password = "<your_password>"  # Change this to your password
# ============================================

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password) 
ap.active(True)

while ap.active == False:
  pass

print("Access point active")
print(ap.ifconfig())
ip = ap.ifconfig()[0]
