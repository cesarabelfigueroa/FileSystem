import itertools
from classes.DirectoryEntry import DirectoryEntry
class Block:
    def __init__(self,blockId, parent, parentBlock):
        self.blockId = blockId
        self.parent = parent
        self.parentBlock = parentBlock
        self.directoryEntries = []

    
    def getId(self):
        return self.id

    def addDirectoryEntry(self, inode, rec_len, name_len, name):
        entry = DirectoryEntry(inode,rec_len,name_len,name)
        self.directoryEntries.append(entry)

    def getLastDirectoryEntries(self):
        size = len(self.directoryEntries)-1
        if size == -1:
            return False
        return self.directoryEntries[size] 

    
