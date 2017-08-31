import sys

allFiles = sys.argv
filePosition = 1
fileData = []

While filePosition < len(allFiles)
    with open (allFiles[filePosition], 'r') as Data:
        fileData.append(Data.read());
    
    filePosition +=1

    newFileName = input("Enter file name to save:")

    with open (newFileName, 'w') as newFile:
        newFile.write("".join(fileData))