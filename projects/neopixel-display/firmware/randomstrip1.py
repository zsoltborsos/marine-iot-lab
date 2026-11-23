from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel
from random import randrange as rnd

pin = Pin(4, Pin.OUT)
strip = 300
np = NeoPixel(pin, strip)

def getRandomPixel(max):
    return rnd(max)

def generateRandomPixels(amount):
    result = []
    for i in range(amount):
        result.append(getRandomPixel(strip - 1))
    return result

def getRandomColor(limit):
    _r = rnd(limit)
    _g = rnd(limit)
    _b = rnd(limit)
    return (_r, _g, _b)

# r = 0
# g = 0
# b = 0
# x = 15

while True:
    randomPixels = generateRandomPixels(60)
    randomColor = getRandomColor(50)
    randomColorBright = getRandomColor(100)
    print("main color ->", randomColor)
    print("other color ->", randomColorBright)
    for i in range(0, strip):
        if i in randomPixels:
            np[i] = randomColorBright
        else:
            np[i] = randomColor
        np.write()
        sleep_ms(10)
        #print("i -> ", i)
    
    sleep(1)
    
