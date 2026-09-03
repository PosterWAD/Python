import random

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


import random

odpowiedz = "x"
wynik = random.randint(1,10)

while odpowiedz != wynik:
    odpowiedz = int(input("Zgadnij liczbę (1-10): "))
    if odpowiedz < wynik:
        print("Za mało!")
    elif odpowiedz > wynik:
        print("Za dużo!")
    else:
        print("Gratulacje! Zgadłeś liczbę.")

