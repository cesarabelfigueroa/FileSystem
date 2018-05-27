import itertools

class Inode:
    newid = itertools.count().next
    def __init__(self, mode, ownerInfo, size, timeStamps, directBlocks, indirectBlocks, doubleIndirect, tripleIndirect):
        self.id = resource_cl.newid()
        self.mode = mode
        self.ownerInfo = ownerInfo
        self.size = size
        self.timeStamps = timeStamps
        self.directBlocks = directBlocks
        self.indirectBlocks = indirectBlocks
        self.doubleIndirect = doubleIndirect
        self.tripleIndirect = tripleIndirect

    def setMode(self, mode):
        self.mode = mode

    def setMode(self, ownerInfo):
        self.ownerInfo = ownerInfo

    def setMode(self, size):
        self.size = size

    def setMode(self, timeStamps):
        self.timeStamps = timeStamps

    def setMode(self, directBlocks):
        self.directBlocks = directBlocks

    def setMode(self, indirectBlocks):
        self.indirectBlocks = indirectBlocks

    def setMode(self, doubleIndirect):
        self.doubleIndirect = doubleIndirect

    def setMode(self, tripleIndirect):
        self.tripleIndirect = tripleIndirect

    def getId(self):
        return self.id

    def getMode(self):
        return self.mode

    def getMode(self):
        return self.ownerInfo

    def getMode(self):
        return self.size

    def getMode(self):
        return self.timeStamps

    def getMode(self):
        return self.directBlocks

    def getMode(self):
        return self.indirectBlocks

    def getMode(self):
        return self.doubleIndirect

    def getMode(self):
        return self.tripleIndirect

    def getNumberOfBlocks(arg):
        return (len(directBlocks) + len(indirectBlocks) + len(doubleIndirect) + len(tripleIndirect))
