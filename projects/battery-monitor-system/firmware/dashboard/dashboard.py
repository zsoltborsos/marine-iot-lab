import uasyncio as asyncio
from color_setup import ssd  # Create a display instance
from gui.core.nanogui import refresh
from gui.widgets.label import Label  # Import any widgets you plan to use
from gui.core.writer import Writer
from gui.widgets.textbox import Textbox
import gui.fonts.courier20 as courier20
import gc
from time import sleep_ms, ticks_ms, ticks_us, ticks_diff
from rp2 import const
from filehandler import FileHandler as fh

# Configuration
DEBUG = False  # Set to True for debug output

_SCREENRESET = 5

import accesspoint
from server_own import Server

class Dashboard:
    def __init__(self):

        if DEBUG:
            print("Dashboard init")
        self.statusText = "(.)(.)"
        self.server = Server()
        self.memOld = 0
        self.mem = 0
        self.statusOld = 0
        self.status = 0
        self.updateNeeded = False
        self.refreshCounter = 0
        self.clearCounter = 0
        self.file = fh("message.txt")
        self.msg = "Waiting..."
        self.newMsg = self.file.read()
        
    async def debugDisplay(self, evt):
        Writer.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
        wri = Writer(ssd, courier20, verbose=False)
        wri.set_clip(False, False, False)
        self.mem = gc.mem_free()
        ip = Label(wri, 200, 3, "IP: {}".format(accesspoint.ip))
        mem = Label(wri, 240, 3, "Mem: {}".format(gc.mem_free()))
        refresh = Label(wri, 280, 3, "")
        clear = Label(wri, 320, 3, "")

        while True:
            if DEBUG:
                print("Updating debug display")
            ip.value("IP: {}".format(accesspoint.ip))
            refresh.value("Refresh: {}".format(self.refreshCounter))
            clear.value("Clear: {}".format(self.clearCounter))
            self.mem = gc.mem_free()
            if self.mem != self.memOld:
                self.memOld = self.mem
                mem.value("Mem: {}".format(self.mem))
                self.updateNeeded = True
            
            await evt.wait()

    async def statusDisplay(self, evt):
        if DEBUG:
            print("Status display init")
        wri = Writer(ssd, courier20, verbose=False)
        wri.set_clip(False, False, False)
        statusLabel = Label(wri, 2, 2, "Incoming message:")
        # statusLabel.value("Incoming message: {}".format(self.msg))
        tb = Textbox(wri, 42, 2, 276, 5, clip=False, bdcolor=ssd.white)
        tb.append("Waiting...")
        while True:

            if DEBUG:
                print("Updating message display")
            self.newMsg = self.file.read()
            if self.newMsg != self.msg:
                tb.append(self.newMsg, ntrim = 100, line = 0)
                tb.scroll(1)
                self.updateNeeded = True
                self.msg = self.newMsg
                
#             else:
#                 self.updateNeeded = False
            await evt.wait()
            

    async def test2(self):
        ssd.fill(ssd.white)
        ssd.clearGc()

    async def tester(self):
        refresh(ssd, True)  # Clear display
        await ssd.wait()
        evt = asyncio.Event()
        asyncio.create_task(self.debugDisplay(evt))
        asyncio.create_task(asyncio.start_server(self.server.serve_client, "0.0.0.0", 80))
        asyncio.create_task(self.statusDisplay(evt))
        partialRefresh = False
        sleeping = False
        partialInit = False
        t = ticks_us()
        ssd.init(1)
        while True:
            gc.collect()
            await ssd.wait()
            
            # ssd.quickUpdate()
            ssd.show()
            evt.set()
            evt.clear()
#             await asyncio.sleep(10)
#             ssd.clearGc()
            # ssd.fill(ssd.black)
            await asyncio.sleep(5)
            await ssd.wait()
            ssd.dither()
            print(ssd.readtest())
            await asyncio.sleep(5)
            
    async def start(self):
        
        refresh(ssd, True)  # Clear display
        await ssd.wait()
        evt = asyncio.Event()
        asyncio.create_task(self.debugDisplay(evt))
        asyncio.create_task(asyncio.start_server(self.server.serve_client, "0.0.0.0", 80))
        asyncio.create_task(self.statusDisplay(evt))
        partialRefresh = False
        sleeping = False
        partialInit = False
        clearNeeded = False
        self.updateNeeded = True
        t = ticks_us()
        while True:
            gc.collect()
            if partialInit == False:
                if DEBUG:
                    print("partial init = false")
                ssd.init(2)
                if DEBUG:
                    print("partial init ran!")
                partialInit = True

            ssd.reset()

            if self.updateNeeded == True:
                await ssd.wait()
                if clearNeeded == True:
                    if DEBUG:
                        print("partial refresh incoming")
                        print("clearing screen <<<<----")
                    try:
                        #ssd.show()
                        #ssd.fill(ssd.black)
                        ssd.clearGc()
                        await ssd.wait()
                        self.refreshCounter = 0
                        self.clearCounter += 1
                        ssd.showPartial()
                        clearNeeded = False
                        continue
                    except Exception as e:
                        if DEBUG:
                            print("wtf -> ", e)
                else:
                    if DEBUG:
                        print("partial refresh incoming == not clearing")
                    try:
                        ssd.showPartial()
                        # ssd.show()
                        self.refreshCounter += 1
                    except Exception as e:
                        if DEBUG:
                            print("wtf -> ", e)
                await ssd.updated()
                await ssd.wait()

            if DEBUG:
                print("Sleeping... zzzz")
            ssd.sleep()
            #sleeping = True
            te = ticks_us()
            runtime = ticks_diff(te, t)//1000
            if DEBUG:
                print('run time --->>', runtime, 'ms')
            if self.refreshCounter == _SCREENRESET:
                clearNeeded = True
                # self.refreshCounter = 0
#             else:
#                 clearNeeded = False

            evt.set()
            evt.clear()
            self.updateNeeded = False
            await asyncio.sleep(10)
        
dash = Dashboard()
#ssd.showPartial()

try:
    #asyncio.run(dash.test2())
    asyncio.run(dash.start())
except KeyboardInterrupt:
    print('Waiting for display to become idle')
    ssd.wait_until_ready()  # Synchronous code
finally:
    _ = asyncio.new_event_loop()