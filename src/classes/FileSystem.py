from classes.Disk import Disk

class FileSystem:

    def __init__(self):
    	self.Device = Disk("./disk/Disk.bin")
    	self.Disk = self.Device.createDisk()
    	self.BLOCK_SIZE = 4096


