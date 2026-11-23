from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
strip = 300
np = NeoPixel(pin, strip)

r = 1
g = 6
b = 49
 
forward = True

for i in range(0, strip):
#     if i == 0:
#         np[strip - 1] = (0, 0, 0)
#     if i != 0:
#         np[i - 1] = (0, 0, 0)
    #np[i] = (r, g, b)
    #np[i] = (26, 16, 2)
    np[i] =(80, 50, 4)
    
    
    #print("i -> ", i)
    np.write()
    #sleep_ms(10)
