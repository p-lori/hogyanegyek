import classes

file = open("adatok.txt", "r", encoding="utf8")
fileList = []

for i in file:
    fileList.append(classes.Kerdesek(i))
file.close()
print(fileList[0].question)
