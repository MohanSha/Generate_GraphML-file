import sys

allFiles = sys.argv
filePosition = 1
fileData = []
print(str(len(allFiles))+"=>"+str(allFiles))
while filePosition < len(allFiles):
    with open (allFiles[filePosition], 'r') as Data:
        fileData.append(Data.read());
        if input("Enter node Y/N: ")=="Y":
             nodevalue=input("Enter node name: ");
             fileData.append(nodevalue);
             pass
        nodevalue="";
    filePosition +=1
def nodes():

    return;
newFileName = input("Enter file name to save:")

with open (newFileName+".graphml", 'w') as newFile:
    newFile.write("".join(fileData))