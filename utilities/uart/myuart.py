from machine import UART, Pin
import _thread

class myUart:

    def __init__(self):
        self.uart0 = UART(0, baudrate=9600, bits=8, tx=Pin(0), rx=Pin(1), timeout=10)

    def send(self, msg):
        self.uart0.write(msg)
        
    def receive(self):
        rxData = bytes()
        while self.uart0.any() > 0:
            rxData += self.uart0.read(1)
            print("UART msg -> " , rxData.decode('utf-8'))
            
    def threadFunc(self):
        while True:
            self.receive()
    
    def listen(self):
        second_thread = _thread.start_new_thread(self.threadFunc, ())

