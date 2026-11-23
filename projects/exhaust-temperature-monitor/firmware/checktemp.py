from machine import Pin, SPI
from max31855 import MAX31855
import time

# MAX31855 is SPI-only (CLK, CS, DO — no MOSI)
# Wiring: GP2 -> CLK, GP4 -> DO (MISO), GP5 -> CS
spi = SPI(0, baudrate=5_000_000, polarity=0, phase=0, sck=Pin(2), miso=Pin(4))
cs = Pin(5, Pin.OUT)

maxi = MAX31855(spi, cs)

while True:
    try:
        #Read Celsius
        temp = maxi.read_celsius()   
        print("Temperature:%s C" %temp)
        time.sleep(1)
    except Exception as e:
        print("Something went wrong ->", e)
