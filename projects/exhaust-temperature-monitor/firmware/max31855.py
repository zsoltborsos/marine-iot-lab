class MAX31855:
  '''
    @brief A class to read thermocouple temperature via SPI.
    The MAX31855 is a read-only SPI device (CLK, CS, DO — no MOSI).
    Wiring: SCK -> CLK, MISO -> DO, any GPIO -> CS (active low).
  '''
  def __init__(self, spi, cs):
    self.spi = spi
    self.cs = cs
    self.cs.value(1)

  def read_celsius(self):
    '''
      @brief Read thermocouple temperature in Celsius.
      @return Temperature as float, or None if a fault is detected.
    '''
    a, b, d = self.read_data()
    if d & 0x7:
      return None
    if a & 0x80:
      a = 0xff - a
      b = 0xff - b
      return -((((a << 8) | b) >> 2) + 1) * 0.25
    return (((a << 8) | b) >> 2) * 0.25

  def read_data(self):
    '''
      @brief Read 4 bytes from MAX31855 via SPI.
      32-bit layout: [31:18] thermocouple temp, [16] fault, [2:0] fault flags.
      @return (byte0, byte1, byte3) — sufficient for temperature and fault detection.
    '''
    buf = bytearray(4)
    self.cs.value(0)
    self.spi.readinto(buf)
    self.cs.value(1)
    return buf[0], buf[1], buf[3]
