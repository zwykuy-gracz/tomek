# Zagnieżdżone Listy:
# Stwórz listę zawierającą listy liczb całkowitych. Następnie napisz kod, który obliczy sumę
# wszystkich liczb w tych zagnieżdżonych listach.

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 0
for i in nested_lists:
    for j in i:
        k += j
# print(k)

# Słownik z Listami:
# Stwórz słownik, w którym klucze to imiona osób, a wartościami są listy ich ulubionych kolorów. 
# Dodaj kilka osób i ich kolory, a następnie napisz kod, który znajdzie osobę z największą liczbą
# ulubionych kolorów.
favorites = {
 "Alice": ["blue", "green", "red"],
 "Bob": ["green", "purple"],
 "Charlie": ["blue", "yellow", "red"],
 "George": ["blue", "yellow", "red", "pink"]
}
longest = 0
names = []
for k, v in favorites.items():
    if len(v) > longest:
        longest = len(v)
for k, v in favorites.items():
    if len(v) == longest:
        names.append(k)
# print(names)

# Operacje na Zbiorach:
# Stwórz dwa zbiory zawierające liczby całkowite. Napisz funkcję, która zwróci zbiór zawierający 
# tylko te liczby, które są wspólne dla obu zbiorów.
common_part = set()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
for i in set1:
    if i in set2:
        common_part.add(i)
# print(common_part)
intersection_1 = set1 & set2
intersection_2  = set1.intersection(set2)
print(intersection_2)

# Zagnieżdżone Słowniki:
# Stwórz zagnieżdżony słownik, który reprezentuje katalog książek. Każda książka powinna mieć
# unikalny numer ISBN. Napisz funkcję, która po numerze ISBN zwróci tytuł książki.
catalog = {
 "978-0451524935": {"title": "1984", "author": "George Orwell"},
 "978-0141036137": {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
}
def book_search(isbn):
    for k, v in catalog.items():
        if k == isbn:
            print(v['title'])
# book_search("978-0141036137")


# Operacje na Liście Słowników:
# Masz listę słowników, gdzie każdy słownik reprezentuje studenta z danymi takimi jak "imię", 
# "nazwisko" i "oceny". Napisz funkcję, która obliczy średnią ocen wszystkich studentów w liście.
students = [
 {"name": "Alice", "grades": [85, 90, 78]},
 {"name": "Bob", "grades": [92, 88, 94]},
 {"name": "Charlie", "grades": [78, 85, 80]}
]

def average_grade(students_list):
    for student in students_list:
        avg = round(sum(student['grades']) / len(student['grades']), 2)
        print(avg)

# average_grade(students)

# Kontrola Powtórzeń w Liście:
# Masz listę zawierającą duplikaty elementów. Napisz kod, który usunie wszystkie powtarzające się
# elementy, zachowując pierwotny porządek.
input_list = [4, 1, 2, 2, 3, 4, 4, 5]
output_set = set(input_list)
#print(output_set) 
# nie wiem czy o to chodzi, ale samo sortuje. W collections jest też SortedSet jakby co

# Słownik z Zagnieżdżonymi Słownikami:
# Stwórz słownik, w którym kluczami są nazwy państw, a wartościami są słowniki z informacjami o 
# stolicach i populacji tych państw. Napisz kod, który znajdzie państwo o największej populacji.
countries = {
 "USA": {"capital": "Washington, D.C.", "population": 331002651},
 "China": {"capital": "Beijing", "population": 1444216107},
 "India": {"capital": "New Delhi", "population": 1380004385}
}
greatest_population = 0
searched_country = ''
for k, v in countries.items():
    if v['population'] > greatest_population:
        greatest_population = v['population']
        searched_country = k
# print(searched_country)

# Wyszukiwanie w Zagnieżdżonych Strukturach:
# Masz zagnieżdżoną listę słowników, reprezentującą dane o produktach w sklepie. Napisz funkcję, 
# która znajdzie wszystkie produkty, których cena jest wyższa niż 100 złotych.
products = [
 {"name": "Laptop", "price": 1200},
 {"name": "Phone", "price": 800},
 {"name": "Tablet", "price": 300},
 {"name": "TV", "price": 1500}
]

def more_than_100(products_list):
    for i in products_list:
        if i['price'] > 100:
            print(f"found {i['name']}")

# more_than_100(products)

# Filtrowanie na Podstawie Listy:
# Masz listę słowników reprezentujących osoby z danymi takimi jak "imię," "wiek" i "miasto." Napisz 
# funkcję, która przyjmuje listę miast i zwraca listę osób, które mieszkają w tych miastach.
people = [
 {"name": "Alice", "city": "New York"},
 {"name": "Bob", "city": "Los Angeles"},
 {"name": "Charlie", "city": "Chicago"},
 {"name": "George", "city": "Chicago"},
]
city_list = ['New York', 'Chicago', 'Wroclaw']

def leaves_inThe_city(ppl, cities = []):
    ppl_list = []
    for city in cities:
        for person in ppl:
            if city == person['city']:
                ppl_list.append(person['name'])
    return ppl_list

people_inThe_city = leaves_inThe_city(people, city_list)
# print(people_inThe_city)

# Grupowanie i Liczenie:
# Masz listę produktów z danymi o kategoriach. Napisz funkcję, która zgrupuje produkty według 
# kategorii i obliczy liczbę produktów w każdej kategorii.
products = [
 {"category": "Electronics", "name": "Laptop"},
 {"category": "Electronics", "name": "Phone"},
 {"category": "Clothing", "name": "T-Shirt"},
 {"category": "Electronics", "name": "Tablet"},
 {"category": "Clothing", "name": "Jeans"}
]

from collections import defaultdict

def grouped_products(prods):
    products_dict = defaultdict(list)
    for prod in prods:
        products_dict[prod['category']].append(prod['name'])

    for k, v in products_dict.items():
        print(f"Category {k} has {len(v)} items")
    print(products_dict)

# grouped_products(products)

# Zagnieżdżone Zbiory:
# Stwórz listę zawierającą zbiory liczb całkowitych. 
# Napisz funkcję, która zwróci sumę wszystkich 
# liczb w tych zagnieżdżonych zbiorach.
nested_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]

