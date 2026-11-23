from machine import ADC
from rp2 import const
import uasyncio as asyncio
import time

_ADCIN=const(26)
_ADCREF=const(27)
# voltage divider ratio
# hw has a voltage divider to produce the 1/10th value
_DIVRATE=const(10)

class AdcMonitor:
    def __init__(self, offsetMultiplier = 1.0):
        self.input = ADC(_ADCIN)
        self.reference = ADC(_ADCREF)
        self.offsetMultiplier = offsetMultiplier
        
    def readInput(self):
        b = []
        bO = 0
        o = []
        oO = 0
        for i in range(0, 50):
            tmp = self.input.read_u16()
            b.append(tmp)
            bO += tmp
            tmp = self.reference.read_u16()
            o.append(tmp)
            oO += tmp
            time.sleep_ms(1)
            
        
        bVal = (bO - min(b) - max(b)) / 48
        oVal = (oO - min(o) - max(o)) / 48
        print("B -> ", bVal)
        print("O -> ", oVal)
        oResult = bVal - (oVal * self.offsetMultiplier)
        print("o result -> ", oResult)
        return [oResult, oVal]

    def calculate(self, val):
        return (val * 3.3 / 65536) * _DIVRATE
    
    def read(self):
        battery, offset = self.readInput()
        batteryVal = self.calculate(battery)
        
        print("ADC read ->", batteryVal)
        
        offsetVal = self.calculate(offset)
        print("Offset by reference ->", offsetVal)
        
if __name__ == '__main__':
    myAdc = AdcMonitor()
    myAdc.read()
