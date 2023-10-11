# Zadanie: Tworzenie Klasy Osoby
# Stwórz klasę o nazwie Person, która reprezentuje osobę. Klasa ta powinna mieć następujące 
# atrybuty:
# name (imię)
# age (wiek)
# city (miasto)
# Klasa Person powinna również mieć następujące metody:
# __init__(self, name, age, city): Konstruktor, który inicjuje atrybuty obiektu na podstawie 
# przekazanych argumentów.
# greet(self): Metoda, która wypisuje przywitanie osoby w formacie "Hello, Imię! Jestem z Miasta. 
# Mam X lat." (gdzie Imię, Miasto i X to odpowiednie atrybuty obiektu).
# Napisz kod, który tworzy obiekty klasy Person i wywołuje ich metody. Przykładowo:
# Oczekiwane wyjście:
# Hello, Alice! Jestem z Nowy Jork. Mam 30 lat.
# Hello, Bob! Jestem z Los Angeles. Mam 25 lat.

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def greet(self):
        print(f"Hello {self.name}! I'm from {self.city}, I'm {self.age} years old")

# person1 = Person("Alice", 30, "Nowy Jork")
# person2 = Person("Bob", 25, "Los Angeles")
# person1.greet()
# person2.greet()

# Stwórz klasę Person z atrybutami name i age. Następnie stwórz podklasę Student, która 
# dziedziczy po klasie Person i dodaje atrybut student_id. Stwórz obiekty obu klas i wyświetl ich 
# właściwości.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized person {self.name}, age {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        Person.__init__(self, name, age)
        self.student_id = student_id
        print(f"Initialized student with id {self.student_id}")

# p1 = Person("Bob", 20)
# s1 = Student("Bob", 20, 321)
# print(s1)

# Stwórz abstrakcyjną klasę AbstractQueue z metodami abstrakcyjnymi enqueue(self, item) i 
# dequeue(self). Następnie utwórz konkretne implementacje kolejki, np. QueueFIFO (kolejka typu 
# FIFO - "First-In-First-Out") i QueueLIFO (kolejka typu LIFO - "Last-In-First-Out"), które dziedziczą
# po AbstractQueue i zaimplementuj odpowiednie metody. #TODO

# Stwórz klasę BankAccount, która ma atrybuty account_number, owner_name i balance. Dodaj 
# metody do wpłaty i wypłaty środków. Napisz też metodę __str__, która zwraca czytelny opis 
# konta.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance += dep_amount

    def withdrawal(self, with_amount):
        if with_amount > self.balance:
            print("not enough of mana")
        else:
            self.balance -= with_amount

    def __str__(self):
        return f"Acount number {self.account_number} belongs to {self.owner_name} has balance of {self.balance}"

# b = BankAccount(123, 'Bob', 11)
# print(b)
# b.deposit(22)
# print(b)
# b.withdrawal(3)
# print(b)

# Stwórz abstrakcyjną klasę Shape z metodą abstrakcyjną area(self), która będzie obliczać pole 
# powierzchni danej figury geometrycznej. Następnie stwórz dwie konkretne implementacje: Circle 
# (koło) i Rectangle (prostokąt) oraz zaimplementuj ich metody area

from abc import ABC
class Shape(ABC): 
    def area(self): 
        pass
  
class Circle(Shape): 
    def area(self, r): 
        return 3.14 * r * r
  
class Rectangle(Shape): 
    def area(self, a, b): 
        return a * b

# c = Circle()
# print(c.area(2))

# r = Rectangle()
# print(r.area(2, 3))

# Stwórz klasę EventList, która reprezentuje listę wydarzeń. Klasa ta powinna mieć atrybut events 
# jako listę, a także metody do dodawania (add_event(self, event)) i usuwania (remove_event(self, 
# event)) wydarzeń. Wydarzenia mogą być reprezentowane jako napisy

class EventList:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
        else:
            print("no such event")

    # def __str__(self):
    #     return f""

# e = EventList()
# e.add_event('asd')
# e.add_event('qwe')
# e.remove_event('asd')
# print(e.events)

# Stwórz klasę Card, która reprezentuje kartę do gry. Karta powinna mieć atrybuty rank (figura) i suit 
# (kolor). Następnie stwórz klasę Deck, która reprezentuje talie kart. Klasa Deck powinna mieć
# metody do tasowania (shuffle(self)) i rozdawania (deal(self)) kart

