import classes
import random

file = open("adatok.txt", "r", encoding="utf8")
fileList = []

for i in file:
    fileList.append(classes.Kerdesek(i))
file.close()

numquestion = 0
point = 0
ans = ["a", "b", "c"]

for i in range(len(fileList)):
    numquestion += 1
    num = random.randint(0, len(fileList) - 1)
    print(f"{numquestion}. kérdés: {fileList[num].question}\nVálaszok:\n\ta, {fileList[num].answer1}\n\tb, "
          f"{fileList[num].answer2}\n\tc, {fileList[num].answer3}")
    answer = input("a / b / c: ")
    while answer not in ans:
        print("Helyes adatot adjon meg!")
        print(f"{numquestion}. kérdés: {fileList[num].question}\nVálaszok:\n\ta, {fileList[num].answer1}\n\tb, "
              f"{fileList[num].answer2}\n\tc, {fileList[num].answer3}")
        answer = input("a / b / c: ")

    if answer == "a":
        point += fileList[num].point1
    elif answer == "b":
        point += fileList[num].point2
    elif answer == "c":
        point += fileList[num].point3

    fileList.remove(fileList[num])

print(f"A pontszámod: {point}")
if point >= 13 and point <= 21:
    print("Gratulálunk, te tudod, hogy kell igazán egészségesen élni. Ami nagyon fontos, hogy továbbra is figyelj oda a\n"
          " megfelelő hidratálásra és a rostbevitelre. Ha még nem próbáltad, akkor itt az ideje kipróbálni az alternatív\n"
          " fehérje megoldásokat is. Szuper egészséges és finom tud lenni. Egyre vigyázz, azért ne hajtsd túl magad. ;)\n")
elif point >= 22 and point <= 30:
    print("Jó úton jársz, de még van mit javítani az étkezéseden. Figyelj a rost és a megfelelő fehérje bevitelre (hal,\n"
          " pulyka vagy csirke legyen a fő és a hüvelyes zöldségek). Nézz utána a mediterrán étrendnek, a tested meg\n"
          " fogja hálálni. A nassolást, amennyire lehet, mellőzd. A nyugodt alváshoz pedig elengedhetetlen a jó\n "
          "környezet, a sötét szoba. Nyugi, nincs szörny az ágy alatt. ;)")
elif point >= 31 and point <= 39:
    print(" Ajjaj, nagy a baj. Nem figyelsz az étkezésedre. Ha ezen nem változtatsz, komoly egészségügyi következményei\n "
          "is lehetnek (mint a cukorbetegség, a magas vérnyomás vagy a korai csontritkulás).")
else:
    print("HIBA!")