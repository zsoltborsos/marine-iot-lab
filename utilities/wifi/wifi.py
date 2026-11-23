import network
from rp2 import const, country
from time import sleep

# ============================================
# WiFi Station Configuration
# ============================================
_SSID = const('MyPicoW')
_PASSWORD = const('<your_password>')  # Change this to your password
# ============================================
_RETRY = const(10)

# 0 : STAT_IDLE – no connection and no activity,
# 1 : STAT_CONNECTING – connecting in progress,
# -3: STAT_WRONG_PASSWORD – failed due to incorrect password,
# -2: STAT_NO_AP_FOUND – failed because no access point replied,
# -1: STAT_CONNECT_FAIL – failed due to other problems,
# 3 : STAT_GOT_IP – connection successful.

class Wifi:
    def __init__(self, ssid=_SSID, password=_PASSWORD):
        self.wlan = network.WLAN(network.STA_IF)
        country('UK')
        self.wlan.active(True)
        self.wlan.config(pm = 0xa11140)
        print(self.wlan.scan())
        self.wlan.connect(ssid, password)
        self.connected = False
        self.connect(self.wlan)

    def connect(self, wlan):
        # Wait for connect or fail
        max_wait = _RETRY
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')
            sleep(1)
            
        # Handle connection error
        print("wlan status -> ", wlan.status())
        if wlan.status() != 3:
            #print('network connection failed --- did it?')
            print('Network connection failed with status %s' % (wlan.status()))
            self.connected = False
        else:
            print('connected')
            self.connected = True
            print('Connected. My IP is: %s' % wlan.ifconfig()[0])
        
#         status = wlan.ifconfig()
#         print( 'ip = ' + status[0] )

    def checkStatus(self, wlan):
        print('Connected -> %s', wlan.isconnected())
    
if __name__ == '__main__':
    wifi = Wifi()
#     try:
#         asyncio.run(http.test())
#     except KeyboardInterrupt:
#         print('Interrupted')
#     finally:
#         _ = asyncio.new_event_loop()