from adcmonitor import AdcMonitor
from display import Display
from buttons import Buttons
import gc
import uasyncio as asyncio
from time import sleep



class BatteryMonitor:
    def __init__(self):
        self.buttons = Buttons()
        self.display = Display(debug=True)
        self.monitor = AdcMonitor()
        self.running = False
        
        
    async def checker(self, evt):
        evt.wait()
        print("val checker1 -> ", self.buttons.pressedVal)
        print("val -> ", self.buttons.pressedVal)
            
        evt.clear()
        asyncio.sleep_ms(0)
        
    def printSome(self, val):
        print("val? ->", val)
            
    async upAction(self):
        self.monitor.offsetMultiplier += 0.1
        self.display.
            
    async def handleAction(self, val, evt):
        if val == 1:
            
            print("Up button action")
        if val == 2:
            print("Down button action")
        if val == 3:
            print("Start button action")
        if val == 4:
            print("Stop button action")
        if val == 5:
            print("Send button action")
#         switch = {
#             1: self.printSome(val),
#             2: "Down",
#             3: "Start",
#             4: "Stop",
#             5: "Send"
#         }
#         switch.get(val,"Not sure what button was pressed...")

            
    async def run(self):
        
        gc.collect()
        evt = asyncio.Event()
        
        while True:
            buttonPressed = await self.buttons.start(evt)
            self.handleAction(buttonPressed, evt)
            
            evt.set()
            await asyncio.sleep_ms(0)

            
if __name__ == '__main__':
    bm = BatteryMonitor()
    
    try:
        asyncio.run(bm.run())
        
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()

    
        
        
        