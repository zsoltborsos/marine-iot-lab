import framebuf
from utime import sleep
from mysd import mySd
from uos import listdir
import gc
from myepaper import Eink
import machine
#import logger
#import myuart

def clear():
    screen = Eink()
    screen.clear()
    sleep(10)
    screen.sleep()
    print("Screen is reset!")

def reset():
    sleep(1)
    Pin(22, Pin.OUT)(1)

@micropython.native
def showImage(img):
    #gc.collect()
    screen = Eink(rotation=270)
    if hasattr(img, 'img_red') and hasattr(img, 'img_bw'):
        #print("image is grey")
        posx = 0
        if img.width < 480:
            posx = (480 - img.width) // 2
        posy = 0
        if img.height < 280:
            posy = (280 - img.height) // 2
        buffer = framebuf.FrameBuffer(img.img_bw, img.width, img.height, framebuf.MONO_HLSB)
        screen.blit(buffer, posx, posy, ram=screen.RAM_BW)
        buffer = framebuf.FrameBuffer(img.img_red, img.width, img.height, framebuf.MONO_HLSB)
        screen.blit(buffer, posx, posy, ram=screen.RAM_RED)
    else:
        #print("image is bw")
        buffer = framebuf.FrameBuffer(img.img_bw, img.width, img.height, framebuf.MONO_HLSB)    
        screen.blit(buffer, 0, 0)

    screen.show()
    screen.sleep()

@micropython.native
def mymain():
#    logs = logger.logger()
#    uart.send("Starting main...")
#     screen = getScreen()
#     screen.clear()
    #clear()
    gc.enable()
    mySdInstance = mySd()
    
    #mySdInstance.test()
    
    imageFiles = listdir("sd/img_bw")
    #print(imageFiles)
    
    # get next image index from file
    
    i = 0
    temp = 0
    #msg = ""
    with open("sd/index.txt", "r") as file:
        i = file.read()
        #print("and our index is -> ", i)
        temp = int(i) + 1
        #print("and our new index is {} -> ", temp)
        file.close()
        #msg += "Index is {}. New index is {}", i, temp
#        msg += "Got index"
#        uart.send("Got Index")
    
    with open("sd/index.txt", "w") as file:
        file.write(str(temp))
        file.close()
    
    
    import sys
    sys.path.append("/sd/img_bw")
    #import IMG_0182_gs_d as img1
    #print("img 1 -> ", img1)
    
    img = 0
    
    try:
        #print("name -> ", imageFiles[int(i)])
#        msg += "Importing img file"
#        uart.send("importing img")
        img = __import__(imageFiles[int(i)][:-3])
    except:
#        msg += "Could not open file"
         print("Could not open file ->", imageFiles[i])
#        uart.send("Could not find image")
    
    if img != 0:
        #gc.collect()
        #print("memory -> ", gc.mem_free())
        #init()
        #uart.send("Trying to show image!")
        sleep(1)
        #gc.collect()
        showImage(img)
        #uart.send("Image showing?!")
        #uart.send("Mem -> {}", gc.mem_free())
        #msg += "memory -> {}", gc.mem_free()
        print("memory -> ", gc.mem_free())
        #print("memory -> ", gc.mem_free())
        #print("img ->", img)
#        msg += "Going to sleep..."
        #uart.send("Going to sleep")
    #sleep(30)   
    
    machine.deepsleep(300000)

#uart = myuart.myUart()
mymain()

#clear()


