import gc
from machine import Pin, SPI
from sdcard import SDCard
from os import mount, VfsFat
from rp2 import const
 
_SCK=const(18)
_MOSI=const(19)
_MISO=const(16)
_CS=const(17)
_BAUD=const(1000000)
_ZERO=const(0)
_EIGHT=const(8)
# _AUTOMOUNT=const(True)
_DRIVESTR=const("/sd")
# _LED=const(-1)
# _DETECT=const(-1)
# _WAIT=const(-1)
# _CB=const(None)

#SDCard(_SPI, _SCK, _MOSI, _MISO, _CS, _SDBAUD)

#, _AUTOMOUNT, _DRIVESTR, _LED, _DETECT, _WAIT, _CB

#spi:int, sck:int, mosi:int, miso:int, cs:int,
#baudrate:int=_BAUD, automount:bool=True, drive:str='/sd',
#led:int=-1, detect:int=-1, wait:bool=False, callback=None) -> None:

#0,baudrate=5_000_000,polarity=0,phase=0,bits=8,
#firstbit=SPI.MSB,sck=p(18),mosi=p(19),miso=p(16))

@micropython.native
class mySd():    
  def __init__(self):
   gc.collect()
   p=Pin
   spi=SPI(_ZERO,baudrate=_BAUD,polarity=_ZERO,phase=_ZERO,bits=_EIGHT,firstbit=SPI.MSB,sck=p(_SCK),mosi=p(_MOSI),miso=p(_MISO))
   cs=p(_CS,p.OUT)
   sd=SDCard(spi, cs)
   vfs=VfsFat(sd)
   mount(sd, _DRIVESTR)

#spi:int, sck:int, mosi:int, miso:int, cs:int, baudrate:int=_BAUD,
#automount:bool=True,
#drive:str='/sd', led:int=-1, detect:int=-1, wait:bool=False, callback=None