# class Card:
#     def __init__(self):
#         pass #TODO

# Stwórz klasę Task, która reprezentuje zadanie do wykonania. Zadanie powinno mieć atrybuty 
# description (opis) i completed (czy zostało zakończone). Następnie stwórz klasę TaskList, która 
# będzie przechowywać listę zadań (tasks) i mieć metody do dodawania (add_task(self, task)), 
# usuwania (remove_task(self, task)), i oznaczania zadań jako zakończone (complete_task(self, 
# task))

class Task:
    description = ''
    completed = False

class TaskList(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.description = task
        self.tasks.append(self.description)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("no such task")
    
    def complete_task(self, task):
        self.completed = True

# t = TaskList()
# t.add_task('coffee')
# print(t.tasks)
# print(t.completed)
# t.complete_task('coffee')
# print(t.completed)

# Stwórz klasę Ticket, która reprezentuje bilet na wydarzenie. Bilet powinien mieć atrybuty, takie jak 
# event_name, ticket_price, quantity, itp. Następnie stwórz klasę TicketBookingSystem, która 
# będzie zarządzać rezerwacją biletów. Klasa ta powinna mieć metody do rezerwacji 
# (reserve_ticket(self, ticket, quantity)), odwołania rezerwacji (cancel_reservation(self, ticket, 
# quantity)), i wyświetlania dostępnych biletów (display_available_tickets(self)) #TODO

# twórz abstrakcyjną klasę Vehicle z atrybutem name oraz metodą abstrakcyjną start(). Następnie 
# stwórz dwie klasy dziedziczące po Vehicle: Car i Motorcycle. Klasa Car powinna implementować
# metodę start() tak, aby wypisywała "Samochód rusza". Klasa Motorcycle powinna 
# implementować metodę start() tak, aby wypisywała "Motocykl rusza".

class Vehicle(ABC):
    name = ''
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car moves")

class Motorcycle(Vehicle):
    def start(self):
        print("Motorcycle moves")

# c = Car()
# c.start()
# m = Motorcycle()
# m.start()

# Stwórz abstrakcyjną klasę Animal z atrybutem name oraz metodą abstrakcyjną make_sound(). 
# Następnie stwórz dwie klasy dziedziczące po Animal: Dog i Cat. Klasa Dog powinna 
# implementować metodę make_sound() tak, aby wypisywała "Woof!". Klasa Cat powinna 
# implementować metodę make_sound() tak, aby wypisywała "Meow!"

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")
    
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# d = Dog()
# d.make_sound()
# c = Cat()
# c.make_sound()

# Stwórz abstrakcyjną klasę Character z atrybutami name i health oraz metodą abstrakcyjną
# attack(). Następnie stwórz dwie klasy dziedziczące po Character: Player (gracz) i Enemy 
# (przeciwnik). Klasa Player powinna implementować metodę attack() tak, aby zadawała obrażenia 
# przeciwnikowi. Klasa Enemy powinna implementować metodę attack() tak, aby zadawała 
# obrażenia graczowi.

class Character:
    name = ''
    health = 10
    def attack(self):
        pass

class Player(Character):
    def __init__(self, name):
        self.name = name

    def attack(self):
        pass
#TODO

# Stwórz abstrakcyjną klasę Shape3D z atrybutem name oraz metodą abstrakcyjną volume(), która 
# będzie obliczać objętość danego kształtu 3D. Następnie stwórz dwie klasy dziedziczące po 
# Shape3D: Sphere (kula) i Cuboid (prostopadłościan). Klasa Sphere powinna przyjmować promień i 
# implementować metodę volume() obliczając objętość kuli. Klasa Cuboid powinna przyjmować
# długość, szerokość i wysokość oraz implementować metodę volume() obliczając objętość
# prostopadłościanu

class Shape3D:
    def volume(self):
        pass

class Sphere(Shape3D):
    def volume(self, radius):
        return 4/3 * 3.14 * radius**3

class Cuboid(Shape3D):
    def volume(self, l, w, h):
        return l * w * h

s = Sphere()
print(s.volume(2))
c = Cuboid()
print(c.volume(2,3,4))