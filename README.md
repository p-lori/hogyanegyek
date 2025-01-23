# Hogyan egyel?


Ez a program egy egyszerű, interaktív kvízt valósít meg, amely segít felmérni, hogy mennyire egészségesen táplálkozol és élsz. A kvíz során különböző életmóddal és táplálkozással kapcsolatos kérdésekre válaszolva pontokat gyűjtesz, amelyek alapján a program kategóriába sorolja az eredményeidet.

Hogyan működik a program?

Adatfájl beolvasása:

A adatok.txt fájlból kerülnek beolvasásra a kérdések és válaszlehetőségek, amelyek a classes.Kerdesek osztály segítségével objektumokká alakulnak.

Kérdések megjelenítése:

A program véletlenszerű sorrendben jeleníti meg a kérdéseket, biztosítva, hogy minden kérdés csak egyszer szerepeljen.

Válaszok ellenőrzése:

A felhasználónak lehetősége van a megadott válaszlehetőségek (a, b, c) közül választani. Hibás input esetén a program újra bekéri a választ.

Pontszámítás:

A felhasználó válaszai alapján pontokat kap, amelyek a válaszokhoz rendelt értékekből kerülnek összesítésre.

Eredmény kiértékelése:

A kvíz végén a program kiértékeli a felhasználó összpontszámát, és az alábbi kategóriák egyikébe sorolja:

13-21 pont: Gratuláció, egészséges életmód.

22-30 pont: Jó úton jársz, de van még javítanivaló.

31-39 pont: Figyelj jobban az egészségedre!

Használati utasítás

Győződj meg arról, hogy a adatok.txt fájl helyesen tartalmazza a kérdéseket és válaszokat a megfelelő formátumban.

Futtasd a programot Python környezetben.

Kövesd az utasításokat, és válaszolj a megjelenő kérdésekre.

A program végén megkapod a pontszámodat és a hozzá tartozó értékelést.

Fájlok

adatok.txt: A kérdéseket és válaszokat tartalmazó adatfájl.

Fő program: A fenti Python kód, amely feldolgozza a kérdéseket, és levezeti a kvízt.

Továbbfejlesztési lehetőségek

Grafikus felhasználói felület (GUI) hozzáadása a könnyebb használat érdekében.

Pontosabb és részletesebb kiértékelés.

Több kategória hozzáadása az eredményekhez.

Új kérdések és válaszlehetőségek bővítése.

Figyelmeztetés

Ez a kvíz nem helyettesíti az orvosi szakvéleményt vagy diagnózist. Célja csupán az, hogy útmutatást nyújtson az egészségesebb életmód felé.