def sum_all_sets(list_of_sets):
    sum_all = 0
    for x in list_of_sets:
        for y in x:
            sum_all += y
    return sum_all

sum_of_all = sum_all_sets(nested_sets)
# print(sum_of_all)

# Słownik z Funkcjami:
# Stwórz słownik, w którym kluczami są operacje matematyczne (np. "Dodawanie", "Mnożenie") i 
# przypisz do każdej z tych operacji odpowiednią funkcję. Następnie napisz kod, który przyjmuje 
# dwie liczby i nazwę operacji i wykonuje odpowiednią operację na tych liczbach, korzystając z 
# funkcji zdefiniowanych w słowniku

def adding_numbers(a, b):
    return a + b

def subtraction_numbers(a, b):
    return a - b

def multiplication_numbers(a, b):
    return a * b

def dividing_numbers(a, b):
    return a / b

operations = {
    'addition': adding_numbers,
    'subtraction': subtraction_numbers,
    'multiplication': multiplication_numbers,
    'dividing': dividing_numbers,
}

def calculator(x, y, operation):
    return operations[operation](x, y)

result = calculator(1, 2, 'subtraction')
# print(result)

# Średnia Długość Słów w Zdaniu:
# Napisz funkcję, która przyjmuje zdanie jako ciąg tekstowy i zwraca średnią długość słów w tym 
# zdaniu. Użyj słownika, aby śledzić liczbę słów o różnych długościach.

from collections import Counter
sentence = "To jest przykładowe zdanie do obliczenia średniej długości słów asdf."

def avg_word_lenght(example_sentence):
    dict_of_words = {}
    list_lenght = [] # lenght of each word
    total_lenght = 0
    list_of_words = example_sentence.split()
    for word in list_of_words:
        list_lenght.append(len(word))
        total_lenght += len(word)

    elements_count = Counter(list_lenght)

    for k, v in elements_count.items():
        print(f"{k}: {v}")
    return int(total_lenght / len(list_of_words))

# print(f"Average lenght: {avg_word_lenght(sentence)}")

# Suma Liczb w Liście na Kolejnych Poziomach Zagnieżdżenia:
# Masz listę zagnieżdżonych list liczb całkowitych. Napisz funkcję, która oblicza sumę liczb na 
# kolejnych poziomach zagnieżdżenia i zwraca listę wyników.

nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
def sum_of_each_list(list_of_lists):
    for l in list_of_lists:
        print(sum(l))

# sum_of_each_list(nested_lists)

# Liczba Wystąpień w Liście:
# Masz listę elementów. Napisz funkcję, która używa collections.Counter do zliczania liczby 
# wystąpień każdego elementu w liście i zwraca słownik, w którym kluczami są elementy, a 
# wartościami są ich liczby wystąpień.
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
def counter_dict(input_list):
    elements_count = Counter(input_list)
    return elements_count

# print(counter_dict(my_list))

