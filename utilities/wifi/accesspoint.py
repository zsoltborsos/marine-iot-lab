import uasyncio as asyncio
import network
import binascii
from rp2 import country, const

# ============================================
# WiFi Access Point Configuration
# ============================================
_SSID = const("MyPiCoW")
_PASS = const("<your_password>")  # Change this to your password
# ============================================

# Known MAC addresses for auto-approval
# Add your device MAC addresses here
# Example:
# _PI4B = const('dca632ccb30d')
# _IP7 = const('5a02b2319d81')
_KNOWN_MACS = {
    # Add known devices here:
    # _PI4B: 'PI4B',
    # _IP7: 'Iphone7'
}


class AccessPoint:
    def __init__(self, boost=True):
        # set country for WIFI
        # move this to boot?
        country('UK')
        self.boost = boost
        self.ip = ''

    async def connect(self):
        self.ap = network.WLAN(network.AP_IF)
        self.ap.config(essid=_SSID, password=_PASS)
        if self.boost:
            self.ap.config(pm = 0xa11140)
        self.ap.active(True)
        
        while self.ap.active == False:
            await asyncio.sleep_ms(0)
            pass
        
        print("Access point active")
        self.ip = self.ap.ifconfig()[0]
        print("My IP -> ", self.ip)

    def getConnectedClients(self):
        details = {}
        connected = {}
        connections = self.ap.status('stations')
        details['connections'] = len(connections)
        counter = 0
        if connections:
            #print("con ->", connections)
            mac = bytes(12)
            for i in connections:
                #print("i -> ", i)
                mac = binascii.hexlify(i[0]).decode('utf-8')
                known = _KNOWN_MACS.get(mac)
                if known:
                    connected[counter] = known
                else:
                    connected[counter] = mac
                counter += 1
            
            details['connected'] = connected
            return details
        return []
    

ap = AccessPoint()

try:
    asyncio.run(ap.connect())
except KeyboardInterrupt:
    print("Interrupted...")
finally:
    _ = asyncio.new_event_loop()
