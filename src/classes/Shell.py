from classes.FileSystem import FileSystem
from pathlib import Path



class Shell:

    def __init__(self, path):
        self.path = path
        self.fs = FileSystem()

    def execute(self):
        while(True):
            print(">>: ", end=" "),
            parameters = input()
            parameters = parameters.split(" ")
            if(parameters[0] == "cat"):
                if parameters[1] == ">":
                    content = input()
                    self.fs.createFile(content, parameters[2])
                else:
                    filename = parameters[1]
                    value = self.fs.readFile(filename)
                    print(value)

            elif(parameters[0] == "ls"):
                current = self.fs.currentDirectory
                if(current != None):
                    if (len(parameters) > 1):
                        if (parameters[1] == "-l"):
                            for entry in current.directoryEntries:
                                printValue = "" + str(entry.name) + " " + str(entry.indexNode.i_mode) + " " + str(
                                    entry.indexNode.i_ctime) + " " + str(entry.indexNode.i_size)
                                print(printValue)
                    else:
                        for entry in current.directoryEntries:
                            print(entry.name)
            elif(parameters[0] == "mkdir"):
                if (len(parameters[1]) >= 1):
                    self.fs.createDirectory(parameters[1])

            elif(parameters[0] == "rmdir"):
                if (len(parameters[1]) >= 1):
                    self.fs.deleteDirectory(parameters[1])
            elif(parameters[0] == "rm"):
                if (len(parameters[1]) >= 1):
                    self.fs.deleteFile(parameters[1])
            elif(parameters[0] == "cd"):
                if (len(parameters[1]) >= 1):
                    self.fs.changeDirectory(parameters[1])

    def createRoot(self):
        if(self.fs.reset):
            self.fs.createDirectory("")
        else:
            # exists
            self.fs.changeDirectory(0)
