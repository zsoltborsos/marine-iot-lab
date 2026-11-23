from machine import Pin
from time import sleep_ms
from rp2 import const
# from primitives import Pushbutton as pb
import uasyncio as asyncio

# lcd buttons
_BDOWN=15
_BUP=17
_BSTART=2
_BSTOP=3

# extra button 
_BSEND=19

class Buttons:
    def __init__(self, debug = False):
        self.debug = debug
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
    
    async def watcher(self, btn, btnVal, evt=None):
        await evt.wait()
        if not btn.value():
            sleep_ms(20)
            if not btn.value():
                if self.debug:
                    print("Button -> ", self.getVal(btnVal))
                self.pressedVal = btnVal
                evt.clear()
                while not btn.value():
                    sleep_ms(20)
                    
    async def start(self, evt=None):
        while True:
            asyncio.create_task(self.watcher(self.buttonUp, 1, evt))
            asyncio.create_task(self.watcher(self.buttonDown, 2, evt))
            asyncio.create_task(self.watcher(self.buttonStart, 3, evt))
            asyncio.create_task(self.watcher(self.buttonStop, 4, evt))
            asyncio.create_task(self.watcher(self.buttonSend, 5, evt))
            if self.pressedVal != 0:
                tmp = self.pressedVal
                self.pressedVal = 0
                evt.set()
                return tmp
            evt.set()
            await asyncio.sleep_ms(0)
            
    async def test(self):
        evt = asyncio.Event()
        while True:
            await self.start(evt)
            
        
if __name__ == '__main__':
    
    buttons = Buttons(debug=True)

    try:
        asyncio.run(buttons.test())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()
