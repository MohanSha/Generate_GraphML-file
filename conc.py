import sys

def nodes(nid,nname,refid):
    print(str(nid) + nname + str(refid))
    return;

def edges(eid,src,target,type="standard"):
    print(str(eid) +src+target+type) 
    return;
 
allFiles = sys.argv
filePosition = 1
fileData = []
print(str(len(allFiles))+"=>"+str(allFiles))
while filePosition < len(allFiles):
    with open (allFiles[filePosition], 'r') as Data:
        fileData.append(Data.read());
        if input("Enter node Y/N: ")=="Y":
             nodevalue=input("Enter node name: ");
             print() 
             nodes(1,"chnrouter",1)
             print() 
             edges(1,"chnrouter","core_switch")
             print() 
             fileData.append(nodevalue);
             pass
        nodevalue="";
    filePosition +=1

newFileName = input("Enter file name to save:")

with open (newFileName+".graphml", 'w') as newFile:
    newFile.write("".join(fileData))