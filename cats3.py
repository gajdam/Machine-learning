kamien = {'x': 2, 'y': 2, 'z': 1}
mysz_polna = {'x': 3, 'y': 5, 'z': 3}
mysz_domowa = {'x': 2, 'y': 7, 'z': 2}
slimak = {'x': 3, 'y': 3, 'z': 3}
lisc = {'x': 2, 'y': 3, 'z': 1}

class Obiekt:
    def __init__(self, tab ,d):
        self.tab = tab
        self.d = d

Luna = [
    Obiekt(mysz_polna, 0.4),
    Obiekt(mysz_domowa, 0.4),
    Obiekt(slimak, 0.1),
    Obiekt(lisc, 0.0),
    Obiekt(kamien, 0.1)
]

Ariana = [
    Obiekt(mysz_polna, 0.125),
    Obiekt(mysz_domowa, 0.125),
    Obiekt(slimak, 0.375),
    Obiekt(lisc, 0.375),
    Obiekt(kamien, 0.0)
]

Dante = [
    Obiekt(mysz_polna, 0.2),
    Obiekt(mysz_domowa, 0.2),
    Obiekt(slimak, 0.05),
    Obiekt(lisc, 0.05),
    Obiekt(kamien, 0.5)
]

def sortuj_obiekty(lista_obiektow):
    def klucz_sortowania(obiekt):
        obj_objetosc = obiekt.tab['x'] * obiekt.tab['y'] * obiekt.tab['z']
        return obiekt.d / obj_objetosc

    return sorted(lista_obiektow, key=klucz_sortowania, reverse=True)

def plecak_wypelnienie(plecak, lista_piorytetow):

    zapakowane_x, zapakowane_y, zapakowane_z, iteracja, temp_y, suma, wartość_przedmiotow = 0, 0, 0, 0, 0, 0, 0

    for obiekt in lista_piorytetow:
        if (obiekt.tab['x'] + zapakowane_x < plecak['x']):

            while (plecak['x'] >= zapakowane_x + obiekt.tab['x']):
                zapakowane_x += obiekt.tab['x']
                zapakowane_y = 0
                suma = 0
                if (plecak['y'] >= zapakowane_y + obiekt.tab['y']):

                    while (plecak['y'] >= zapakowane_y + obiekt.tab['y']):

                        suma += obiekt.tab['y']
                        zapakowane_y += obiekt.tab['y']
                        iteracja += 1
                        wartość_przedmiotow += obiekt.d
                        zapakowane_z = obiekt.tab['z']

                        while (plecak['z'] >= zapakowane_z + obiekt.tab['z']):

                            zapakowane_z += obiekt.tab['z']
                            iteracja += 1
                            wartość_przedmiotow += obiekt.d

                    if (suma < plecak['y']):
                        zapakowane_y = 0
                        temp_y = plecak['y'] - suma

                if (temp_y >= zapakowane_y + obiekt.tab['z']):

                    while (temp_y >= zapakowane_y + obiekt.tab['z']):
                        zapakowane_y += obiekt.tab['z']
                        iteracja += 1
                        wartość_przedmiotow += obiekt.d
                        zapakowane_z = obiekt.tab['y']

                        while (plecak['z'] >= zapakowane_z + obiekt.tab['y']):
                            zapakowane_z += obiekt.tab['y']
                            iteracja += 1
                            wartość_przedmiotow += obiekt.d

        if (obiekt.tab['z'] + zapakowane_x < plecak['x']):

            while (plecak['x'] >= zapakowane_x + obiekt.tab['z']):
                zapakowane_x += obiekt.tab['z']
                zapakowane_y = 0
                suma = 0
                if (plecak['y'] >= zapakowane_y + obiekt.tab['y']):

                    while (plecak['y'] >= zapakowane_y + obiekt.tab['y']):

                        suma += obiekt.tab['y']
                        zapakowane_y += obiekt.tab['y']
                        iteracja += 1
                        wartość_przedmiotow += obiekt.d
                        zapakowane_z = obiekt.tab['z']

                        while (plecak['z'] >= zapakowane_z + obiekt.tab['x']):
                            zapakowane_z += obiekt.tab['x']
                            iteracja += 1
                            wartość_przedmiotow += obiekt.d

                    if (suma < plecak['y']):
                        zapakowane_y = 0
                        temp_y = plecak['y'] - suma

                if (temp_y >= zapakowane_y + obiekt.tab['x']):

                    while (temp_y >= zapakowane_y + obiekt.tab['x']):
                        zapakowane_y += obiekt.tab['x']
                        iteracja += 1
                        wartość_przedmiotow += obiekt.d
                        zapakowane_z = obiekt.tab['y']

                        while (plecak['x'] >= zapakowane_z + obiekt.tab['y']):
                            zapakowane_z += obiekt.tab['y']
                            iteracja += 1
                            wartość_przedmiotow += obiekt.d

    return iteracja, wartość_przedmiotow

plecak = {'x': 10, 'y': 20, 'z': 10}

posortowane_Luna = sortuj_obiekty(Luna)
posortowane_Ariana = sortuj_obiekty(Ariana)
posortowane_Dante = sortuj_obiekty(Dante)

wynik_Luna, wartosc_Luna = plecak_wypelnienie(plecak,posortowane_Luna)
wynik_Ariana, wartosc_Ariana = plecak_wypelnienie(plecak,posortowane_Ariana)
wynik_Dante, wartosc_Dante = plecak_wypelnienie(plecak,posortowane_Dante)

print(f"Punkty, uzyskane przez Luna: {wynik_Luna*0.5 + wartosc_Luna*0.5}")
print(f"Punkty, uzyskane przez Ariana: {wynik_Ariana*0.5 + wartosc_Ariana*0.5}")
print(f"Punkty, uzyskane przez Dante: {wynik_Dante*0.5 + wartosc_Dante*0.5}")
