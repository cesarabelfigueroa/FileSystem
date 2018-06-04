from classes.Shell import Shell
from classes.FileSystem import FileSystem

def main():
	shell = Shell("./disk/Disk.bin")
	shell.createRoot()
	shell.execute()
main()