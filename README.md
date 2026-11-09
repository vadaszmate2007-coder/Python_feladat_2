Levegőminőség és Egészségügyi Hatások Elemzése

A projekt egy Python alapú adatelemző és vizualizációs alkalmazás, amely városi levegőminőségi adatokat dolgoz fel a `pandas`, `numpy` és `matplotlib` könyvtárak segítségével. A projekt fő célja a legfontosabb légszennyező anyagok PM2.5, NO2, O3 eloszlásának, összefüggéseinek és szezonális ingadozásainak részletes vizsgálata.


---

Projekt áttekintése

A fő elemző szkript (`2pythonpluszfeladt.py`) a bemeneti CSV adatfájlból kinyeri a kritikus levegőminőségi mutatókat, elvégzi a szükséges statisztikai számításokat (átlag, szórás, korreláció, százalékos arányok), majd az eredményeket egy 2x3-as elrendezésű, átlátható grafikonos mátrixon jeleníti meg.

Főbb vizsgált szennyezők:
* PM2.5 Finom szálló por.
* NO2 Nitrogen dioxide.
* O3 Ozone.

---

Adatforrás és struktúra

A projekt az `Air_Quality_and_Health_Impacts.csv` adathalmazt használja, amely az alábbi kulcsfontosságú oszlopokat tartalmazza:

`Name`  A szennyező anyag megnevezése (pl. *Fine particles (PM 2.5)*, *Nitrogen dioxide (NO2)*, *Ozone (O3)*) 
`Geo Place Name`  A mérés helyszíne (városrész / földrajzi egység) 
`Data Value`  A mért koncentráció értéke 
`Time Period`  A mérés időszaka (pl. *Summer*, *Winter*, vagy éves átlagok) 

---

Elemzési feladatok és módszertan

A szkript 5 fő statisztikai feladatot végez el az adathalmazon:

1. Legrosszabb városrészek PM2.5
Kiszámítja az egyes városrészek átlagos PM2.5 koncentrációját, és kiemeli az 5 legmagasabb értékkel rendelkező területet.

2. Korreláció vizsgálata PM2.5 és NO2
   Meghatározza a szálló por és a nitrogén-dioxid átlogos koncentrációját.

3. Szennyezőanyagok szórása (Ingadozás)
Kiszámítja az egyes szennyezők értékének szórását, megmutatva a mérési adatok stabilitását vagy ingadozását:


4. Kiugróan magas NO2 esetek
Azonosítja a kritikus NO2 értékeket, meghatározza azok arányát az összes méréshez képest, és kilistázza a leginkább érintett városrészeket.

5. Szezonális hatások vizsgálata (Tél vs. Nyár)
Összehasonlítja a nyári és téli NO2 átlagértékeket a fűtési szezon és a hidegindítások hatásának kimutatására.

---

Előfeltételek és telepítés

A projekt futtatásához **Python 3.8+** környezet szükséges.

Szükséges csomagok telepítése

Telepítsd a függőségeket a `pip` segítségével:

pip install pandas numpy matplotlib

---

Használat és futtatás

1. Klónozd a tárolót vagy töltsd le a fájlokat:
2. Helyezd el az `Air_Quality_and_Health_Impacts.csv` fájlt és a `2pythonpluszfeladt.py` szkriptet ugyanabba a könyvtárba.
3. Nyiss egy terminált a projekt mappájában.
4. Futtasd a szkriptet: python 2pythonpluszfeladt.py

---

Vizualizációk áttekintése

A szkript lefutása után egy összefoglaló ablak jelenik meg, amely 2x3-as elrendezésben mutatja be a grafikonokat:
az első sor az 1–3. feladat, a második sor a 4–5. feladat ábráit tartalmazza.

---
