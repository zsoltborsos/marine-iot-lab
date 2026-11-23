import uasyncio as asyncio
from machine import UART
uart0 = UART(0, 9600)  # Wire GPIO 0-5 and 1-4
uart1 = UART(1, 9600)

async def sender(uart, n):
    swriter = asyncio.StreamWriter(uart, {})
    while True:
        swriter.write(f'Hello from uart{n}\n')
        await swriter.drain()
        await asyncio.sleep(2)

async def receiver(uart, n):
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.readline()
        print(f'Recieved by uart{n}', res)

async def main():
    n = 0
    for uart in (uart0, uart1):
        asyncio.create_task(sender(uart, n))
        asyncio.create_task(receiver(uart, n))
        n += 1
        
    while True:
        await asyncio.sleep(1)

def test():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        asyncio.new_event_loop()
test()