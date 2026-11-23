from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel
from random import randrange as rnd

# NeoPixel Matrix Configuration
# 20x11 LED matrix = 220 LEDs total
pin = Pin(4, Pin.OUT)
strip = 220  # 20 columns x 11 rows = 220 LEDs
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

r = 0
g = 0
b = 0
# x = 15
direction1 = 1
direction2 = 1
direction3 = 1
colorToChange = 1
while True:
    #randomPixels = generateRandomPixels(60)
    randomColor = getRandomColor(20)
    #randomColorBright = getRandomColor(100)
    print("main color ->", randomColor)
    #print("other color ->", randomColorBright)
    r, g, b = randomColor
    for i in range(0, strip):
        if i == 0:
            np[i] = randomColor
        else:
            r, g, b = np[i - 1]
            if colorToChange == 1:
                if r > 80:
                    direction1 *= -1
                r += direction1
            if colorToChange == 2:
                if g > 80:
                    direction2 *= -1
                g += direction2
            if colorToChange == 3:
                if b > 80:
                    direction3 *= -1
                b += direction3
            np[i] = (r, g, b)
        colorToChange += 1
        if colorToChange == 4:
            colorToChange = 1
        np.write()
        #sleep_ms(10)
        #print("i -> ", i)
    
    #sleep(1)
    