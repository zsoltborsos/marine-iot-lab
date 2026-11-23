from adcmonitor import AdcMonitor
from display import Display
from buttons import Buttons
import gc
import uasyncio as asyncio
# from time import sleep
from primitives import set_global_exception
import micropython
micropython.alloc_emergency_exception_buf(100)


class BatteryMonitor:
    def __init__(self, display=None, memDisplay=False, debug=False):
        set_global_exception()
        self.monitor = AdcMonitor(debug)
        if display:
            self.display = Display(self.monitor.offsetMultiplier, memDisplay)
        else:
            self.display = None
        self.displayOn = display
        self.debug = debug
        self.buttons = Buttons()
        self.running = False

    async def upAction(self, evt):
        self.monitor.offsetMultiplier += 0.1
        if self.displayOn:
            await evt.wait()
            await self.display.updateOffsetMultiplierDisplay(self.monitor.offsetMultiplier, evt)
            evt.clear()
            
    async def downAction(self, evt):
        self.monitor.offsetMultiplier -= 0.1
        if self.displayOn:
            await evt.wait()
            await self.display.updateOffsetMultiplierDisplay(self.monitor.offsetMultiplier, evt)
            evt.clear()
            
    async def startAction(self, evt):
        self.running = True
        if self.displayOn:
            await evt.wait()
            await self.display.updateStatusDisplay("On", evt)
        evt.clear()
    
    async def stopAction(self, evt):
        self.running = False
        if self.displayOn:
            await evt.wait()
            await self.display.updateStatusDisplay("Off", evt)
        evt.clear()
    
    async def readInputs(self, evt):
        while True:
            await evt.wait()
            if self.running:
                await self.monitor.read(evt)
                await asyncio.sleep(0)
                if self.displayOn:
                    if self.monitor.batteryVal:
                        await self.display.updateBatteryDisplay(self.monitor.batteryVal, evt)
                    await asyncio.sleep(0)
                    if self.monitor.offsetVal:
                        await self.display.updateOffsetDisplay(self.monitor.offsetVal, evt)
            evt.clear()
            
    async def readInputs2(self, evt):
        await evt.wait()
        if self.running:
            await self.monitor.read(evt)
            await asyncio.sleep(0)
            if self.displayOn:
                if self.monitor.batteryVal:
                    await self.display.updateBatteryDisplay(self.monitor.batteryVal, evt)
                await asyncio.sleep(0)
                if self.monitor.offsetVal:
                    await self.display.updateOffsetDisplay(self.monitor.offsetVal, evt)
        evt.clear()

    async def handleAction(self, val, evt):
        if val == 1:
            if self.debug:
                print("Up button action")
            await self.upAction(evt)
        if val == 2:
            if self.debug:
                print("Down button action")
            await self.downAction(evt)
        if val == 3:
            if self.debug:
                print("Start button action")
            await self.startAction(evt)
        if val == 4:
            if self.debug:
                print("Stop button action")
            await self.stopAction(evt)
        if val == 5:
            if self.debug:
                print("Send button action")
            
    async def run(self):
        gc.collect()
        evt = asyncio.Event()
        asyncio.create_task(self.readInputs(evt))
        while True:
            buttonPressed = await self.buttons.start(evt)
            if buttonPressed:
                await self.handleAction(buttonPressed, evt)
            evt.set()
            await asyncio.sleep(0)

    async def test(self):
        evt = asyncio.Event()
        evt.set()
        await self.monitor.read(evt)
        

if __name__ == '__main__':
    bm = BatteryMonitor(display=True, memDisplay=True, debug=True)
    try:
        asyncio.run(bm.run())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()
