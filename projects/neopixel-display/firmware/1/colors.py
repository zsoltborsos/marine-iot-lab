from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel

pin = Pin(4, Pin.OUT)
strip = 300
np = NeoPixel(pin, strip)


for i in range(0, 300):
#     if i == 0:
#         np[strip - 1] = (0, 0, 0)
#     if i != 0:
#         np[i - 1] = (0, 0, 0)
    #np[i] = (r, g, b)
    #np[i] = (26, 16, 2)
    #np[i] =(80, 50, 4)
    np[i] =(100, 100, 100)
    np.write()
    
    
    #print("i -> ", i)

    #sleep_ms(10)



# warm yellow
# np[i] =(80, 50, 4)
# 
# (26, 16, 2)
