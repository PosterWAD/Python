import random
import math

#imie = input("Podaj imię: ")
#print(f"Wybrane imie to: {imie}")

#nazwisko = input("Podaj nazwisko: ")
#print(f"Wybrane nazwisko to: {nazwisko}")

#wiek = float(input("Podaj wiek: "))
#print(f"Wybrany wiek to: {wiek}")

#print(f"Dane: {imie} {nazwisko}, wiek: {wiek}")

# try:
#     liczba1 = float(input("Podaj pierwszą liczbę: "))
#     liczba2 = float(input("Podaj drugą liczbę: "))
# except ValueError:
#     print("Błąd: Wprowadzono niepoprawną wartość. Proszę podać liczby.")
#     exit()  # Bez tego program pójdzie dalej i zgłosi błąd.
#
# znak = input("Podaj znak działania (+, -, *, /): ")
#
# if znak == "+":
#     print(f"Wynik dodawania: {liczba1 + liczba2}")
# elif znak == "-":
#     print(f"Wynik odejmowania: {liczba1 - liczba2}")
# elif znak == "*":
#     print(f"Wynik mnożenia: {liczba1 * liczba2}")
# elif znak == "/":
#     if liczba2 != 0:
#         print(f"Wynik dzielenia: {liczba1 / liczba2}")
#     else:
#         print("Błąd: Nie można dzielić przez zero.")
# else:
#     print("Niepoprawny znak działania.")


#def osoba(imie, wiek):
#    print(f"Imię: {imie}, Wiek: {wiek}")


#imie = input("Podaj imię: ")
#wiek = int(input("Podaj wiek: "))

#osoba(imie, wiek)

#def dodaj(a, b):
#    return a + b
#def odejmij(a, b):
#    return a - b
#def pomnoz(a, b):
#    return a * b   
#def podziel(a, b):
#    if b != 0:
#        return a / b
#    else:
#        return "Błąd: Nie można dzielić przez zero."

#print("Wybierz działanie: (+, -, *, /)")
#znak = input("Podaj znak działania: ")
#try:
#    a = int(input("Podaj pierwszą liczbę: "))
#    b = int(input("Podaj drugą liczbę: "))
#except ValueError:
#    print("Błąd: Wprowadzono niepoprawną wartość. Proszę podać liczby.")
#    exit()
#if znak == "+":
#    print(f"Wynik dodawania: {dodaj(a, b)}")
#elif znak == "-":
#    print(f"Wynik odejmowania: {odejmij(a, b)}")
#elif znak == "*":   
#    print(f"Wynik mnożenia: {pomnoz(a, b)}")
#elif znak == "/":
#    print(f"Wynik dzielenia: {podziel(a, b)}")
#else:
#    print("Niepoprawny znak działania.")

#def sprawdz_wiek(wiek):
#    if wiek < 0:
#        return "Niepoprawny wiek"
#    elif wiek < 18:
#        return "Niepełnoletni"
#    else:
#        return "Pełnoletni"

#wiek = int(input("Podaj wiek: "))
#wynik = sprawdz_wiek(wiek)

#print(wynik)

#zawodnicy = ["Lewandowski", "Zieliński", "Szczęsny"]
#print("Lista zawodników:")
#for zawodnik in zawodnicy:
#    print(zawodnik)

#nowyZawodnik = input("Podaj nazwisko nowego zawodnika: ")

#zawodnicy.append(nowyZawodnik)

#print("Lista zawodników po dodaniu nowego:")
#for zawodnik in zawodnicy:
#    print(zawodnik)

#zawodnik = {
#    "imie": "Robert",
#    "nazwisko": "Lewandowski",
#    "wiek": 38,
#    "numer": 9,
#    "druzyna": "Polska"
#}

#print(f"Imie i nazwisko: {zawodnik['imie']} {zawodnik['nazwisko']}")
#print(f"Numer koszulki: {zawodnik['numer']}")

#pozycja = input("Podaj pozycję zawodnika: ")
#zawodnik["pozycja"] = pozycja 

#print(zawodnik)


