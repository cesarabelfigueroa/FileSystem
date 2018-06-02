import itertools
import math

class Inode:
    def __init__(self, inodeId, mode, size):
        self.id = inodeId
        self.i_mode = mode
        self.i_size = size
        self.i_atime = datetime.datetime.now()
        self.i_ctime = datetime.datetime.now()
        self.i_mtime = datetime.datetime.now()
        self.i_dtime = '/0'
        self.i_links_count = 0
        self.i_blocks = math.ceil(size / 4000)
        self.i_block = []
        self.offset = 65024
        self.limit = 589312

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
