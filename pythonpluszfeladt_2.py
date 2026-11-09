import pandas
import numpy
import matplotlib.pyplot as graf

df = pandas.read_csv('Air_Quality_and_Health_Impacts.csv')

pm_adatok = df[df['Name'] == 'Fine particles (PM 2.5)']
no2_adatok = df[df['Name'] == 'Nitrogen dioxide (NO2)']
o3_adatok = df[df['Name'] == 'Ozone (O3)']

print("1. Feladat: Legrosszabb városrészek (PM2.5)")
pm_atlagok = pm_adatok.groupby('Geo Place Name')['Data Value'].mean()
legrosszabb_5 = pm_atlagok.sort_values(ascending=False).head(5)
print(legrosszabb_5.to_string())

print("2. Feladat: Korreláció a PM2.5 és NO2 között")
no2_atlagok = no2_adatok.groupby('Geo Place Name')['Data Value'].mean()
kozos_tabla = pandas.merge(pm_atlagok, no2_atlagok, on='Geo Place Name')
kozos_tabla.columns = ['PM25_atlag', 'NO2_atlag']
korrelacio = numpy.corrcoef(kozos_tabla['PM25_atlag'], kozos_tabla['NO2_atlag'])
print(f"Számított korrelációs együttható: {korrelacio[0, 1]:.4f}")

print("3. Feladat: Szennyezőanyagok szórása (ingadozása)")
pm_szoras = numpy.std(pm_adatok['Data Value'].dropna())
no2_szoras = numpy.std(no2_adatok['Data Value'].dropna())
o3_szoras = numpy.std(o3_adatok['Data Value'].dropna())
print(f"PM2.5 szórás: {pm_szoras:.4f}")
print(f"NO2 szórás: {no2_szoras:.4f}")
print(f"Ozone szórás: {o3_szoras:.4f}")

print("4. Feladat: Kiugróan magas (30 feletti) NO2 esetek aránya")
osszes_no2_sor = len(no2_adatok)
magas_no2 = no2_adatok[no2_adatok['Data Value'] > 30] 
szazalek = (len(magas_no2) / osszes_no2_sor) * 100
print(f"Magas NO2 arány: {szazalek:.2f}%")
varos_eloszlas = magas_no2['Geo Place Name'].value_counts().head(5)

print("5. Feladat: Téli vs. Nyári szezon átlagai (Hidegindítás / Fűtés)")
nyar = no2_adatok[no2_adatok['Time Period'].str.contains('Summer', na=False)]
tel = no2_adatok[no2_adatok['Time Period'].str.contains('Winter', na=False)]
nyar_atlag = nyar['Data Value'].mean()
tel_atlag = tel['Data Value'].mean()
print(f"Nyári NO2 átlag: {nyar_atlag:.2f}")
print(f"Téli NO2 átlag: {tel_atlag:.2f}")
print("\nSzámítások kész! Grafikonok pozícionálása (2 sor x 3 oszlop mátrixban)...\n")


fig, axes = graf.subplots(nrows=2, ncols=3, figsize=(18, 10))
fig.suptitle('Levegőminőség Elemzése ', fontsize=18, fontweight='bold', y=0.98)

axes[0, 0].barh(legrosszabb_5.index, legrosszabb_5.values, color='#c0392b', edgecolor='black')
axes[0, 0].invert_yaxis() 
axes[0, 0].set_title('1. Leginkább szennyezett városrészek (PM2.5)', fontsize=12)
axes[0, 0].set_xlabel('PM2.5 átlagos koncentráció')
axes[0, 0].grid(axis='x', linestyle='--', alpha=0.7)

axes[0, 1].scatter(kozos_tabla['PM25_atlag'], kozos_tabla['NO2_atlag'], alpha=0.7, color='#8e44ad', edgecolor='black', s=50)
axes[0, 1].set_title('2. PM2.5 és NO₂ kapcsolata', fontsize=12)
axes[0, 1].set_xlabel('PM2.5 Átlag (Szálló por)')
axes[0, 1].set_ylabel('NO₂ Átlag (Kipufogógázok)')
axes[0, 1].grid(linestyle='--', alpha=0.7)

szoras_ertekek = [pm_szoras, no2_szoras, o3_szoras]
szennyezok = ['PM2.5', 'NO₂', 'Ozone (O3)']
axes[0, 2].bar(szennyezok, szoras_ertekek, color=['#7f8c8d', '#e67e22', '#16a085'], edgecolor='black', width=0.5)
axes[0, 2].set_title('3. Szennyezőanyagok szórása', fontsize=12)
axes[0, 2].set_ylabel('Szórás mértéke')
axes[0, 2].grid(axis='y', linestyle='--', alpha=0.7)

axes[1, 0].pie(varos_eloszlas, labels=varos_eloszlas.index, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black', 'linewidth': 1})
axes[1, 0].set_title('4. Top 5 kiugró NO₂ szintű városrész', fontsize=12)

ertekek = [nyar_atlag, tel_atlag]
evszakok = ['Nyári átlag', 'Téli átlag']
axes[1, 1].bar(evszakok, ertekek, color=['#27ae60', '#2980b9'], edgecolor='black', width=0.4)
axes[1, 1].set_title('5. Hidegindítás és téli fűtés hatása (NO₂)', fontsize=12)
axes[1, 1].set_ylabel('Átlagos NO₂ koncentráció')
axes[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

axes[1, 2].axis('off') 
graf.tight_layout(rect=[0, 0.03, 1, 0.96])
graf.show()