# zawodnicy = [
#     {
#         "imie": "Robert",
#         "nazwisko": "Lewandowski",
#         "numer": 9,
#         "drużyna": "Chicago Fire"
#     },
#     {
#         "imie": "Piotr",
#         "nazwisko": "Zieliński",
#         "numer": 20,
#         "drużyna": "Inter Mediolan"
#     },
#     {
#         "imie": "Wojciech",
#         "nazwisko": "Szczęsny",
#         "numer": 1,
#         "drużyna": "Barcelona"
#     }
# ]
#
# print(zawodnicy[0])
#
# for zawodnik in zawodnicy:
#     print(f" Imię: {zawodnik['imie']},\n Nazwisko: {zawodnik['nazwisko']},\n Numer: {zawodnik['numer']}, \n Drużyna: {zawodnik['drużyna']}")
#
# nowy_zawodnik = {
#     "imie": input("Podaj imię nowego zawodnika: "),
#     "nazwisko": input("Podaj nazwisko nowego zawodnika: "),
#     "numer": int(input("Podaj numer nowego zawodnika: ")),
#     "drużyna": input("Podaj drużynę nowego zawodnika: ")
# }
#
# zawodnicy.append(nowy_zawodnik)
#
# for zawodnik in zawodnicy:
#     print(f" Imię: {zawodnik['imie']},\n Nazwisko: {zawodnik['nazwisko']},\n Numer: {zawodnik['numer']}, \n Drużyna: {zawodnik['drużyna']}")
    
# pelnoletnia = True
# ma_bilet = True
#
# osoba1_wiek = int(input("Podaj wiek osoby 1: "))
# osoba1_bilet = int(input("Czy osoba 1 ma bilet? (1 - tak, 0 - nie): "))
#
# if osoba1_wiek < 18:
#     pelnoletnia = False
#     print("Osoba 1 jest niepełnoletnia.")
# if osoba1_bilet == 0:
#     ma_bilet = False
#     print("Osoba 1 nie ma biletu.")
#
# if pelnoletnia == True and ma_bilet == True:
#     print("Osoba 1 może wejść na koncert.")
# else:
#     print("Osoba 1 nie może wejść na koncert.")

# liczba = 1
#
# while liczba <= 10:
#     print(liczba)
#     liczba += 1
#
# zgadywana_liczba = 7
#
# while zgadywana_liczba != liczba:
#     liczba = int(input("Zgadnij liczbę (1-10): "))
#     if liczba < zgadywana_liczba:
#         print("Za mało!")
#     elif liczba > zgadywana_liczba:
#         print("Za dużo!")
#     else:
#         print("Gratulacje! Zgadłeś liczbę.")

# odpowiedz = "x"
# wynik = random.randint(1, 10)
# liczba_prob = 0
# while odpowiedz != wynik:
#     odpowiedz = int(input("Zgadnij liczbę (1-10): "))
#     liczba_prob += 1
#     if liczba_prob == 5:
#         print("Przegrałeś! Przekroczyłeś limit prób.")
#         break
#     if odpowiedz < wynik:
#         print("Za mało!")
#     elif odpowiedz > wynik:
#         print("Za dużo!")
#     else:
#         print(f"Gratulacje! Zgadłeś liczbę za {liczba_prob} próbą.")


# def punkty_za_wynik(gole_druzyny, gole_przeciwnika):
#     if gole_druzyny > gole_przeciwnika:
#         return 3
#     elif gole_druzyny == gole_przeciwnika:
#         return 1
#     else:  # gole_druzyny < gole_przeciwnika
#         return 0
#
# punkty = print(f"Punkty zdobyte przez drużynę: {punkty_za_wynik(2, 1)}")


# gole = [2, 1, 3, 0, 4]
# ilosc_meczy = len(gole)
# print(f"Ilość meczów: {ilosc_meczy}")
#
# def suma_goli(lista_goli):
#     suma = 0
#     for gol in lista_goli:
#         suma += gol
#     return suma
#
# print(f"Suma goli: {suma_goli(gole)}")
#
# def srednia_goli(lista_goli):
#     return suma_goli(lista_goli) / len(lista_goli)
#
# print(f"Średnia goli na mecz: {srednia_goli(gole)}")
#
# def max_goli(lista_goli):
#     return max(lista_goli)
#
# def min_goli(lista_goli):
#     return min(lista_goli)
#
# print(f"Maksymalna liczba goli w meczu: {max_goli(gole)}")
# print(f"Minimalna liczba goli w meczu: {min_goli(gole)}")


# gole = [2, 1, 2, 0, 3, 2, 1]
#
# mecze_z_wieloma_golami = []
#
# def znajdz_mecze_z_wieloma_golami(lista_goli, prog_goli):
#     for gol in lista_goli:
#         if gol > prog_goli:
#             mecze_z_wieloma_golami.append(gol)
#     return mecze_z_wieloma_golami
#
# print(f"Mecze z wieloma golami (więcej niż 1): {znajdz_mecze_z_wieloma_golami(gole, 1)}. Takich meczy było {len(mecze_z_wieloma_golami)}.")

