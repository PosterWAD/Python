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

zawodnik = {
    "imie": "Robert",
    "nazwisko": "Lewandowski",
    "wiek": 38,
    "numer": 9,
    "druzyna": "Polska"
}

print(f"Imie i nazwisko: {zawodnik['imie']} {zawodnik['nazwisko']}")
print(f"Numer koszulki: {zawodnik['numer']}")

pozycja = input("Podaj pozycję zawodnika: ")
zawodnik["pozycja"] = pozycja

print(zawodnik)