# Stos z Deque:
# Stwórz prosty stos (LIFO - Last-In, First-Out) używając struktury deque z modułu collections. 
# Zaimplementuj operacje push, pop i peek (zwracanie wartości na szczycie stosu bez usuwania). 
# Przetestuj działanie stosu dodając i usuwając elementy
from collections import deque

de = deque([1, 2, 3])
de.append(4) # push. appendleft
# print(de)
de.pop() # popleft()
# print(de)
# print(de[-1]) # peek

# Grupowanie Elementów w Liście:
# Masz listę elementów. Napisz funkcję, która używa collections.defaultdict do grupowania tych 
# elementów według ich długości (ilości znaków) w słownik, gdzie kluczami są długości, a 
# wartościami są listy elementów o danej długości.

from collections import defaultdict

my_list = ["apple", "banana", "cherry", "date", "fig"]

def word_lenght_dict(list_of_words):
    grouped = defaultdict(int)
    for w in list_of_words:
        grouped[len(w)] += 1
    print(grouped)

# word_lenght_dict(my_list)

# Kalkulator Wyników Wyborów:
# Stwórz słownik, w którym kluczami są nazwy kandydatów, 
# a wartościami są głosy oddane na tych kandydatów. 
# Następnie użyj collections.Counter, aby znaleźć zwycięzcę wyborów.
votes = {"Candidate A": 350, "Candidate B": 420, "Candidate C": 280}

winner = max(votes, key=votes.get) # nie mam pojęcia jak tu użyć Counter. Counter by stworzył ten dict jeżeli byś mieli listę ze wszystkimi wynikami głosowania
# print(winner)

# Grupowanie Studentów:
# Masz listę słowników reprezentujących studentów z danymi takimi jak "imię," "wiek" i "miasto." 
# Użyj collections.defaultdict, aby grupować studentów według miast.
students = [
 {"name": "Alice", "city": "New York"},
 {"name": "Bob", "city": "Los Angeles"},
 {"name": "Charlie", "city": "New York"},
 {"name": "George", "city": "Los Angeles"},
]

from_city = defaultdict(list)
for s in students:
    from_city[s['city']].append(s['name'])
# print(from_city)

# Średnia Długość Słów w Zdaniach:
# Masz listę zdań. 
# Napisz funkcję, która używa collections.Counter do zliczania średniej długości 
# słów we wszystkich zdaniach.
sentences = ["To jest pierwsze zdanie.", "To jest drugie zdanie."]
split_list = []
count_list = []
for s in sentences:
    split_list.append(s.split())
for s in split_list:
    for w in s:
        count_list.append(w)
count_list = [i.replace(".", "") for i in count_list]
# print(count_list)
elements_count = Counter(count_list)
# print(elements_count) # nie mam pojęcia jak użyć tutaj Counter 

# Liczenie Liter w Tekście:
# Napisz funkcję, która używa collections.Counter, aby zliczyć liczbę wystąpień każdej litery w 
# danym tekście.
text = "To jest przykład tekstu, w którym liczymy wystąpienia liter."
text_stripped = text.replace(" ", "")
letters_count = Counter(text_stripped)
# print(letters_count)

# Suma Liczb w Zagnieżdżonej Liście:
# Masz zagnieżdżoną listę zawierającą liczby całkowite. 
# Użyj rekursji i collections.Counter, aby 
# obliczyć sumę wszystkich liczb w tej zagnieżdżonej liście.
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] #TODO

# Grupowanie Produktów według Kategorii:
# Masz listę słowników reprezentujących produkty z danymi takimi jak "nazwa" i "kategoria". 
# Użyj collections.defaultdict, aby grupować produkty według kategorii.
products = [
 {"name": "Laptop", "category": "Electronics"},
 {"name": "T-Shirt", "category": "Clothing"},
 {"name": "Phone", "category": "Electronics"},
 {"name": "Jeans", "category": "Clothing"}
]
grouped_products = defaultdict(list)
for p in products:
    grouped_products[p['category']].append(p['name'])
# print(grouped_products)

# Słownik z Zagnieżdżonymi Słownikami i Listami:
# Stwórz słownik zagnieżdżony, który reprezentuje katalog książek. 
# Każda książka powinna mieć
# unikalny numer ISBN, a informacje o książkach powinny zawierać listę autorów. 
# Użyj collections.defaultdict lub collections.defaultdict(list).

