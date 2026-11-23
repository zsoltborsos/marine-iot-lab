from machine import Pin
import time
from rp2 import const

_GPIO1=13
_GPIO2=12
_GPIO3=2
_GPIO4=3

class buttons:
    def __init__(self, gpio1=_GPIO1, gpio2=_GPIO2, gpio3=_GPIO3, gpio4=_GPIO4):
        p = Pin
        self.buttonDown = p(_GPIO1, p.IN, p.PULL_UP)
        self.buttonUp = p(_GPIO2, p.IN, p.PULL_UP)
        self.buttonStart = p(_GPIO3, p.IN, p.PULL_UP)
        self.buttonStop = p(_GPIO4, p.IN, p.PULL_UP)

    def listen(self, cb):
        try:
            while True:
                #lock.acquire()
                #print("Lock acquired!")
                if not self.buttonDown.value():
                    time.sleep_ms(20)
                    if not self.buttonDown.value():
                        print("Button -> DOWN pressed!")
                        cb(1)
                        while not self.buttonDown.value():
                            time.sleep_ms(20)
                            
                if not self.buttonUp.value():
                    time.sleep_ms(20)
                    if not self.buttonUp.value():
                        print("Button -> UP pressed!")
                        cb(2)
                        while not self.buttonUp.value():
                            time.sleep_ms(20)
                            
                if not self.buttonStart.value():
                    time.sleep_ms(20)
                    if not self.buttonStart.value():
                        print("Button -> START pressed!")
                        cb(3)
                        while not self.buttonStart.value():
                            time.sleep_ms(20)

                if not self.buttonStop.value():
                    time.sleep_ms(20)
                    if not self.buttonStop.value():
                        print("Button -> STOP pressed!")
                        cb(4)
                        while not self.buttonStop.value():
                            time.sleep_ms(20)
                            
        except Exception as e:
            print("Something went wrong with the buttons! -> ", e)
            pass
