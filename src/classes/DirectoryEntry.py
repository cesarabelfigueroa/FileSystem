
class DirectoryEntry:

    def __init__(self, inode, rec_len, name_len, name):
        self.inode = inode
        self.rec_len = rec_len
        self.name_len = name_len
        self.name = name

    def getRecLen (self):
        return self.rec_len