catalog = {
 "978-0451524935": {"title": "1984", "author": "George Orwell"},
 "978-0141036137": {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
} #TODO

# Zestawienie Wyników Egzaminów:
# Masz listę słowników reprezentujących wyniki egzaminów uczniów. Każdy słownik zawiera "imię", 
# "wynik" i "przedmiot". Użyj collections.defaultdict, aby zestawić wyniki uczniów według 
# przedmiotów.
exam_results = [
 {"name": "Alice", "subject": "Math", "score": 90},
 {"name": "Bob", "subject": "Math", "score": 85},
 {"name": "Charlie", "subject": "Science", "score": 92}
]

subject_score = defaultdict(list)
for e in exam_results:
    subject_score[e['subject']].append(e['name'])

# print(subject_score)

# Grupowanie na Podstawie Warunków:
# Masz listę słowników reprezentujących samochody z danymi takimi jak "marka", "model" i "rok 
# produkcji". Użyj collections.defaultdict, aby grupować samochody według roku produkcji, ale 
# tylko te, których rok produkcji jest nowszy niż 2010.
cars = [
 {"brand": "Toyota", "model": "Camry", "year": 2015},
 {"brand": "Honda", "model": "Civic", "year": 2010},
 {"brand": "Ford", "model": "Fusion", "year": 2012},
 {"brand": "Toyota", "model": "Corolla", "year": 2020}
]
car_order = defaultdict(list)
for c in cars:
    if c['year'] > 2010:
        car_order[c['year']].append(c['model'])

# print(car_order)

# Sortowanie Bąbelkowe na Liście:
# Napisz funkcję, która implementuje sortowanie bąbelkowe na liście liczb całkowitych. Sortowanie 
# bąbelkowe polega na wielokrotnym przechodzeniu przez listę i zamianie miejscami sąsiednich 
# elementów, jeśli są one w niewłaściwej kolejności, aż lista będzie posortowana rosnąco. Zwróć
# posortowaną listę.
my_list = [64, 25, 12, 22, 11]

def bubble(st):
    for i in range(len(st),1,-1):
        for j in range(0,i-1):
            if st[j]>st[j+1]:
                st[j],st[j+1]=st[j+1],st[j]
            else:
                pass
    return st
# print(bubble(my_list))

# Sortowanie Bąbelkowe na Zagnieżdżonej Liście:
# Masz listę zagnieżdżoną zawierającą listy liczb całkowitych. 
# Napisz funkcję, która implementuje 
# sortowanie bąbelkowe na każdej zagnieżdżonej liście i zwraca listę zagnieżdżoną z 
# posortowanymi podlistami.
my_nested_list = [[64, 25, 12], [22, 11], [100, 1, 5, 78, 45]]

def nested_bubble(st):
    for n in st:
        for i in range(len(n),1,-1):
            for j in range(0,i-1):
                if n[j]>n[j+1]:
                    n[j],n[j+1]=n[j+1],n[j]
                else:
                    pass
    return st

# print(nested_bubble(my_nested_list))

# Dodawanie Macierzy:
# Napisz funkcję, która przyjmuje dwie macierze (reprezentowane jako listy list) i zwraca wynik ich 
# dodawania. Upewnij się, że macierze mają takie same wymiary.
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

def matrix_addition(m1, m2):
    if len(m1) != len(m2):
        return "Addition can't be done"
    else:
        result = [[0, 0], [0, 0]]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j] = m1[i][j] + m2[i][j]
        return result

matrix_add = matrix_addition(matrix1, matrix2)
# print(matrix_add)

# Mnożenie Macierzy:
# Napisz funkcję, która przyjmuje dwie macierze i zwraca wynik ich mnożenia. Upewnij się, że liczba 
# kolumn pierwszej macierzy jest równa liczbie wierszy drugiej macierzy.
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

def multiply_matrix(m1, m2):
    if len(m1[0]) != len(m2):
        return "matrix multiplication can't be done"   
    f = []
    for i in range(len(m1)):
        f.append([])
        for j in range(len(m2[0])):
            f[i].append(0)
            for index in range(len(m2)):
                f[i][j] += m1[i][index] * m2[index][j]    
    return f

multiplication_matrix = multiply_matrix(matrix1, matrix2)
# print(multiplication_matrix)

# Transpozycja Macierzy:
# Napisz funkcję, która przyjmuje macierz i zwraca jej transpozycję, czyli macierz o wymienionych 
# wierszach i kolumnach.
matrix = [[1, 2, 3], [4, 5, 6]]


def transpozition_matrix(m):
    result = [[0,0],
            [0,0],
            [0,0]]
    for i in range(len(m)):
        for j in range(len(m[0])):
            result[j][i] = m[i][j]

    for r in result:
        print(r)

# transpozition_matrix(matrix)

# Obliczanie Wyznacznika Macierzy 2x2:
# Napisz funkcję, która oblicza wyznacznik macierzy 2x2.
matrix = [[3, 4], [1, 2]] #TODO