from machine import Pin
from time import sleep, sleep_ms
from neopixel import NeoPixel
from random import randint
import uasyncio as asyncio

class XmasTree:
    
    snowIdx = [ 7, 8, 9, 10, 12, 11, 13, 30, 31, 32, 35,
                52, 57, 74, 79, 78, 97, 100, 119, 121,
                142, 143, 120, 99, 77, 98, 75, 56, 53,
                34, 33, 54, 55, 76, 0, 1, 2, 3, 19, 20,
                21, 22, 23, 24, 41, 45, 43, 42, 44, 46,
                63, 64, 65, 66, 67, 68, 85, 86, 87, 89,
                108, 111, 110, 109, 88, 131, 132, 153 ]
    
    dropLeftOrder = [ 0, 3, 1, 2 ]
    dropLeft = [
        [ 0, 21, 22, 43, 44, 65, 66, 87, 88, 109, 110, 131, 132, 153, 154, 175, 176 ],
        [ 1, 20, 23, 42, 45, 64, 67, 86, 89, 108, 111, 130 ],
        [ 2, 19, 24, 41, 46, 63, 68, 85 ],
        [ 3, 18, 25, 40 ]]
    
    dropRightOrder = [ 0, 2, 1, 3 ]
    dropRight = [
        [ 10, 11, 32, 33, 54, 55, 76, 77, 98, 99, 120, 121, 142, 143, 164, 165, 186 ],
        [ 9, 12, 31, 34, 53, 56, 75, 78, 97, 100, 119, 122],
        [ 8, 13, 30, 35, 52, 57, 74, 79 ],
        [ 7, 14, 29, 36 ]]    

    def __init__(self):
        #pin = Pin(16, Pin.OUT)
        leds = 220
        self.np = NeoPixel(Pin(16, Pin.OUT), leds)

    def show(self, np):
        np.write()

    def drawTree(self, np):
        # yeey final version ?
        np[214] = (25, 13, 0)
        np[203] = (25, 13, 0)
        np[192] = (25, 13, 0)
        np[193] = (0, 26, 0)
        np[194] = (0, 26, 0)
        np[195] = (0, 26, 0)
        np[191] = (0, 26, 0)
        np[190] = (0, 26, 0)
        np[189] = (0, 26, 0)
        np[188] = (0, 26, 0)
        np[185] = (0, 26, 0)
        np[167] = (0, 26, 0)
        np[196] = (0, 26, 0)
        np[177] = (0, 26, 0)
        np[173] = (0, 26, 0)
        np[157] = (0, 26, 0)
        np[129] = (0, 26, 0)
        np[197] = (0, 26, 0)
        np[187] = (0, 26, 0)
        np[38] = (0, 26, 0)
        np[49] = (0, 26, 0)
        np[208] = (26, 0, 0)
        np[198] = (26, 0, 0)
        np[200] = (26, 0, 0)
        np[206] = (26, 0, 0)
        np[92] = (0, 26, 0)
        np[80] = (0, 26, 0)
        np[135] = (0, 26, 0)
        np[134] = (0, 26, 0)
        np[133] = (0, 26, 0)
        np[91] = (0, 26, 0)
        np[90] = (0, 26, 0)
        np[84] = (0, 26, 0)
        np[139] = (0, 26, 0)
        np[140] = (0, 26, 0)
        np[141] = (0, 26, 0)
        np[123] = (0, 26, 0)
        np[94] = (0, 26, 0)
        np[95] = (0, 26, 0)
        np[96] = (0, 26, 0)
        np[60] = (0, 26, 0)
        np[50] = (0, 26, 0)
        np[48] = (0, 26, 0)
        np[47] = (0, 26, 0)
        np[51] = (0, 26, 0)
        np[62] = (26, 0, 0)
        np[107] = (26, 0, 0)
        np[152] = (26, 0, 0)
        np[58] = (26, 0, 0)
        np[101] = (26, 0, 0)
        np[144] = (26, 0, 0)
        np[37] = (0, 26, 0)
        np[39] = (0, 26, 0)
        np[27] = (0, 26, 0)
        np[61] = (0, 26, 0)
        np[59] = (0, 26, 0)
        np[83] = (0, 26, 0)
        np[71] = (0, 26, 0)
        np[81] = (0, 26, 0)
        np[104] = (0, 26, 0)
        np[82] = (0, 26, 0)
        np[93] = (0, 26, 0)
        np[114] = (0, 26, 0)
        np[115] = (0, 26, 0)
        np[116] = (0, 26, 0)
        np[126] = (0, 26, 0)
        np[127] = (0, 26, 0)
        np[128] = (0, 26, 0)
        np[125] = (0, 26, 0)
        np[124] = (0, 26, 0)
        np[136] = (0, 26, 0)
        np[137] = (0, 26, 0)
        np[138] = (0, 26, 0)
        np[148] = (0, 26, 0)
        np[158] = (0, 26, 0)
        np[171] = (0, 26, 0)
        np[172] = (0, 26, 0)
        np[159] = (0, 26, 0)
        np[170] = (0, 26, 0)
        np[181] = (0, 26, 0)
        np[180] = (0, 26, 0)
        np[179] = (0, 26, 0)
        np[178] = (0, 26, 0)
        np[182] = (0, 26, 0)
        np[183] = (0, 26, 0)
        np[184] = (0, 26, 0)
        np[168] = (0, 26, 0)
        np[169] = (0, 26, 0)
        np[160] = (0, 26, 0)
        np[161] = (0, 26, 0)
        np[17] = (26, 26, 19)
        np[5] = (26, 26, 19)
        np[15] = (26, 26, 19)
        np[16] = (26, 26, 26)
        
        np.write()

    async def drop(self, np, col, evt):
        await evt.wait()
        randomTime = randint(130,250)
        #await asyncio.sleep_ms(randomTime)
        await asyncio.sleep_ms(0)
        for i in range(len(col)):
            if i >= 2:
                np[col[0]] = (0, 0, 0)
                np[col[i - 1]] = (5, 5, 5)
                np[col[i - 2]] = (0, 0, 0)
            np[col[i]] = (20, 20, 20)
            if i < len(col) - 1:
                np[col[i + 1]] = (5, 5, 5)
            #sleep_ms(100)
            if i == len(col) - 1:
                np[col[i - 1]] = (0, 0, 0)
            
            await asyncio.sleep_ms(randomTime)
