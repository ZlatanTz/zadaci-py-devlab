def best_students(names, grades):
    return [(name, grade) for name, grade in zip(names, grades) if grade > 8.5]


def reduce(func, items, initial):
    result = initial
    for x in items:
        result = func(result, x)
    return result


def average_per_subject(data):
    subjects = set(map(lambda x: x[2], data))  
    result = {}

    for subject in subjects:
        
        subject_grades = list(map(lambda x: x[1], filter(lambda x: x[2] == subject, data)))

        
        total = reduce(lambda a, b: a + b, subject_grades, 0)

        result[subject] = total / len(subject_grades) if subject_grades else 0

    return result












def append_to_file(list_of_students, filename="students.txt"):
    
    
    lines = []
    for s in list_of_students:
        line = f'{s["ime"]},{s["prezime"]},{int(s["godina"])},{float(s["prosjek"])}'
        lines.append(line)

    
    with open(filename, "a", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")






def get_students_with_greater_grade(year, grade_letter, filename="students.txt"):
    
    
    min_by_letter = {"A": 9.5, "B": 8.5, "C": 7.5, "D": 6.5, "E": 6.0}
    if grade_letter not in min_by_letter:
        raise ValueError("grade_letter must be one of A, B, C, D, E")

    threshold = min_by_letter[grade_letter]
    result = []

    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(",")
                if len(parts) != 4:
                    continue  
                ime, prezime, godina_str, prosjek_str = parts
                try:
                    godina = int(godina_str)
                    prosjek = float(prosjek_str)
                except ValueError:
                    continue

                if godina == year and prosjek >= threshold:
                    result.append({
                        "ime": ime,
                        "prezime": prezime,
                        "godina": godina,
                        "prosjek": prosjek
                    })
    except FileNotFoundError:
        
        pass

    return result





if __name__ == "__main__":
    
    initial_students = [
        {"ime": "Marko", "prezime": "Markovic", "godina": 2, "prosjek": 8.6},
        {"ime": "Boris", "prezime": "Boricic", "godina": 3, "prosjek": 7.9},
        {"ime": "Novak", "prezime": "Novovic", "godina": 3, "prosjek": 6.9},
    ]

    
    open("students.txt", "w", encoding="utf-8").close()
    append_to_file(initial_students)

    
    more_students = [
        {"ime": "Ana", "prezime": "Anic", "godina": 3, "prosjek": 9.6},   
        {"ime": "Mila", "prezime": "Milic", "godina": 3, "prosjek": 8.5}, 
        {"ime": "Ivan", "prezime": "Ivanic", "godina": 2, "prosjek": 6.4} 
    ]
    append_to_file(more_students)

    
    res1 = get_students_with_greater_grade(3, "C")
    print("Test 1, year=3, C:", res1)
    

    
    res2 = get_students_with_greater_grade(3, "A")
    print("Test 2, year=3, A:", res2)
    

    
    res3 = get_students_with_greater_grade(2, "E")
    print("Test 3, year=2, E:", res3)
    





import os
from datetime import datetime

ALLOWED_GENRES = [
    "action", "adventure", "rpg", "strategy", "shooter",
    "puzzle", "sports", "racing", "horror", "simulation"
]

CURRENT_YEAR = datetime.now().year



def parse_line_to_fields(line):
    parts = [p.strip() for p in line.strip().split(";")]
    if len(parts) != 5:
        return None
    name, rating_str, year_str, publisher, genres_str = parts
    return name, rating_str, year_str, publisher, genres_str

def is_valid_name(name):
    return isinstance(name, str) and 2 <= len(name) <= 50

def is_valid_rating(rating_str):
    try:
        val = float(rating_str)
        rounded = round(val, 2)
        return 1.0 <= rounded <= 10.0
    except ValueError:
        return False

def normalize_rating(rating_str):
    return round(float(rating_str), 2)

def is_valid_year(year_str):
    try:
        y = int(year_str)
        return 1950 < y < CURRENT_YEAR
    except ValueError:
        return False

def normalize_year(year_str):
    return int(year_str)

def is_valid_publisher(pub):
    if pub == "":
        return True
    return 2 <= len(pub) <= 40

def is_valid_genres(genres_str):
    genres = [g for g in genres_str.split(" ") if g]
    if len(genres) == 0 or len(genres) > 3:
        return False
    return all(g in ALLOWED_GENRES for g in genres)

def normalize_genres(genres_str):
    return [g for g in genres_str.split(" ") if g]

def validate_line(line):
    fields = parse_line_to_fields(line)
    if fields is None:
        return False, "neispravan format linije"
    name, rating_str, year_str, publisher, genres_str = fields

    
    name = name.lower()
    publisher = publisher.lower()
    genres_str = genres_str.lower()

    if not is_valid_name(name):
        return False, "neispravan naziv"
    if not is_valid_rating(rating_str):
        return False, "neispravna ocjena"
    if not is_valid_year(year_str):
        return False, "neispravna godina"
    if not is_valid_publisher(publisher):
        return False, "neispravan izdavac"
    if not is_valid_genres(genres_str):
        return False, "neispravni zanrovi dozvoljeni su: " + ", ".join(ALLOWED_GENRES)

    game = {
        "naziv": name,
        "ocjena": normalize_rating(rating_str),
        "godina": normalize_year(year_str),
        "izdavac": publisher,
        "zanrovi": normalize_genres(genres_str)
    }
    return True, game



def filter_file_to_valid(filename="igrice.txt", output_filename="igrice_filtered.txt"):
    valid_games = []
    invalid_lines = []

    if not os.path.exists(filename):
        print("fajl igrice txt ne postoji dodajte ga rucno prije pokretanja")
        return valid_games

    with open(filename, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            if not line.strip():
                continue
            ok, res = validate_line(line)
            if ok:
                valid_games.append(res)
            else:
                invalid_lines.append((idx, line.strip(), res))

    with open(output_filename, "w", encoding="utf-8") as out:
        for g in valid_games:
            out.write(f'{g["naziv"]};{g["ocjena"]:.2f};{g["godina"]};{g["izdavac"]};{" ".join(g["zanrovi"])}\n')

    print("ispravne igre nakon filtriranja")
    if not valid_games:
        print("nema ispravnih igara")
    for g in valid_games:
        pub = g["izdavac"] if g["izdavac"] else "(nema izdavaca)"
        print(f'{g["naziv"]};{g["ocjena"]:.2f};{g["godina"]};{pub};{" ".join(g["zanrovi"])}')

    if invalid_lines:
        print("neispravne linije iz pocetnog fajla")
        for idx, content, reason in invalid_lines:
            print(f"linija {idx}: '{content}' razlog: {reason}")

    return valid_games

def append_games_to_file(games, filename="igrice_filtered.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        for g in games:
            f.write(f'{g["naziv"]};{g["ocjena"]:.2f};{g["godina"]};{g["izdavac"]};{" ".join(g["zanrovi"])}\n')



def prompt_yes_no(prompt):
    while True:
        ans = input(prompt + " [y/n]: ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("unesite y ili n")

def prompt_new_game():
    print("unesite novu igru u trazenom formatu")
    print("dozvoljeni zanrovi su " + ", ".join(ALLOWED_GENRES))
    print("izdavac moze biti prazan maksimalno 3 zanra odvojena razmakom")
    print("ocjena je broj od 1 do 10 sa dvije decimale")
    print("primjer unos: gta 5;9.50;2013;rockstar;action adventure")

    raw = input("unos: ").strip().lower()
    ok, res = validate_line(raw)
    if ok:
        return res
    print("greska " + str(res))
    return None

def interactive_add_games(output_filename="igrice_filtered.txt"):
    if not prompt_yes_no("zelite li unijeti nove igre"):
        return

    added = []
    while True:
        game = prompt_new_game()
        if game is not None:
            added.append(game)
            print("igra je prihvacena")
        else:
            if not prompt_yes_no("unos je neispravan zelite li pokusati ponovo"):
                break

        if not prompt_yes_no("zelite li unijeti jos jednu igru"):
            break

    if added:
        append_games_to_file(added, output_filename)
        print(f"dodato {len(added)} igara u {output_filename}")



def load_games(filename="igrice_filtered.txt"):
    games = []
    if not os.path.exists(filename):
        return games
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            ok, res = validate_line(line)
            if ok:
                games.append(res)
    return games



def filter_by_name_prefix(games, term):
    term_low = term.lower()
    return [g for g in games if g["naziv"].lower().startswith(term_low)]

def filter_by_rating_min(games, min_rating):
    return [g for g in games if g["ocjena"] >= min_rating]

def filter_by_year(games, year, mode):
    if mode == "before":
        return [g for g in games if g["godina"] < year]
    elif mode == "after":
        return [g for g in games if g["godina"] > year]
    else:
        return []

def filter_by_publisher_prefix(games, term):
    term_low = term.lower()
    return [g for g in games if g["izdavac"] and g["izdavac"].lower().startswith(term_low)]

def filter_by_genres(games, genres):
    wanted = set(g.lower() for g in genres)
    return [g for g in games if wanted.issubset(set(x.lower() for x in g["zanrovi"]))]

def print_games(games, title="rezultati"):
    print(title)
    if not games:
        print("nema rezultata")
        return
    for g in games:
        pub = g["izdavac"] if g["izdavac"] else "(nema izdavaca)"
        print(f'{g["naziv"]};{g["ocjena"]:.2f};{g["godina"]};{pub};{" ".join(g["zanrovi"])}')



def interactive_filtering(games):
    while True:
        print("odaberite filtriranje")
        print("1 po nazivu igre koje pocinju zadatim terminom")
        print("2 po ocjeni igre sa ocjenom vecom ili jednakom od zadate")
        print("3 po godini prije ili poslije unijete godine")
        print("4 po izdavacu koji pocinje zadatim terminom")
        print("5 po zanru ili vise zanrova do 3 komada")
        print("0 kraj")

        choice = input("izbor: ").strip().lower()
        if choice == "0":
            break
        elif choice == "1":
            term = input("unesite pocetni termin naziva: ").strip().lower()
            print_games(filter_by_name_prefix(games, term))
        elif choice == "2":
            print("napomena ocjene su od 1 do 10")
            try:
                val = float(input("minimalna ocjena: ").strip())
            except ValueError:
                print("neispravan broj")
                continue
            if not (1.0 <= val <= 10.0):
                print("ocjena mora biti izmedju 1 i 10")
                continue
            print_games(filter_by_rating_min(games, round(val, 2)))
        elif choice == "3":
            try:
                y = int(input("godina: ").strip())
            except ValueError:
                print("neispravna godina")
                continue
            mode = input("unesite before za prije ili after za poslije: ").strip().lower()
            if mode not in ("before", "after"):
                print("neispravan izbor")
                continue
            print_games(filter_by_year(games, y, mode))
        elif choice == "4":
            term = input("unesite pocetni termin izdavaca: ").strip().lower()
            print_games(filter_by_publisher_prefix(games, term))
        elif choice == "5":
            print("dozvoljeni zanrovi su " + ", ".join(ALLOWED_GENRES))
            raw = input("unesite 1 do 3 zanra odvojena razmakom: ").strip().lower()
            genres = [g for g in raw.split(" ") if g]
            if not (1 <= len(genres) <= 3) or any(g not in ALLOWED_GENRES for g in genres):
                print("neispravan unos zanrova")
                continue
            print_games(filter_by_genres(games, genres))
        else:
            print("nepoznata opcija")



def main():
    filter_file_to_valid("igrice.txt", "igrice_filtered.txt")
    interactive_add_games("igrice_filtered.txt")
    games = load_games("igrice_filtered.txt")
    interactive_filtering(games)

if __name__ == "__main__":
    main()
