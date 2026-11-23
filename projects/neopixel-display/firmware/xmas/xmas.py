from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
strip = 220
np = NeoPixel(pin, strip)

r = 0
g = 0
b = 0
x = 15
forward = True
while True:
    
    for i in range(0, strip):
        if i == 0:
            np[strip - 1] = (0, 0, 0)
        if i != 0:
            np[i - 1] = (0, 0, 0)
        np[i] = (0, x, 0)
        np.write()
        sleep_ms(10)
        print("i -> ", i)

