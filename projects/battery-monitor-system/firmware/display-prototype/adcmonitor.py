from machine import ADC
from rp2 import const
import uasyncio as asyncio

_ADCIN=const(26)
_ADCREF=const(27)
# voltage divider ratio
# hw has a voltage divider to produce the 1/10th of the input value
_DIVRATE=const(10)
_OFFSET = 1.0

class AdcMonitor:
    def __init__(self, offsetMultiplier = _OFFSET, debug = False):
        self.input = ADC(_ADCIN)
        self.reference = ADC(_ADCREF)
        self.offsetMultiplier = offsetMultiplier
        self.debug = debug
        self.batteryVal = 0
        self.offsetVal = 0
        
    async def readInput(self, evt):
        b = []
        bO = 0
        o = []
        oO = 0
        await evt.wait()
        for i in range(0, 50):
            tmp = self.input.read_u16()
            b.append(tmp)
            bO += tmp
            tmp = self.reference.read_u16()
            o.append(tmp)
            oO += tmp
            await asyncio.sleep_ms(1)
        
        bVal = (bO - min(b) - max(b)) / 48
        oVal = (oO - min(o) - max(o)) / 48

#         bVal = bO / 50
#         oVal = oO / 50
        oResult = bVal - (oVal * self.offsetMultiplier)
        if self.debug:            
            print("B -> ", bVal)
            print("O -> ", oVal)
            print("raw offset -> ", oResult)
            
        evt.clear()
        return [oResult, oVal]

    def calculate(self, val):
        return (val * 3.3 / 65536) * _DIVRATE
    
    async def read(self, evt):
        await evt.wait()
        battery, offset = await self.readInput(evt)
        #if battery and offset:
        self.batteryVal = self.calculate(battery)
        self.offsetVal = self.calculate(offset)
        if self.debug:
            print("ADC read ->", self.batteryVal)
            print("Offset from reference input ->", self.offsetVal)

        evt.clear()
        await asyncio.sleep(0)
        
    async def test(self):
        evt = asyncio.Event()
        evt.set()
        await self.read(evt)
        
        
if __name__ == '__main__':
    myAdc = AdcMonitor(debug=True)
    
    try:
        asyncio.run(myAdc.test())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()
