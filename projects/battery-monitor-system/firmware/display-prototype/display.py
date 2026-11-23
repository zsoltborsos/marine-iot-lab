from color_setup import ssd
from gui.core.colors import *
from gui.core.nanogui import refresh
from gui.widgets.label import Label
from gui.core.writer import CWriter
import gui.fonts.arial35 as arial35
import gc
import uasyncio as asyncio


class Display:

    def __init__(self, offsetMultiplier=1.0, debug=False):
        refresh(ssd, True)
        CWriter.set_textpos(ssd, 0, 0)
        wri = CWriter(ssd, arial35, GREEN, BLACK, verbose=False)
        wri.set_clip(True, True, True)
        self.offsetMultiplier = offsetMultiplier
        self.debug = debug
        self.batteryLabel = Label(wri, 50, 0, "Battery: ~")
        self.offsetLabel = Label(wri, 90, 0, "Offset: ~")
        self.offsetMultiplierLabel = Label(wri, 130, 0, "Multiplier: {}".format(offsetMultiplier))
        self.statusLabel = Label(wri, 200, 130, "Off", fgcolor=RED)
        if self.debug:
            self.memLabel = Label(wri, 2, 45, "Mem: ~")

        Label(wri, 2, 2, " - ", bdcolor=MAGENTA)
        Label(wri, 2, 277, " + ", bdcolor=MAGENTA)
        Label(wri, 203, 2, "Stop", bdcolor=MAGENTA)
        Label(wri, 203, 242, "Start", bdcolor=MAGENTA)
        refresh(ssd)

    async def updateMemDisplay(self, evt):
        await evt.wait()
        self.memLabel.value("Mem: {}".format(gc.mem_free()))
        evt.clear()

    async def updateOffsetDisplay(self, val, evt):
        await evt.wait()
        voltLevel = '%.4f' % val
        toPrint = "Offset:{}V  ".format(voltLevel)
        self.offsetLabel.value(toPrint)
        if self.debug:
            await self.updateMemDisplay(evt)
        refresh(ssd)
        evt.clear()
        await asyncio.sleep_ms(500)

    async def updateStatusDisplay(self, status, evt):
        await evt.wait()
        toPrint = "{} ".format(status)
        self.statusLabel.value(toPrint)
        if self.debug:
            await self.updateMemDisplay(evt)
        refresh(ssd)
        evt.clear()
        await asyncio.sleep_ms(500)

    async def updateBatteryDisplay(self, val, evt):
        await evt.wait()
        voltLevel = '%.4f' % val
        toPrint = "Battery:{}V  ".format(voltLevel)
        self.batteryLabel.value(toPrint)
        if self.debug:
            await self.updateMemDisplay(evt)
        refresh(ssd)
        evt.clear()
        await asyncio.sleep_ms(500)

    async def updateOffsetMultiplierDisplay(self, val, evt):
        await evt.wait()
        offset = '%.1f' % val
        if val < 0:
            toPrint = "Multiplier:{}".format(offset)
        else:
            toPrint = "Multiplier:{}  ".format(offset)

        self.offsetMultiplierLabel.value(toPrint)
        if self.debug:
            await self.updateMemDisplay(evt)
        refresh(ssd)
        evt.clear()
        await asyncio.sleep_ms(500)

    async def test(self, evt):
        if evt is None:
            evt = asyncio.Event()
        print("test fn")
        offsetMp = 1.0
        battery = 11.80
        offset = 0.56
        for i in range(1, 10):
            evt.set()
            await self.updateOffsetMultiplierDisplay((offsetMp + (i / 10)), evt)
            await asyncio.sleep(0.5)
            evt.set()
            await self.updateBatteryDisplay((battery * (i / 10)), evt)
            await asyncio.sleep(0.5)
            evt.set()
            await self.updateOffsetDisplay((offset * (i / 100)), evt)
            await asyncio.sleep(0.5)


if __name__ == '__main__':
    display = Display(debug=True)
    try:
        asyncio.run(display.test(asyncio.Event()))
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()