#             if i > 0:
#                 await asyncio.sleep_ms(randomTime)
#             else:
#                 sleep_ms(100)
            np.write()
            
        # clear col?
#         for i in col:
#             np[i] = (0,0,0)
#         np.write()
        await asyncio.sleep(0)
        evt.clear()
        
    async def snow(self, np, idx, evt):
        await evt.wait()
        #tmp = np[idx]
        if np[idx] != (0,0,0):
            print("aborting this one!")
            evt.clear()
            evt.set()
            return
        #await asyncio.sleep_ms(0)
        r = 0
        g = 0
        b = 0
        randomTime = randint(1,30)
        #print("snow up ->", randomTime)
        await asyncio.sleep_ms(10)
        for i in range(40):
            np[idx] = (r,g,b)
            r = g = b = r+1
            np.write()
            if i > 20:
                await asyncio.sleep_ms(randomTime)
            else:
                #await asyncio.sleep_ms(0)
                sleep_ms(randomTime)

        await asyncio.sleep_ms(0)
        randomTime = randint(1,30)
        #print("snow down ->", randomTime)
        for i in range(40):
            r = g = b = r-1
            np[idx] = (r,g,b)
            np.write()
            if i > 20:
                await asyncio.sleep_ms(randomTime)
            else:
                sleep_ms(randomTime)
        await asyncio.sleep(0)
        np[idx] = (0,0,0)
        np.write()
        await asyncio.sleep(1)
        evt.clear()
        
        
    def getRandomSnow(self):
        return self.snowIdx[randint(0, len(self.snowIdx) - 1)]

    def getRandomTimer(self):
        return randint(1, 5)
    
    async def createSnow(self, evt):
        await evt.wait()
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        await self.snow(self.np, self.getRandomSnow(), evt)
        await asyncio.sleep_ms(0)
        evt.clear()
        
    def mixOrders(self):
        self.dropLeftOrder = [ randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 3) ]
        self.dropRightOrder = [ randint(0, 3), randint(0, 3), randint(0, 3), randint(0, 3) ]
