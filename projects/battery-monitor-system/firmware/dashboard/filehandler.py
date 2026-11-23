import os

class FileHandler:
    def __init__(self, fileName):
        self.fileName = fileName
        
    def save(self,content):
        with open(self.fileName, 'w') as f:
            f.write(str(content))
            f.close()
            
    def read(self):
        with open(self.fileName, 'r') as f:
            tmp = f.read()
            f.close()
            return tmp