import classes
import random
import moduls


fileList = moduls.ReadFile("adatok.txt")

numquestion = 0
point = 0

for i in range(len(fileList)):
    numquestion += 1
    num = random.choice(fileList)
    print(f"{numquestion}. kérdés: {num.question}\nVálaszok:\n\ta, {num.answer1}\n\tb, "
          f"{num.answer2}\n\tc, {num.answer3}")
    answer = input("a / b / c: ").lower()
    while answer not in ("a", "b", "c"):
        print("Helyes adatot adjon meg!")
        print(f"{numquestion}. kérdés: {num.question}\nVálaszok:\n\ta, {num.answer1}\n\tb, "
              f"{num.answer2}\n\tc, {num.answer3}")
        answer = input("a / b / c: ").lower()

    if answer == "a":
        point += num.point1
    elif answer == "b":
        point += num.point2
    elif answer == "c":
        point += num.point3

    fileList.remove(num)

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