#         tmp = self.dropLeftOrder.pop(0)
#         self.dropLeftOrder.append(tmp)
#         tmp = self.dropRightOrder.pop(0)
#         self.dropRightOrder.append(tmp)
    
    async def createDrop(self, evt):
        await evt.wait()
        asyncio.create_task(self.drop(self.np, self.dropLeft[self.dropLeftOrder[0]], evt))
        asyncio.create_task(self.drop(self.np, self.dropRight[self.dropRightOrder[0]], evt))
        asyncio.create_task(self.drop(self.np, self.dropRight[self.dropRightOrder[1]], evt))
        await self.drop(self.np, self.dropLeft[self.dropLeftOrder[1]], evt)
        await asyncio.sleep_ms(0)
        evt.set()
        asyncio.create_task(self.drop(self.np, self.dropLeft[self.dropLeftOrder[2]], evt))
        asyncio.create_task(self.drop(self.np, self.dropRight[self.dropRightOrder[2]], evt))
        asyncio.create_task(self.drop(self.np, self.dropRight[self.dropRightOrder[3]], evt))
        await self.drop(self.np, self.dropLeft[self.dropLeftOrder[3]], evt)
        await asyncio.sleep_ms(0)
        self.mixOrders()
        evt.clear()

    async def meltSnow(self, evt):
        await evt.wait()
#         evt.clear()
        await asyncio.sleep(5)
#         evt.set()
#         await asyncio.sleep_ms(0)
        snowyList = [ 176, 130, 85, 40, 186, 122, 79, 36 ]
        # print(self.np[176])
        r, g, b = self.np[176]
        if r > 20:
            r = g = b = 20
        for i in range(20):
            if r > 0:
                r = g = b = r - 1
            for idx in snowyList:
                self.np[idx] = (r, g, b)
                await asyncio.sleep_ms(0)
            self.np.write()
            if r == 0:
                break
            await asyncio.sleep_ms(40)
        
        evt.clear()

    async def main(self):
        self.drawTree(self.np)
        evt = asyncio.Event()
        while True:
        #z = thread(snow(x), ())
            #evt.set()
            await asyncio.sleep_ms(0)
            for i in range(5):
                evt.set()
                await self.createSnow(evt)
                await asyncio.sleep_ms(0)
                
            await asyncio.sleep(2)
            for i in range(10):
                evt.set()
                await self.createDrop(evt)
                await asyncio.sleep_ms(0)
            await asyncio.sleep(1)
            evt.set()
            await self.meltSnow(evt)
            #await asyncio.sleep_ms(100)
#             for d in range(4):
#                 #r = randint(0, 3)
#                 asyncio.create_task(self.drop(self.np, self.dropLeft[d], evt))
#                 #await asyncio.sleep_ms(0)
            #sleep(self.getRandomTimer())
            await asyncio.sleep(0)
            #evt.set()

    async def test(self):
        evt = asyncio.Event()
        evt.set()
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        asyncio.create_task(self.snow(self.np, self.getRandomSnow(), evt))
        
        await self.snow(self.np, self.getRandomSnow(), evt)
        evt.set()
        await self.snow(self.np, self.getRandomSnow(), evt)
        evt.set()
        await self.snow(self.np, self.getRandomSnow(), evt)
        evt.set()
        asyncio.create_task(self.drop(self.np, self.dropLeft[0], evt))
        asyncio.create_task(self.drop(self.np, self.dropLeft[1], evt))
        asyncio.create_task(self.drop(self.np, self.dropLeft[2], evt))
        asyncio.create_task(self.drop(self.np, self.dropLeft[3], evt))
        evt.set()
        await self.drop(self.np, self.dropLeft[0], evt)
        evt.set()
        await self.drop(self.np, self.dropLeft[1], evt)
        evt.set()
        await self.drop(self.np, self.dropLeft[2], evt)
        evt.set()
        await self.drop(self.np, self.dropLeft[3], evt)
        await asyncio.sleep(0)
        
        

if __name__ == '__main__':
    tree = XmasTree()
    tree.drawTree(tree.np)
    try:
        asyncio.run(tree.main())
    except KeyboardInterrupt:
        print('Interrupted')
    finally:
        _ = asyncio.new_event_loop()