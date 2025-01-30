import classes

def ReadFile(path):
    file = open(path, "r", encoding="utf8")
    fileList = []
    for i in file:
        fileList.append(classes.Kerdesek(i))
    return fileList
