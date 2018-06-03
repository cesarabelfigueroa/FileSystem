from classes.Disk import Disk
from classes.block import Block
from classes.DirectoryEntry import DirectoryEntry
class FileSystem:

    def __init__(self):
        self.Device = Disk("./disk/Disk.bin")
        self.Disk = self.Device.createDisk()
        self.currentDirectory = None

    def createFile(self, content, name):
        data = bytearray(content, 'utf8')
        inode = self.Device.createInode(1,len(data))
        for block in range(0,inode.i_blocks):
            availableBlock = self.Device.getAvailableSpaceInDataBitmap()
            self.Device.setOcuppiedDataBitmap(availableBlock)
            inode.addBlock(availableBlock)
            subdata = data[block*4000:block*4000+4000]
            self.Device.writeData(subdata,block)
        
        lastDirectory = self.currentDirectory.getLastDirectoryEntries()
        nameSize = len(bytearray(name, "utf8"))
        self.Device.saveInodeInDisk(inode)
        if lastDirectory:
            rec_len = lastDirectory.getRecLen()
            self.currentDirectory.addDirectoryEntry(inode.getId(), rec_len() + 64 + nameSize, nameSize, name)
        else:
            self.currentDirectory.addDirectoryEntry(inode.getId(), 0 , nameSize, name)

    def createDirectory (self, name):
        inode = self.Device.createInode(0,0)
        availableBlock = self.Device.getAvailableSpaceInDataBitmap()
        self.Device.setOcuppiedDataBitmap(availableBlock)
        block = Block(availableBlock)
        inode.addBlock(availableBlock)
        self.Device.saveInodeInDisk(inode)
        nameSize = len(bytearray(name, "utf8"))

        if self.currentDirectory is None:
            self.currentDirectory = block
        else:
            lastDirectory = self.currentDirectory.getLastDirectoryEntries()
            if lastDirectory:
                rec_len = lastDirectory.getRecLen()
                self.currentDirectory.addDirectoryEntry(inode.getId(), rec_len() + 64 + nameSize, nameSize, name)
            else:
                self.currentDirectory.addDirectoryEntry(inode.getId(), 0 , nameSize, name)
        
        self.Device.writeObject(block,availableBlock)
        
    def readFile(self, filename):
        entries = self.currentDirectory.directoryEntries
        for x in entries:
            if(x.name == filename):
                inode = self.Device.getInodeFromDisk(x.inode)
                print(inode.i_block)

                for block in inode.i_block:
                    print(block)
                    value = self.Device.readData(block)
                    print(value)
                return ""

        

            
            


        