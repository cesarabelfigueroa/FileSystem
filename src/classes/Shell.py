from classes.FileSystem import FileSystem

class Shell:

    def __init__ (self):
        self.fs = FileSystem()
    def execute(self):
        while(True):
            print(">>: ", end=" "),
            parameters = input()
            parameters = parameters.split(" ")
            if(parameters[0] == "cat"):
                print("cat")
                if parameters[1]== ">":
                    content = input()
                    

            elif(parameters[0] == "ls"):
                print("ls")
            elif(parameters[0] == "mkdir"):
                print("mkdir")
            elif(parameters[0] == "rmdir"):
                print("rmdir")
            elif(parameter[0] == "rm"):
                print("rm")
            elif(parameter[0] == "cd"):
                print("cd")
            
    def createRoot(self):
        self.fs.createDirectory("hola")
