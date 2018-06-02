from classes.Disk import Disk


class FileSystem:

    def __init__(self):
        self.Device = Disk("./disk/Disk.bin")
        #self.Disk = self.Device.createDisk()
        self.BLOCK_SIZE = 4096
        dataBitMapIndex = self.Device.getAvailableSpaceInDataBitmap()
        inodeBitMapIndex = self.Device.getAvailableSpaceInInodeBitmap()
        self.Device.setOcuppiedDataBitmap(dataBitMapIndex)

        #self.Device.setOcuppiedDataBitmap(inodeBitMapIndex)

        print(self.Device.getAvailableSpaceInDataBitmap())
        print(self.Device.getAvailableSpaceInInodeBitmap())

    def creteFile(self, content):
        inode = self.Device.createInode(1,len(bytearray(content)))

        