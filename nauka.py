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

# def BMI(waga,wzrost):
#     bmi = waga / (wzrost **2)
#     if bmi < 18.5:
#         return f"Niedowaga, Twoje BMI to {bmi}"
#     elif bmi < 25:
#         return f"Waga prawidłowa, Twoje BMI to {bmi:.2f}"
#     elif bmi < 30:
#         return f"Nadwaga, Twoje BMI to {bmi:.2f}"
#     else:
#         return f"Otyłość, Twoje BMI to {bmi:.2f}"
#
# waga = float(input("Podaj wagę w kg: "))
# wzrost = float(input("Podaj wzrost w metrach: "))
# print(BMI(waga,wzrost))

# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.players = []
#
#     def add_player(self, player):
#         self.players.append(player)
#         print(f"Zawodnik {player} został dodany do drużyny {self.name}")
#
#     def remove_player(self, player):
#         if player in self.players:
#             self.players.remove(player)
#             print(f"Zawodnik {player} został usunięty z drużyny {self.name}")
#         else:
#             print(f"Zawodnik {player} nie został znaleziony w drużynie {self.name}")
#
#     def display_players(self):
#         print(f"Zawodnicy drużyny {self.name}:")
#         for player in self.players:
#             print(f" - {player}")
#
# druzyna = Team("Barcelona")
# druzyna.add_player("Raphinha")
# druzyna.display_players()
# druzyna.add_player("Lamine Yamal")
# druzyna.remove_player("Raphinha")
# druzyna.display_players()


# class Product:
#     def __init__(self, name, price, quantity=0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def info(self):
#         print(f"Produkt: {self.name}, Cena: {self.price}, Ilość: {self.quantity}")
#
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Produkt {product.name} został dodany do sklepu {self.name}")
#     def total_value(self):
#         return sum(product.price * product.quantity for product in self.products)
#
#     def find_cheapest(self):
#         if not self.products:
#             return None
#         najtańszy = self.products[0]
#         for product in self.products:
#             if product.price < najtańszy.price:
#                 najtańszy = product
#         return najtańszy
#
# sklep = Shop("MediaMarkt")
# p1 = Product("Laptop", 3500, 10)
# p2 = Product("Myszka", 120, 50)
# p3 = Product("Monitor", 1800, 5)
# sklep.add_product(p1)
# sklep.add_product(p2)
# sklep.add_product(p3)
# print(f"Łączna wartość: {sklep.total_value()}")
# print(f"Najtańszy produkt: {sklep.find_cheapest().name}")

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f"{self.title} - {self.author} ({self.pages} stron)"
#
#     def is_long(self):
#         return self.pages > 300
#
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#         print(f"Książka {book.title} została dodana do biblioteki {self.name}")
#
#     def show_books(self):
#         print(f"Książki w bibliotece {self.name}:")
#         for book in self.books:
#             print(f" - {book}")
#
#     def find_long_books(self):
#         long_books = []
#         for book in self.books:
#             if book.is_long():
#                 long_books.append(book)
#         return long_books
#
#
# ksiazka1 = Book("Pan Tadeusz", "Adam Mickiewicz", 1000)
# ksiazka2 = Book("Wesele", "Stanisław Wyspiański", 300)
# ksiazka3 = Book("Zemsta", "Aleksander Fredro", 200)
# biblioteka = Library("Biblioteka Miejska")
# biblioteka.add_book(ksiazka1)
# biblioteka.add_book(ksiazka2)
# biblioteka.add_book(ksiazka3)
# biblioteka.show_books()
#
# print(ksiazka1)
#
# print("Długie książki:")
# for ksiazka in biblioteka.books:
#     if ksiazka.is_long():
#         print(ksiazka)
#
# print("Długie książki:")
# for book in biblioteka.find_long_books():
#     print(f"-{book}")

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#     def __str__(self):
#         return f"{self.brand} ({self.year})"
#
#     def age(self):
#         return 2026 - self.year
#
# class Car(Vehicle):
#     def __init__(self, num_of_doors):
#         self.num_of_doors = num_of_doors
#
#     def __str__(self):
#         return f"{self.brand} ({self.year}) ma {self.num_of_doors} drzwi"
#
# class Motorcycle(Vehicle):
#     def __init__(self, engine_type):
#         self.engine_type = engine_type
#
#     def __str__(self):
#         return f"{self.brand} ({self.year}) ma {self.engine_type}"
#
# Audi_A3 = Vehicle("Audi", 2024)
# print(Audi_A3)
#
# Audi_A3 = Car("Audi", 2024, 5)
# print(Audi_A3)
#
# Yamaha = Motorcycle("Yamaha", 2024, "V8")
# print(Yamaha)


# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def __str__(self):
#         return f"{self.owner} | Saldo: {self.balance}"
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:     
#             print("Nie masz wystarczajacych srodkow na koncie")
#         else:
#             self.balance -= amount
#
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
# 
#     def add_interest(self):
#         self.balance += self.balance * self.interest_rate
#         print(f"Oprocentowanie dodane do konta: {self.balance * self.interest_rate}")
#
# class StudentAccount(Account):
#     def __init__(self, owner, balance=0, university=None):
#         super().__init__(owner, balance)
#         self.university = university
#
#     def withdraw(self, amount):
#         if amount > 500:
#             print("Nie mozna wyplacic wiekszej kwoty niz 500zl")
#         elif amount > self.balance:
#             print("Nie masz wystarczajacych srodkow na koncie")
#         else:
#             self.balance -= amount
#
# konto = SavingsAccount("Anna", 1000, 0.05)
# konto.add_interest()
# print(konto)
#
# student = StudentAccount("Marek", 2000, "AGH")
# student.withdraw(300)
# student.withdraw(600)
# print(student)

# kwadraty = []
# for x in range(10):
#     kwadraty.append(x ** 2)
# print(kwadraty)
#
# kwadraty = [x ** 2 for x in range(10)]
# print(kwadraty)
#
# liczby = [1,5,12,3,8,15,7,20,2,9]
# parzyste = [x for x in liczby if x % 2 == 0]
# print(parzyste)
#
# wieksze_od_10 = [x for x in liczby if x > 10]
# print(wieksze_od_10)
#
# nazwy = [f"Liczba: {x}" for x in liczby]
# print(nazwy)  

# while True:
#     print("Wybierz co chcesz zrobić: ")
#     print("1. Dodać tekst do pliku")
#     print("2. Odczytać tekst z pliku")
#     print("3. Wyjść")
#     wybor = int(input("Podaj numer wybranej opcji: "))
#     try:
#         if wybor == 1:
#             print("Podaj tekst, który chcesz dodać do pliku:")
#             tekst = input()
#             with open("plik.txt", "a") as f:
#                 f.write(tekst + "\n")
#             print("Tekst został dodany do pliku")
#         elif wybor == 2:
#             with open("plik.txt", "r") as f:
#                 print(f.read())
#         elif wybor == 3:
#             break
#         else:
#             print("Podano zły numer, spróbuj ponownie")
#     except FileNotFoundError:
#         print("Nie znaleziono pliku")

# def wyswietl_prudkty(lista_produktow):
#     for produkt in lista_produktow:
#         print(f"Nazwa: {produkt[0]}, Cena: {produkt[1]}, Ilosc: {produkt[2]}")    
#
# def dodaj_produkt(lista_produktow):
#     nazwa = input("Podaj nazwe produktu")
#     cena = float(input("Podaj cene produktu"))
#     ilosc = int(input("Podaj ilosc produktu"))
#     lista_produktow.append(nazwa, cena, ilosc)
#     print(f"Produkt {nazwa} zostal dodany do listy")
#
# def usun_produkt(lista_produktow):
#     nazwa = input("Podaj nazwe produktu do usuniecia:")
#     for produkt in lista_produktow:
#         if produkt[0] == nazwa:
#             lista_produktow.remove(produkt)
#             print(f"Produkt {nazwa} zostal usuniety z listy")
#             break
#     else:
#         print(f"Nie znaleziono produktu {nazwa}")
#
# def liczba_produktow(lista_produktow):
#     print(f"Ilosc produktow: {len(lista_produktow)}")
#
# produkty = []
#
# while True:
#     print("Wybierz co chcesz zrobić:")
#     print("1. Wyświetl produkty")
#     print("2. Dodaj produkt")
#     print("3. Usuń produkt")
#     print("4. Wyświetl liczbę produktów")
#     print("0. Wyjście")
#     wybor = int(input("Podaj numer wybranej opcji: "))
#     if wybor == 1:
#         wyswietl_prudkty(produkty)
#     elif wybor == 2:
#         dodaj_produkt(produkty)
#     elif wybor == 3:
#         usun_produkt(produkty)
#     elif wybor == 4:
#         liczba_produktow(produkty)
#     elif wybor == 0:
#         exit()
    

def dodaj_druzyne(druzyny):
    print("Wybierz nazwe dla swojej druzyny:")
    druzyna = input()
    if druzyna not in druzyny:
        druzyny[druzyna] = []
        print(f"Druzyna {druzyna} zostala dodana")
    else:
        print(f"Druzyna {druzyna} juz istnieje")

def dodaj_zawodnika(druzyny):
    print("Podaj druzyne do ktorej chcesz dodac zawodnika:")
    druzyna = input()
    if druzyna in druzyny:
        print("Podaj imie i nazwisko zawodnika:")
        zawodnik = input()
        druzyny[druzyna].append(zawodnik)
        print(f"Zawodnik {zawodnik} zostal dodany do druzyny {druzyna}")
    else:
        print(f"Druzyna {druzyna} nie istnieje")
    
def wyswietl_druzyny(druzyny):
    for druzyna in druzyny:
        print(f"Druzyna {druzyna} ma {len(druzyny[druzyna])} zawodnikow")
        for zawodnik in druzyny[druzyna]:
            print(f" - {zawodnik}")


druzyny = {
    "Real Madryt": [],
    "Barcelona": [],
    "Atletico Madryt": []
}

dodaj_druzyne(druzyny)


