import itertools

class Block:
    def __init__(self,blockId):
        self.blockId = blockId
        self.inodePointers = []


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
