import gc
from machine import Pin, SPI
# Optional use of SD card. Requires official driver. In my testing the
# 31.25MHz baudrate works. Other SD cards may have different ideas.
from sdcard import SDCard
import os

# with open("/sd/test.txt", "w") as f:
#     f.write("Hello world!\r\n")
@micropython.native
class mySd():
    
    def __init__(self):        
        gc.collect()  # Precaution before instantiating framebuf
        # Max baudrate produced by Pico is 31_250_000. ST7789 datasheet allows <= 62.5MHz.
        # Note non-standard MISO pin. This works, verified by SD card.

        #init SPI
        p = Pin
        spi = SPI(0,
                  baudrate=1_000_000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=SPI.MSB,
                  sck=p(18),
                  mosi=p(19),
                  miso=p(16))

        cs = p(14, p.OUT)
        # create sdcard instance
        sd = SDCard(spi, cs)

        vfs = os.VfsFat(sd)
        os.mount(sd, '/sd')


#     def print_directory(self, path, tabs = 0):
#         for file in os.listdir(path):
#             stats = os.stat(path+"/"+file)
#             filesize = stats[6]
#             isdir = stats[0] & 0x4000
#         
#             if filesize < 1000:
#                 sizestr = str(filesize) + " by"
#             elif filesize < 1000000:
#                 sizestr = "%0.1f KB" % (filesize/1000)
#             else:
#                 sizestr = "%0.1f MB" % (filesize/1000000)
#         
#             prettyprintname = ""
#             for i in range(tabs):
#                 prettyprintname += "   "
#             prettyprintname += file
#             if isdir:
#                 prettyprintname += "/"
#             print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))
#             
#             # recursively print directory contents
#             if isdir:
#                 self.print_directory(path+"/"+file, tabs+1)
# 
# 
#     def test(self):
#         print("Files on filesystem:")
#         print("====================")
#         self.print_directory("/sd")


# with open("sd/test01.txt", "r") as file:
#     data = file.read()
#     print("and our data is -> \n", data)