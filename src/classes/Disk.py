from classes.inode import Inode
import pickle

class Disk:

    def __init__(self, path):
        # MB SIZE
        self.size = 256
        self.path = path
        self.BLOCK_BITMAP_SIZE = 64000
        self.INODE_BITMAP_SIZE = 1024
        self.INODE_SIZE = 512
        self.BLOCK_OFFSET = self.INODE_SIZE*1024 + self.BLOCK_BITMAP_SIZE + self.INODE_BITMAP_SIZE 
        self.BLOCK_SIZE = 32000
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
            file.close()

    def setOcuppiedInodeBitmap(self, index):
        with open(self.path, "rb+") as file:
            file.seek(index)
            file.write(bytearray([1]))
            file.close()

    def saveInodeInDisk(self, inode):
        with open(self.path, "rb+") as file:
            file.seek((inode.id*self.INODE_SIZE)+inode.offset)
            value = pickle.dumps(inode, True) 
            file.write(value)
            file.close()

    def getInodeFromDisk(self, index):
        value = ""
        with open(self.path, "rb+") as file:
            file.seek((index*self.INODE_SIZE)+ 65024)
            value = pickle.load(file, encoding='bytes')
            file.close()
        return value

    def createInode(self, mode, size):
        index = self.getAvailableSpaceInInodeBitmap()
        self.setOcuppiedInodeBitmap(index)
        inode = Inode(index-self.BLOCK_BITMAP_SIZE,mode,size)
        return inode

    def writeData (self, data, block):
        with open(self.path, "rb+") as file:
            file.seek(self.BLOCK_OFFSET+ block* self.BLOCK_SIZE)
            file.write(data)
            value = file.read(4000)
            file.close()


    def readData(self, index):
        value = ""
        with open(self.path, "rb+") as file:
            file.seek(self.BLOCK_OFFSET+ index* self.BLOCK_SIZE)
            value = file.read(32000)
            file.close()
        return value

    def writeObject(self, val,block):
        with open(self.path, "rb+") as file:
            file.seek(self.BLOCK_OFFSET+ block* self.BLOCK_SIZE)
            value = pickle.dumps(val, True) 
            file.write(value)
            file.close()
