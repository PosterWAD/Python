#imie = input("Podaj imię: ")
#print(f"Wybrane imie to: {imie}")

#nazwisko = input("Podaj nazwisko: ")
#print(f"Wybrane nazwisko to: {nazwisko}")

#wiek = float(input("Podaj wiek: "))
#print(f"Wybrany wiek to: {wiek}")

#print(f"Dane: {imie} {nazwisko}, wiek: {wiek}")

liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

znak = input("Podaj znak działania (+, -, *, /): ")

if znak == "+":
    wynik = liczba1 + liczba2
    print(f"Wynik dodawania: {wynik}")
elif znak == "-":
    wynik = liczba1 - liczba2
    print(f"Wynik odejmowania: {wynik}")
elif znak == "*":
    wynik = liczba1 * liczba2
    print(f"Wynik mnożenia: {wynik}")
elif znak == "/":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
        print(f"Wynik dzielenia: {wynik}")
    else:
        print("Błąd: Nie można dzielić przez zero.")
else:
    print("Niepoprawny znak działania, bądź liczby nie są liczbami.")