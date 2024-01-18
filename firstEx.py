import random

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def odleglosc(punkt1, punkt2):
    return ((punkt1.x - punkt2.x) ** 2 + (punkt1.y - punkt2.y) ** 2) ** 0.5

def ocena_trasy(trasa):
    suma_odleglosci = 0
    for i in range(len(trasa) - 1):
        suma_odleglosci += odleglosc(trasa[i], trasa[i+1])
    return suma_odleglosci

def ocena_trasy_z_dzialaniami(trasa):
    suma_odleglosci = 0
    dzialania = []

    for i in range(len(trasa) - 1):
        odleglosc_miedzy_punktami = odleglosc(trasa[i], trasa[i+1])
        suma_odleglosci += odleglosc_miedzy_punktami
        dzialanie = f"odleglosc(({trasa[i].x}, {trasa[i].y}), ({trasa[i+1].x}, {trasa[i+1].y})) = {odleglosc_miedzy_punktami}"
        dzialania.append(dzialanie)

    return suma_odleglosci, dzialania

def wyswietl_trasy(trasy):
    for i, trasa in enumerate(trasy, start=1):
        print(f"Trasa {i}:")
        for punkt in trasa:
            print(f"({punkt.x}, {punkt.y})")
        print(f"Suma odległości: {ocena_trasy(trasa)}\n")

def algorytm_genetyczny(populacja, k, punkty, start, end):
    for pokolenie in range(100):  # liczba pokoleń
        populacja = sorted(populacja, key=lambda x: ocena_trasy(x))
        najlepsza_trasa = populacja[0]

        if len(najlepsza_trasa) == k + 2:
            return najlepsza_trasa  # nie usuwamy punktu początkowego i końcowego

        nowa_populacja = []

        for _ in range(len(populacja) // 2):
            rodzice = random.sample(populacja[:10], 2)  # wybierz dwóch rodziców z pierwszych 10 tras
            punkt_krzyzowania = random.randint(1, len(rodzice[0]) - 2)  # zmieniono punkt_krzyzowania
            potomek = rodzice[0][:punkt_krzyzowania] + rodzice[0][punkt_krzyzowania+1:]  # zmieniono potomek
            nowa_populacja.append(potomek)

        populacja = nowa_populacja

    return None

plansza_tab = []

k = random.randint(1, 10)
n = random.randint(k+1, 50)

start = Punkt(random.randint(1, 100), random.randint(1, 100))
end = Punkt(random.randint(1, 100), random.randint(1, 100))

for _ in range(n):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    punkt = Punkt(x, y)
    plansza_tab.append(punkt)

for punkt in plansza_tab:
    print(f"Punkt: ({punkt.x}, {punkt.y})")

print(f"Punkt początkowy: {start.x},{start.y}")
print(f"Punkt końcowy: {end.x},{end.y}")
print(f"K punktów: {k}")

populacja_size = len(plansza_tab)
if k + 2 > populacja_size:
    print("Error: Sample size is larger than the population size.")
    exit()

# Zmiana - punkt początkowy zawsze na początku, a punkt końcowy na końcu
populacja = [[start] + random.sample(plansza_tab, k) + [end] for _ in range(50)]

trasy_genetyczne = algorytm_genetyczny(populacja, k, plansza_tab, start, end)

if trasy_genetyczne:
    print("Najkrótsza trasa:")
    for punkt in trasy_genetyczne:
        print(f"({punkt.x}, {punkt.y})")

    suma_najkrotszej_trasy, dzialania = ocena_trasy_z_dzialaniami(trasy_genetyczne)
    print(f"Suma odległości dla najkrótszej trasy: {suma_najkrotszej_trasy}")

    print("\nDziałania:")
    for dzialanie in dzialania:
        print(dzialanie)
else:
    print("Nie udało się znaleźć trasy.")

# Dodane - wyświetlanie wszystkich tras
print("\nWszystkie trasy:")
wyswietl_trasy(populacja)
