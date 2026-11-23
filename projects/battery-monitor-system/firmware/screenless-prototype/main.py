from machine import Pin, ADC
from time import sleep, sleep_ms
from color_setup import ssd  # Create a display instance
from gui.core.colors import *
from gui.core.nanogui import refresh
from gui.widgets.label import Label  # Import any widgets you plan to use
from gui.core.writer import CWriter
# import gui.fonts.freesans20 as freesans20
import gui.fonts.arial35 as arial35

# import utime
# import uasyncio as asyncio

_SWDOWN=15
_SWUP=17
_SWSTART=2
_SWSTOP=3
_SWSEND=19
_ADCIN=26
_ADCOFFSET=27

class BatteryMonitor:
    def __init__(self):
#         p = Pin
#         self.buttonDown = p(_SWDOWN, p.IN, p.PULL_UP)
#         self.buttonUp = p(_SWUP, p.IN, p.PULL_UP)
#         self.buttonStart = p(_SWSTART, p.IN, p.PULL_UP)
#         self.buttonStop = p(_SWSTOP, p.IN, p.PULL_UP)
#         self.buttonSend = p(_SWSEND, p.IN, p.PULL_UP)
#         
        self.batteryLevelInput = ADC(_ADCIN)
        self.offsetInput = ADC(_ADCOFFSET)
        self.offsetMultiplier = 1.0
        
        self.running = False
#         self.initScreen()
#         self.listen()

    
    def listen(self):
        #try:
            #self.running = False
            while True:
                #lock.acquire()
                #print("Lock acquired!")
                if not self.buttonDown.value():
                    sleep_ms(20)
                    if not self.buttonDown.value():
                        print("Button -> DOWN pressed!")
                        self.updateOffsetMultiplier(2)
                        while not self.buttonDown.value():
                            sleep_ms(20)
                            
                if not self.buttonUp.value():
                    sleep_ms(20)
                    if not self.buttonUp.value():
                        print("Button -> UP pressed!")
                        self.updateOffsetMultiplier(1)
                        while not self.buttonUp.value():
                            sleep_ms(20)
                            
                if not self.buttonStart.value():
                    sleep_ms(20)
                    if not self.buttonStart.value():
                        print("Button -> START pressed!")
                        self.updateStatusDisplay("On")
                        self.monitor()
                        self.running = True
                        while not self.buttonStart.value():
                            sleep_ms(20)
                            
                if not self.buttonStop.value():
                    sleep_ms(20)
                    if not self.buttonStop.value():
                        print("Button -> STOP pressed!")
                        self.updateStatusDisplay("Off")
                        self.running = False
                        while not self.buttonStop.value():
                            sleep_ms(20)
                
                if self.running == True:
                    self.monitor()

    def readInput(self):
        b = []
        bO = 0
        o = []
        oO = 0
        for i in range(0, 50):
            tmp = self.batteryLevelInput.read_u16()
            b.append(tmp)
            bO += tmp
            tmp = self.offsetInput.read_u16()
            o.append(tmp)
            oO += tmp
            sleep(0.01)    
        
        bVal = (bO - min(b) - max(b)) / 48
        oVal = (oO - min(o) - max(o)) / 48
        print("B -> ", bVal)
        print("O -> ", oVal)
        oResult = bVal - (oVal * self.offsetMultiplier)
        print("o result -> ", oResult)
        return [oResult, oVal]

    def calculate(self, val):
        return (val * 3.3 / 65536) * 10

    def updateOffsetDisplay(self, val):
        voltLevel = '%.4f' % val
        toPrint = "Offset:{}V  ".format(voltLevel)
        self.offsetLabel.value(toPrint)
        refresh(ssd)
    
    def updateStatusDisplay(self, status):
        toPrint = "{} ".format(status)
        self.statusLabel.value(toPrint)
        refresh(ssd)
        
    def updateMainDisplay(self, val):
        voltLevel = '%.4f' % val
        toPrint = "Battery:{}V  ".format(voltLevel)
        self.batteryLabel.value(toPrint)
        refresh(ssd)

    def updateOffsetMultiplierDisplay(self, val):
        offset = '%.1f' % val
        if val < 0:
            toPrint = "Multiplier:{}".format(offset)
        else:
            toPrint = "Multiplier:{}  ".format(offset)
            
        self.offsetMultiplierLabel.value(toPrint)
        refresh(ssd)
     
    def updateOffsetMultiplier(self, val):
        if val == 1:
            self.offsetMultiplier += 0.1
        else:
            self.offsetMultiplier -= 0.1
            
        self.updateOffsetMultiplierDisplay(self.offsetMultiplier)
        
        
    def monitor(self):
        tmp = 0
        #while True:
            #print("thread -> ", _thread.get_ident())
            #print("stack -> ", _thread.stack_size())
            #self.lock.acquire()
        i, o = self.readInput()
        tmp = self.calculate(i)
        
        print("Battery status ->", tmp)
        
        self.updateMainDisplay(tmp)
        tmp = self.calculate(o)
        print("Offset ->", tmp)
        self.updateOffsetDisplay(tmp)
        sleep(0.2)
#         self.lock.release()

if __name__ == '__main__':
    sleep(2)
    batteryMonitor = BatteryMonitor()
    #_thread.start_new_thread(batteryMonitor.monitor(), ())