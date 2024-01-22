import random
slownik_zdobyczy = {"myszy_polne": 150, "myszy_domowe": 80, "ślimaki": 90, "liście": 300, "kamyki": 200}
pole_x = 5000
pole_y = 5000
def pole_i_nagrody():
    lzk = []  # lzk - lista zajętych koordynatów

    for klucz, wartosc in slownik_zdobyczy.items():
        for i in range(wartosc):
            rnd_x = random.randint(0, 5000)
            rnd_y = random.randint(0, 5000)

            while any(entry[0] == klucz and entry[1:3] == (rnd_x, rnd_y) for entry in lzk):
                rnd_x = random.randint(0, 5000)
                rnd_y = random.randint(0, 5000)

            lzk.append((klucz, rnd_x, rnd_y))
    return lzk
print(pole_i_nagrody())
def podziel_pole_poziomo(rozmiar):
    poleA = (0, 0, rozmiar[0], round(rozmiar[1] / 3))
    poleB = (0, round(rozmiar[1] / 3), rozmiar[0], round(2 * rozmiar[1] / 3))
    poleC = (0, round(2 * rozmiar[1] / 3), rozmiar[0], rozmiar[1])
    return [poleA, poleB, poleC]
def podziel_pole_pionowo(rozmiar):
    poleA = (0, 0, round(rozmiar[0] / 3), rozmiar[1])
    poleB = (round(rozmiar[0] / 3), 0, round(2 * rozmiar[0] / 3), rozmiar[1])
    poleC = (round(2 * rozmiar[0] / 3), 0, rozmiar[0], rozmiar[1])
    return [poleA, poleB, poleC]
rozmiar_pola = (5000, 5000)
pola_poziome = podziel_pole_poziomo(rozmiar_pola)
print("\nPoziome podziały:")
for pole in pola_poziome:
    print(pole)
pola_pionowe = podziel_pole_pionowo(rozmiar_pola)
print("Pionowe podziały:")
for pole in pola_pionowe:
    print(pole)
lzk = pole_i_nagrody()

def nagrody_na_polach(pola):
    poleA, poleB, poleC = [], [], []
    for item in lzk:
        for i in range(len(pola)):
            if pola[i][0] <= item[1] < pola[i][2] and pola[i][1] <= item[2] < pola[i][3]:
                if i == 0:
                    poleA.append(item)
                elif i == 1:
                    poleB.append(item)
                else:
                    poleC.append(item)
    return poleA, poleB, poleC

myszy_total=slownik_zdobyczy["myszy_polne"]+slownik_zdobyczy["myszy_domowe"]
slimaki_total=slownik_zdobyczy["ślimaki"]
liscie_kamyki_total = slownik_zdobyczy["kamyki"]+slownik_zdobyczy["liście"]

def pola_kotow(poziomo, pionowo, myszy_total, slimaki_total, liscie_kamyki_total):
    p_poziomo=nagrody_na_polach(poziomo)
    p_pionowo=nagrody_na_polach(pionowo)
    zestawy_poziomo = []
    i=0 #iterator
    print("Poziomo: ")
    for pole in p_poziomo:
        myszy_counter = 0
        slimaki_counter = 0
        liscie_kamienie_counter = 0
        for item in pole:
            nagroda=item[0]
            if nagroda=="myszy_domowe" or nagroda=="myszy_polne":
                myszy_counter+=1
            elif nagroda=="ślimaki":
                slimaki_counter+=1
            else:
                liscie_kamienie_counter+=1
        zestawy_poziomo.append([myszy_counter/myszy_total, slimaki_counter/slimaki_total, liscie_kamienie_counter/liscie_kamyki_total])
        print("Zestaw",i," - L:", zestawy_poziomo[i][0],"A:", zestawy_poziomo[i][1],"D", zestawy_poziomo[i][2])
        i += 1

    zestawy_pionowo = []
    i=0
    print("Pionowo")
    for pole in p_pionowo:
        myszy_counter = 0
        slimaki_counter = 0
        liscie_kamienie_counter = 0
        for item in pole:
            nagroda=item[0]
            if nagroda=="myszy_domowe" or nagroda=="myszy_polne":
                myszy_counter+=1
            elif nagroda=="ślimaki":
                slimaki_counter+=1
            else:
                liscie_kamienie_counter+=1
        zestawy_pionowo.append([myszy_counter/myszy_total, slimaki_counter/slimaki_total, liscie_kamienie_counter/liscie_kamyki_total])
        print("Zestaw",i," - L:", zestawy_pionowo[i][0],"A:", zestawy_pionowo[i][1],"D", zestawy_pionowo[i][2])
        i += 1
    return zestawy_poziomo, zestawy_pionowo

koci_slownik = {0:'Luna', 1:'Ariana', 2:'Dante'}
zestawy_poziomo, zestawy_pionowo = pola_kotow(pola_poziome, pola_pionowe, myszy_total, slimaki_total, liscie_kamyki_total)

def oblicz_dla_kogo(zestawy):
    rozwiazanie = []
    przypisane_koty = []
    for zestaw in range(len(zestawy)):
        najlepszy_z_zestawu = zestawy[zestaw][0]
        ktory_kot = 0
        for koci_wspolczynnik in range(1, len(zestawy[zestaw])):
            if(najlepszy_z_zestawu < zestawy[zestaw][koci_wspolczynnik] and koci_wspolczynnik not in przypisane_koty):
                najlepszy_z_zestawu = zestawy[zestaw][koci_wspolczynnik]
                ktory_kot = koci_wspolczynnik
        przypisane_koty.append(ktory_kot)
        rozwiazanie.append([koci_slownik[ktory_kot], najlepszy_z_zestawu])
    return rozwiazanie


rozwiazanie_poziome = oblicz_dla_kogo(zestawy_poziomo)
rozwiazanie_pionowe = oblicz_dla_kogo(zestawy_pionowo)

suma_dla_poz = 0
for i in rozwiazanie_poziome:
    suma_dla_poz += i[1]
suma_dla_pio = 0
for i in rozwiazanie_pionowe:
    suma_dla_pio += i[1]

if suma_dla_pio > suma_dla_poz:
    print('Najlepsze rozwiazanie pionowe')
    rozwiazanie = rozwiazanie_pionowe
else:
    print('Najlepsze rozwiazanie poziome')
    rozwiazanie = rozwiazanie_poziome

for miau in range(len(rozwiazanie)):
    print(f'Najlepszy zestawu {miau}go, {rozwiazanie[miau][0]} - {rozwiazanie[miau][1]}')
