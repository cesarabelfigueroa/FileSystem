
class DirectoryEntry:

    def __init__(self, inode, rec_len, name_len, name, indexNode):
        self.inode = inode
        self.rec_len = rec_len
        self.name_len = name_len
        self.name = name
        self.indexNode = indexNode

    def getRecLen (self):
        return self.rec_len