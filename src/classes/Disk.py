class Disk:

    def __init__(self, path):
        # MB SIZE
        self.size = 256
        self.path = path

    def getSizeMB(self):
        return self.size

    def getSizeKB(self):
        return self.size * 1024

    def getSizeBytes(self):
        return self.getSizeKB() * 1024

    def createDisk(self):
        f = open(self.path, 'w')
        f.seek(self.getSizeBytes())
        f.write('\0')
        f.close()

