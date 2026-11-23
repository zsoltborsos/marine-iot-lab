import time
import uasyncio as asyncio
from filehandler import FileHandler as fh

class Server:
    def __init__(self):
        self.responseJson = '{"msg":"%s"}'
        self.commands = bytearray(20)
        self.message = fh("message.txt")
        #self.tmpArray = [0,0,0,0,0,0,0,0,0,0]

    async def getQueryParams(self, queryString):
        # multiple params present
        response = []
        print("query string-> ", queryString)
        if queryString.find('&') != -1:
            print("hurray")
            commands = queryString.split('&')
            for command in range(0, len(commands)):
                response.append(command.split('='))
        else:
            #single param
            print("single param")
            response = queryString.split('=')
            
        print("Response -> ", response)
        return response

    async def serve_client(self, reader, writer):
        print("Client connected")
        request_line = await reader.readline()
        print("Request:", request_line)
        # We are not interested in HTTP request headers, skip them
        
        while await reader.readline() != b"\r\n":
            pass

        request = str(request_line)
        print("rq", request)
        commands = None
        pos = request.find("/&")
        if pos == -1:
            print("passing on this one...")
            return
        else:
            print("Pos -> ", pos)
            commands = await self.getQueryParams(request[pos+2:-14])
            print("Commands -> ", str(commands))
            
        if commands != None:
            try:
                self.message.save(commands)
                print("Message saved!")
            except Exception as e:
                print("Could not save message to file!")
        
        response = self.responseJson % 'OK'
        writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        writer.write(response)

        await writer.drain()
        await writer.wait_closed()
        print("Client disconnected")
        

    async def serve(self, evt=None):
        print('Setting up webserver...')
        
        commands = asyncio.create_task(asyncio.start_server(self.serve_client, "0.0.0.0", 80))
        while True:
            print("heartbeat")
            await asyncio.sleep(2)
            #await evt.wait()
            if await commands:
                print("Command at the end ---------------> ", commands)
            
    def start(self):        
        try:
            #event = asyncio.Event()
            asyncio.run(self.serve())
            
        finally:
            asyncio.new_event_loop()


if __name__=='__main__':
    server = Server()
    server.start()