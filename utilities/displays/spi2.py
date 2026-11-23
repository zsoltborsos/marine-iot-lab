# RST_PIN = 21
# DC_PIN = 20
# CS_PIN = 17
# BUSY_PIN = 22
# MISO = 16
# MOSI = 19
# SCK = 18
from drivers.ePaper3in7 import EPD as SSD
RST_PIN         = 12
DC_PIN          = 8
CS_PIN          = 9
BUSY_PIN        = 13

SCK=10
#MISO=11
MOSI=11

# VCC	VSYS	Power input
# GND	GND	GND
# DIN	GP11	MOSI pin of SPI interface, data transmitted from Master to Slave.
# CLK	GP10	SCK pin of SPI interface, clock input
# CS	GP9	Chip select pin of SPI interface, Low active
# DC	GP8	Data/Command control pin (High: Data; Low: Command)
# RST	GP12	Reset pin, low active
# BUSY	GP13	Busy pin

rst = machine.Pin(RST_PIN, machine.Pin.OUT)
busy = machine.Pin(BUSY_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
cs = machine.Pin(CS_PIN, machine.Pin.OUT)
#spi = machine.SPI(1, baudrate=4_000_000)
dc = machine.Pin(DC_PIN, machine.Pin.OUT)


# spi = machine.SPI(0,
#                   baudrate=1000000,
#                   polarity=1,
#                   phase=1,
#                   bits=8,
#                   firstbit=machine.SPI.MSB,
#                   miso=machine.Pin(MISO),
#                   mosi=machine.Pin(MOSI),
#                   sck=machine.Pin(SCK)
#                   )


spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=1,
                  phase=1,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  #miso=machine.Pin(MISO),
                  mosi=machine.Pin(MOSI),
                  sck=machine.Pin(SCK)
                  )


ssd = SSD(spi, cs, dc, rst, busy, landscape=False, asyn=True)


def command(command):
    dc(0)
    cs(0)
    spi.write(command)
    cs(1)

def data(d, buf1=bytearray(1)):
    dc(1)
    for b in d:
        cs(0)
        buf1[0] = b
        spi.write(buf1)
        cs(1)
            
def reg_write(data):
    """
    Write 1 byte to the specified register.
    """
    
    # Construct message (set ~W bit low, MB bit low)
    msg = bytearray()
    #msg.append(0x00 | reg)
    msg.append(data)
    
    # Send out SPI message
    cs.value(0)
    spi.write(msg)
    cs.value(1)
    
def reg_read(reg, cycle = 1):
    
    # Construct message (set ~W bit high)
    msg = bytearray()
    msg.append(reg)
    
    # Send out SPI message and read
    cs.value(0)
    dc(1)
    spi.write(msg)
    result = spi.read(128)
    print("reg_read result:", result)
    dc(0)

    cs.value(1)

    return result

# Start CS pin high
#cs.value(1)

# Workaround: perform throw-away read to make SCK idle high
# reg_read(0x00)


