from machine import Pin
from time import sleep_ms
from rp2 import const
# from primitives import Pushbutton as pb
import uasyncio as asyncio
from primitives import set_global_exception
import micropython
micropython.alloc_emergency_exception_buf(100)

# lcd buttons
_BDOWN=15
_BUP=17
_BSTART=2
_BSTOP=3

# extra button 
_BSEND=19

class Buttons:
    def __init__(self):
        p = Pin
        self.buttonDown = p(_BDOWN, p.IN, p.PULL_UP)
        self.buttonUp = p(_BUP, p.IN, p.PULL_UP)
        self.buttonStart = p(_BSTART, p.IN, p.PULL_UP)
        self.buttonStop = p(_BSTOP, p.IN, p.PULL_UP)
        self.buttonSend = p(_BSEND, p.IN, p.PULL_UP)
        self.pressedVal = 0
    
    def getVal(self, val):
        switch={
            1 : "Up",
            2 : "Down",
            3 : "Start",
            4 : "Stop",
            5 : "Send"
           }
        return switch.get(val,"Not sure what button was pressed...")
    
    async def watcher(self, btn, btnVal, evt = asyncio.Event()):
        await evt.wait()
        if not btn.value():
            sleep_ms(20)
            if not btn.value():
                print("Button -> ", self.getVal(btnVal))
                self.pressedVal = btnVal
                evt.clear()
                while not btn.value():
                    sleep_ms(20)
                    
    async def start(self, evt = asyncio.Event()):
        while True:
            asyncio.create_task(self.watcher(self.buttonUp, 1, evt))
            asyncio.create_task(self.watcher(self.buttonDown, 2, evt))
            asyncio.create_task(self.watcher(self.buttonStart, 3, evt))
            asyncio.create_task(self.watcher(self.buttonStop, 4, evt))
            asyncio.create_task(self.watcher(self.buttonSend, 5, evt))
            if self.pressedVal != 0:
                print("yeey -> ", self.pressedVal)
                tmp = self.pressedVal
                self.pressedVal = 0
                evt.set()
                return tmp
            evt.set()
            await asyncio.sleep_ms(0)
            
        
    def clearVal(self):
        self.pressedVal = 0
        
if __name__ == '__main__':
    
    buttons = Buttons()

    try:
        #evt = asyncio.Event()
        asyncio.run(buttons.start())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()