#sklep = {
#    "owoce": ["jabłko", "banan"],
#    "warzywa": ["marchew", "ziemniak"],
#    "napoje": ["woda", "sok"]
# }

#print(sklep["owoce"])

#sklep["owoce"].append("gruszka")
#print(sklep["owoce"])

#for nazwa, produkty in sklep.items():
#    print(nazwa)
#    print(produkty)

#for nazwa, produkty in sklep.items():
#    print(f"Kategoria: {nazwa}")
#    for produkt in produkty:
#        print(f" - {produkt}")

# biblioteka = {
#     "fantasy": ["Hobbit", "Harry Potter"],
#     "kryminal": ["Sherlock Holmes", "Morderstwo w Orient Expressie"],
#     "science fiction": ["Diuna", "Solaris"]
# }
#
# for gatunek in biblioteka.items():
#     print(f"Gatunek: {gatunek[0]}")
#
# nowy_gatunek = input("Podaj nowy gatunek: ")
# nowa_ksiazka = input("Podaj tytuł nowej książki: ")
#
# if nowy_gatunek in biblioteka:
#     biblioteka[nowy_gatunek].append(nowa_ksiazka)
# else:
#     biblioteka[nowy_gatunek] = [nowa_ksiazka]
#
# for gatunek, ksiazki in biblioteka.items():
#     print(f"Gatunek: {gatunek}")
#     for ksiazka in ksiazki:
#         print(f" - {ksiazka}")

# biblioteka = {
#     "fantasy": ["Hobbit", "Harry Potter"],
#     "kryminal": ["Sherlock Holmes", "Morderstwo w Orient Expressie"],
#     "science fiction": ["Diuna", "Solaris"]
# }
#
# nowy_gatunek = input("Podaj gatunek: ")
# nowa_ksiazka = input("Podaj książkę do usunięcia: ")
# if nowy_gatunek in biblioteka:
#     biblioteka[nowy_gatunek].append(nowa_ksiazka)
# else:
#     biblioteka[nowy_gatunek] = [nowa_ksiazka]
#
# for gatunek, ksiazki in biblioteka.items():
#     print(f"Gatunek: {gatunek}")
#     for ksiazka in ksiazki:
#         print(f" - {ksiazka}")
#
# biblioteka[nowy_gatunek].remove(nowa_ksiazka)
# print(f"Książka '{nowa_ksiazka}' została usunięta z gatunku '{nowy_gatunek}'.")
# for gatunek, ksiazki in biblioteka.items():
#     print(f"Gatunek: {gatunek}")
#     for ksiazka in ksiazki:
#         print(f" - {ksiazka}")

# def dodaj_ksiazke(biblioteka, gatunek, ksiazka):
#     if gatunek in biblioteka:
#         biblioteka[gatunek].append(ksiazka)
#     else:
#         biblioteka[gatunek] = [ksiazka]
#
# def usun_ksiazke(biblioteka, gatunek, ksiazka):
#     if gatunek in biblioteka and ksiazka in biblioteka[gatunek]:
#         biblioteka[gatunek].remove(ksiazka)
#         if not biblioteka[gatunek]:  # Jeśli lista jest pusta, usuń gatunek.
#             del biblioteka[gatunek]
#
# biblioteka = {
#     "fantasy": ["Hobbit", "Harry Potter"],
#     "kryminal": ["Sherlock Holmes", "Morderstwo w Orient Expressie"],
#     "science fiction": ["Diuna", "Solaris"]
# }
#
# dodaj_ksiazke(biblioteka, "fantasy", "Władca Pierścieni")
# usun_ksiazke(biblioteka, "fantasy", "Hobbit")
#
# for gatunek, ksiazki in biblioteka.items():
#     print(f"Gatunek: {gatunek}")
#     for ksiazka in ksiazki:
#         print(f" - {ksiazka}")


