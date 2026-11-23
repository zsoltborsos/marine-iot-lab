
from color_setup import ssd  # Create a display instance
from gui.core.nanogui import refresh
from gui.widgets.label import Label  # Import any widgets you plan to use
from gui.core.writer import Writer
import gui.fonts.courier20 as courier20
import gc
from time import sleep_ms, ticks_ms, ticks_us, ticks_diff
from rp2 import const

ssd.wait_until_ready()
ssd.fill(ssd.black)
ssd.show()

ssd.fill(ssd.white)
ssd.wait_until_ready()
ssd.show()