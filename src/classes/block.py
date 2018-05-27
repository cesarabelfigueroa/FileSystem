import itertools

class Block:
    newid = itertools.count().next
    def __init__(self, data):
        self.id = resource_cl.newid()
        self.data = data
        self.inodePointers = []

    def setData(self):
        self.data = data

    def setInodePointers(self, inodePointers):
        self.inodePointers = inodePointers

    def setInodePointer(self, inodePointer):
        self.inodePointers.append(inodePointer)

    def getId(self):
        return self.id

    def getInodePointers(self):
        return self.inodePointers

    def getInodePointerById(self, id):
        for inodePointer in inodePointers:
            if (id == inodePointer.id):
                return inodePointer
        return "not found"

    def getInodePointerByName(self, name):
        for inodePointer in inodePointers:
            if (name == inodePointer.name):
                return inodePointer
        return "not found"
