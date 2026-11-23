from color_setup import ssd
from gui.core.colors import *
from gui.core.nanogui import refresh
from gui.widgets.label import Label
from gui.core.writer import CWriter
import gui.fonts.arial35 as arial35
import gc


class Display:

    def __init__(self, offsetMultiplier=1.0, debug=False):
        refresh(ssd, True)  # Initialise and clear display.
        CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
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

    def updateMemDisplay(self):
        self.memLabel = "Mem: %.4f" % gc.mem_free()

    def updateOffsetDisplay(self, val):
        voltLevel = '%.4f' % val
        toPrint = "Offset:{}V  ".format(voltLevel)
        self.offsetLabel.value(toPrint)
        if self.debug:
            self.updateMemDisplay()
        refresh(ssd)

    def updateStatusDisplay(self, status):
        toPrint = "{} ".format(status)
        self.statusLabel.value(toPrint)
        if self.debug == True:
            self.updateMemDisplay()
        refresh(ssd)

    def updateMainDisplay(self, val):
        voltLevel = '%.4f' % val
        toPrint = "Battery:{}V  ".format(voltLevel)
        self.batteryLabel.value(toPrint)
        if self.debug:
            self.updateMemDisplay()
        refresh(ssd)

    def updateOffsetMultiplierDisplay(self, val):
        offset = '%.1f' % val
        if val < 0:
            toPrint = "Multiplier:{}".format(offset)
        else:
            toPrint = "Multiplier:{}  ".format(offset)

        self.offsetMultiplierLabel.value(toPrint)
        if self.debug:
            self.updateMemDisplay()
        refresh(ssd)

    def updateOffsetMultiplier(self, val):
        if val == 1:
            self.offsetMultiplier += 0.1
        else:
            self.offsetMultiplier -= 0.1

        self.updateOffsetMultiplierDisplay(self.offsetMultiplier)


if __name__ == '__main__':
    display = Display(debug=True)
