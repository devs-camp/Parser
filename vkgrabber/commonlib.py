import os

def subdir(dirPath, subfolder):
    return os.path.join(dirPath, subfolder)

def subfile(dirPath, filename):
    return os.path.join(dirPath, filename)

def saveFile(fileFullPath, content):
    file = open(fileFullPath, "w")
    file.write(content)
    file.close()

def createFolder(folder):
    if not os.path.isdir(folder):
        os.mkdir(folder)

def printProgress(progress):
    print("." * progress, end="")