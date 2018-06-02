from classes.inode import Inode

class Disk:

    def __init__(self, path):
        # MB SIZE
        self.size = 256
        self.path = path
        self.BLOCK_BITMAP_SIZE = 65536
        self.INODE_BITMAP_SIZE = 1048576
        self.INODE_SIZE = 512
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

    def getAvailableSpaceInDataBitmap(self):
        f = open(self.path, 'r')
        for bit in range(0, self.BLOCK_BITMAP_SIZE):
            f.seek(bit)
            value = f.read(1)
            if value == '\x00':
                return bit
        return False

    def getAvailableSpaceInInodeBitmap(self):
        f = open(self.path, 'r')
        for bit in range(self.BLOCK_BITMAP_SIZE, self.INODE_BITMAP_SIZE + self.BLOCK_BITMAP_SIZE):
            f.seek(bit)
            value = f.read(1)
            if value == '\x00':
                return bit
        return False

    def setOcuppiedDataBitmap(self, index):
        with open(self.path, "rb+") as file:
            file.seek(index)
            file.write(bytearray([1]))
            value = file.read(1)
            print(str(value))
            file.close()

    def setOcuppiedInodeBitmap(self, index):
        with open(self.path, "rb+") as file:
            file.seek(index)
            file.write(bytearray([1]))
            value = file.read(1)
            print(str(value))
            file.close()

    def saveInodeInDisk(self, inode):
        with open(self.path, "rb+") as file:
            file.seek((inode.id*self.INODE_SIZE)+inode.offset)
            file.write(bytearray(inode))
            file.close()
        

    def createInode(self, mode, size):
        index = self.getAvailableSpaceInInodeBitmap()
        self.setOcuppiedInodeBitmap(index)

        inode = Inode(index,mode,size)
        self.saveInodeInDisk(inode)
        return inode


