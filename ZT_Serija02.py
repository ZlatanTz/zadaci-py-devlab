# Zadaci 5 7 12


def worstPodcast(podcasti: list) -> str:
  najgori = min(
    podcasti,
    key = lambda p: p['br_pozitivni'] / p['br_negativni'] if p['br_negativni'] != 0 else 'ne moze se dijeliti nulom'
  )
  return[najgori['naziv']]



class Book:
    def __init__(self, naslov: str, autor: str, godina_izdanja: int, br_kopija: int):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.br_kopija = br_kopija

    def get_naslov(self):
        return self.naslov

    def get_autor(self):
        return self.autor

    def get_godina_izdanja(self):
        return self.godina_izdanja

    def get_br_kopija(self):
        return self.br_kopija

    def set_naslov(self, naslov):
        self.naslov = naslov

    def set_autor(self, autor):
        self.autor = autor

    def set_godina_izdanja(self, godina_izdanja):
        self.godina_izdanja = godina_izdanja

    def set_br_kopija(self, br_kopija):
        self.br_kopija = br_kopija

    def __str__(self):
        return f"{self.naslov} - {self.autor} ({self.godina_izdanja}), kopija: {self.br_kopija}"


class Library:
    def __init__(self):
        self.inventar = []

    def dodaj_knjigu(self, knjiga):
        self.inventar.append(knjiga)

    def obrisi_knjigu(self, naslov):
        for knjiga in self.inventar:
            if knjiga.naslov.lower() == naslov.lower():
                self.inventar.remove(knjiga)
                return True
        return False

    def pretrazi_po_naslovu(self, naslov):
        return [k for k in self.inventar if naslov.lower() in k.naslov.lower()]

    def pretrazi_po_autoru(self, autor):
        return [k for k in self.inventar if autor.lower() in k.autor.lower()]

    def prikazi_knjige(self):
        if not self.inventar:
            print("Biblioteka je prazna.")
        else:
            for knjiga in self.inventar:
                print(knjiga)


def meni():
    biblioteka = Library()

    while True:
        print("\n--- Biblioteka ---")
        print("1. Dodaj knjigu")
        print("2. Prikazi sve knjige")
        print("3. Pretrazi po naslovu")
        print("4. Pretrazi po autoru")
        print("5. Obrisi knjigu")
        print("6. Uredi knjigu")
        print("0. Izlaz")

        izbor = input("Izaberite opciju: ")

        if izbor == "1":
            naslov = input("Unesite naslov: ")
            autor = input("Unesite autora: ")
            godina = int(input("Unesite godinu izdanja: "))
            kopija = int(input("Unesite broj kopija: "))
            knjiga = Book(naslov, autor, godina, kopija)
            biblioteka.dodaj_knjigu(knjiga)
            print("Knjiga dodata!")

        elif izbor == "2":
            biblioteka.prikazi_knjige()

        elif izbor == "3":
            naslov = input("Unesite naslov za pretragu: ")
            rezultat = biblioteka.pretrazi_po_naslovu(naslov)
            for k in rezultat:
                print(k)

        elif izbor == "4":
            autor = input("Unesite autora za pretragu: ")
            rezultat = biblioteka.pretrazi_po_autoru(autor)
            for k in rezultat:
                print(k)

        elif izbor == "5":
            naslov = input("Unesite naslov knjige za brisanje: ")
            if biblioteka.obrisi_knjigu(naslov):
                print("Knjiga obrisana.")
            else:
                print("Knjiga nije pronadjaena.")

        elif izbor == "6":
            naslov = input("Unesite naslov knjige koju zelite urediti: ")
            rezultat = biblioteka.pretrazi_po_naslovu(naslov)
            if rezultat:
                knjiga = rezultat[0]
                print("Pronadjna knjiga:", knjiga)
                print("Sta zelite urediti?")
                print("1. Naslov")
                print("2. Autor")
                print("3. Godina izdanja")
                print("4. Broj kopija")
                podizbor = input("Izaberite: ")

                if podizbor == "1":
                    knjiga.naslov = input("Unesite novi naslov: ")
                elif podizbor == "2":
                    knjiga.autor = input("Unesite novog autora: ")
                elif podizbor == "3":
                    knjiga.godina_izdanja = int(input("Unesite novu godinu izdanja: "))
                elif podizbor == "4":
                    knjiga.br_kopija = int(input("Unesite novi broj kopija: "))
                print("Knjiga je uspjesno azurrirana!")
            else:
                print("Knjiga nije pronadjena.")

        elif izbor == "0":
            print("Izlaz iz programa...")
            break

        else:
            print("Nepostojeca opcija, pokusajte ponovo.")




class Company:
    def __init__(self, name: str, area: str, balance: float, max_num_of_employees: int):
        self.__name = name
        self.__area = area
        self.__employees = []
        self.__balance = balance
        self.__max_num_of_employees = max_num_of_employees

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance

    def get_max_num_of_employees(self):
        return self.__max_num_of_employees

    def set_max_num_of_employees(self, num):
        if num >= 0:
            self.__max_num_of_employees = num

    def add_employee(self, employee):
        if len(self.__employees) < self.__max_num_of_employees:
            self.__employees.append(employee)

    def remove_employee(self, employee_name, employee_surname):
        for emp in self.__employees:
            if emp["name"] == employee_name and emp["surname"] == employee_surname:
                self.__employees.remove(emp)
                break


