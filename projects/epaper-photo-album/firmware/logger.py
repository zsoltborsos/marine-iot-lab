import mysd
import time

class logger:
    def __init__(self):
        sd = mysd.mySd()
        with open("sd/log.txt", "a") as file:
            file.write("\nLogging started at -> ", time.gmtime())
            file.close()
            
    def log(self, msg):
        with open("sd/log.txt", "a") as file:
            file.write("\n", msg)
            file.close()