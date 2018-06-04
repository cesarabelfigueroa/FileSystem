from classes.Disk import Disk
from classes.block import Block
from classes.DirectoryEntry import DirectoryEntry
class FileSystem:

    def __init__(self):
        self.Device = Disk("./disk/Disk.bin")
        self.Disk = self.Device.createDisk()
        self.currentDirectory = None
        self.currentBlock = None

    def createFile(self, content, name):
        data = bytearray(content, 'utf8')
        inode = self.Device.createInode(1,len(data))

        for block in range(0,inode.i_blocks):
            availableBlock = self.Device.getAvailableSpaceInDataBitmap()
            self.Device.setOcuppiedDataBitmap(availableBlock)
            inode.addBlock(availableBlock)
            subdata = data[block*4000:block*4000+4000]
            self.Device.writeData(subdata,availableBlock)
        
        lastDirectory = self.currentDirectory.getLastDirectoryEntries()
        nameSize = len(bytearray(name, "utf8"))
        self.Device.saveInodeInDisk(inode)
        if lastDirectory:
            rec_len = lastDirectory.getRecLen()
            self.currentDirectory.addDirectoryEntry(inode.getId(), rec_len + 64 + nameSize, nameSize, name)
        else:
            self.currentDirectory.addDirectoryEntry(inode.getId(), 0 , nameSize, name)
        self.Device.writeObject(self.currentDirectory, self.currentBlock)

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
            self.currentBlock = availableBlock
        else:
            lastDirectory = self.currentDirectory.getLastDirectoryEntries()
            if lastDirectory:
                rec_len = lastDirectory.getRecLen()
                self.currentDirectory.addDirectoryEntry(inode.getId(), rec_len + 64 + nameSize, nameSize, name)
            else:
                self.currentDirectory.addDirectoryEntry(inode.getId(), 0 , nameSize, name)
        
        self.Device.writeObject(block,availableBlock)
        self.Device.writeObject(self.currentDirectory, self.currentBlock)
        
    def readFile(self, filename):
        entries = self.currentDirectory.directoryEntries
        for x in entries:
            if(x.name == filename):
                inode = self.Device.getInodeFromDisk(x.inode)
                if (inode.i_mode != 0):
                    returnValue= ""
                    for block in inode.i_block:
                        value = self.Device.readData(block)
                        returnValue += (value.decode("utf8")).rstrip('\0')
                    return returnValue
                else:
                    return filename + " Is a directory"

    def changeDirectory(self,directoryName):
        entries = self.currentDirectory.directoryEntries
        for x in entries:
            if(x.name == directoryName):
                inode = self.Device.getInodeFromDisk(x.inode)
                if (inode.i_mode == 0):
                    
                    for block in inode.i_block:
                        value = self.Device.readObject(block)
                        self.currentDirectory = value
                        self.currentBlock = block
                        print (value.directoryEntries)
                    
                else:
                    return directoryName + " Is a File"

        

            
            


        