# biblioteka = {
#     "fantasy": ["Hobbit", "Harry Potter"],
#     "kryminal": ["Sherlock Holmes"],
#     "science fiction": ["Diuna"]
# }
#
# wybor = -1
#
# while wybor != 0:
#     print("\nMenu:")
#     print("1. Wyświetl wszystkie książki")
#     print("2. Dodaj książkę")
#     print("3. Usuń książkę")
#     print("0. Wyjście")
#     wybor = int(input("Wybierz opcję: "))
#
#     if wybor == 1:
#         for gatunek, ksiazki in biblioteka.items():
#             print(f"Gatunek: {gatunek}")
#             for ksiazka in ksiazki:
#                 print(f" - {ksiazka}")
#     elif wybor == 2:
#         gatunek = input("Podaj gatunek: ")
#         ksiazka = input("Podaj tytuł książki: ")
#         if gatunek in biblioteka:
#             biblioteka[gatunek].append(ksiazka)
#         else:
#             biblioteka[gatunek] = [ksiazka]
#     elif wybor == 3:
#         gatunek = input("Podaj gatunek: ")
#         ksiazka = input("Podaj tytuł książki do usunięcia: ")
#         if gatunek in biblioteka and ksiazka in biblioteka[gatunek]:
#             biblioteka[gatunek].remove(ksiazka)
#     elif wybor == 0:
#         print("Do widzenia!")
#         break
#     else:
#         print("Niepoprawny wybór. Spróbuj ponownie.")

# while True:
#     try:
#         wiek = int(input("Podaj wiek: "))
#
#         if wiek < 0:
#             print("Niepoprawny wiek. Wiek nie może być ujemny.")
#             continue
#         elif wiek < 18:
#             print("Niepełnoletni")
#             #albo zamiast dać break poza można dać tutaj
#         else:
#             print("Pełnoletni")
#             #oraz można dać break tutaj
#         break
#     except ValueError:
#         print("Niepoprawna wartość. Proszę podać liczbę całkowitą.")
#
# def srednia(lista):
#     if len(lista) == 0:
#         return 0
#     return sum(lista) / len(lista)
#
#
# lista_liczba = []
# suma = 0
# for liczba in range(1, 6):
#     podaj_liczbe = int(input(f"Podaj liczbę {liczba}: "))
#     lista_liczba.append(podaj_liczbe)
#     suma += podaj_liczbe
#
# print(f"Suma: {suma}")
# print(f"Średnia: {srednia(lista_liczba)}")
# print(f"Max liczba: {max(lista_liczba)}, min liczba: {min(lista_liczba)}")

#def suma_parzystych(lista):
#    suma = 0
#    for liczba in lista:
#        if liczba % 2 == 0:
#            suma += liczba
#    return suma

#lista_liczb = [1,2,3,4,5,6,7,8,9,10]

#print(f"Suma liczb parzystych: {suma_parzystych(lista_liczb)}")


#class Player:
#    def __init__(self, name, team, position):
#        self.name = name
#        self.team = team
#        self.position = position
#
#    def info(self):
#        print(f"{self.name} gra w drużynie {self.team} na pozycji {self.position}")
#
#player1 = Player("Robert Lewandowski", "Chicago's Fire", "Napastnik")
#
#player1.info()
#
#player2 = Player("Szymon Piękoś", "Źródlana Team", "Napastnik")
#player3 = Player("Kamil Klysk", "Matysowska Team", "Bramkarz")
#
#player2.info()
#player3.info()

# players = [1,2,3]
#
# for player in players:
#     print(f"Numer zawodnika: {player}")
#
# def czy_parzysta(podana_liczba):
#     if podana_liczba % 2 == 0:
#         return True
#     else:
#         return False
# def czy_dodatnia(podana_liczba):
#     if podana_liczba > 0:
#         print(f"Liczba {podana_liczba} jest dodatnia")
#     elif podana_liczba < 0:
#         print(f"Liczba {podana_liczba} jest ujemna")
#     else:
#         print("Liczba jest zerem")
#
# liczba = int(input("Podaj liczbe: "))
# if czy_parzysta(liczba):
#     print(f"Liczba {liczba} jest parzysta")
# else:
#     print(f"Liczba {liczba} jest nieparzysta")
# czy_dodatnia(liczba)
#
# if liczba > 10:
#     print(f"Liczba {liczba} jest większa od 10")
# elif liczba < 10:
#     print(f"Liczba {liczba} jest mniejsza od 10")
# else:
#     print(f"Liczba {liczba} jest równa 10")

# def pole_kola(r):
#     return math.pi * r * r
#
#
# r = float(input("Podaj promień: "))
# print(f"Pole koła o promieniu {r} wynosi {pole_kola(r)}")

def BMI(waga,wzrost):
    bmi = waga / (wzrost **2)
    if bmi < 18.5:
        return f"Niedowaga, Twoje BMI to {bmi}"
    elif bmi < 25:
        return f"Waga prawidłowa, Twoje BMI to {bmi:.2f}"
    elif bmi < 30:
        return f"Nadwaga, Twoje BMI to {bmi:.2f}"
    else:
        return f"Otyłość, Twoje BMI to {bmi:.2f}"

waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w metrach: "))
print(BMI(waga,wzrost))
    