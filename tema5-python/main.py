import math
from datetime import datetime, timedelta


# ex1---------------------------
# a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle,
# Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def ex1_test():
    circle = Circle(10)
    circle_area = circle.area()
    circle_perimeter = circle.perimeter()
    print("Circle area:", circle_area)
    print("Circle perimeter:", circle_perimeter)

    rectangle = Rectangle(3, 4)
    rectangle_area = rectangle.area()
    rectangle_perimeter = rectangle.perimeter()
    print("Rectangle area:", rectangle_area)
    print("Rectangle perimeter:", rectangle_perimeter)

    triangle = Triangle(3, 4, 5)
    triangle_area = triangle.area()
    triangle_perimeter = triangle.perimeter()
    print("Triangle area:", triangle_area)
    print("Triangle perimeter:", triangle_perimeter)


ex1_test()

# ex2---------------------------
class Account:
    def __init__(self, account_owner, total_amount=0):
        self.total_amount = total_amount
        self.account_owner = account_owner

    def deposit(self, deposit_amount):
        self.total_amount += deposit_amount
        print(f"Successful operation, you deposited {deposit_amount}$. Current amount: {self.total_amount}$")

    def withdrawal(self, withdrawal_amount):
        if self.total_amount >= withdrawal_amount:
            self.total_amount -= withdrawal_amount
            print(f"Successful operation, you extracted {withdrawal_amount}$. Current amount: {self.total_amount}$")
        else:
            print(f"Failed operation. Current amount: {self.total_amount}$. You can't extract {withdrawal_amount}")

    def check_total_amount(self):
        print(f"Current amount: {self.total_amount}$")

    def info(self):  # functia asta am facut o doar sa folosesc account_owner la ceva
        print(f"Hi, {self.account_owner}. The available operations are:")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Check current funds")


class SavingsAccount(Account):
    def __init__(self, account_owner, total_amount=0, interest_rate=0.1):
        super().__init__(account_owner, total_amount)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.total_amount * self.interest_rate
        self.total_amount += interest  # maresc cu interest_rate, total amount+total_amount*interest_rate
        print(f"Interest added: {interest}$. Current amount: {self.total_amount}$")

    def info(self):
        super().info()
        print("4. Calculate Interest")


class CheckingAccount(Account):
    def __init__(self, account_owner, total_amount=0, overdraft_limit=100):
        super().__init__(account_owner, total_amount)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.total_amount + self.overdraft_limit:
            self.total_amount -= amount
            print(f"Withdraw {amount}$. Current amount: {self.total_amount}$")
        else:
            print(f"Failed operation. Exceeded overdraft limit. Current amount: {self.total_amount}$")

    def info(self):
        super().info()
        print("4. Withdraw with overdraft")


def ex2():
    savings_account = SavingsAccount("Ana", 500, 0.5)
    savings_account.info()
    savings_account.deposit(200)
    savings_account.deposit(234)
    savings_account.withdrawal(100)
    savings_account.check_total_amount()
    savings_account.calculate_interest()

    checking_account = CheckingAccount("Maria", 500, 200)
    checking_account.info()
    checking_account.deposit(100)
    checking_account.deposit(300)
    checking_account.withdrawal(150)
    checking_account.check_total_amount()
    checking_account.withdraw_with_overdraft(600)
    '''
    account = Account("MARA")
    account.deposit(100)
    account.deposit(4300)
    account.withdrawal(5000)
    account.withdrawal(200)
    account.deposit(120)
    #ctrl alt l pt format ok
    '''


# ex2()


# ex3---------------------------

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self, distance_traveled, fuel_consumed):
        mileage = distance_traveled / fuel_consumed  # pe net zice The formula for mileage is: Mileage =
        # Total Distance Travelled / Total Fuel Consumed, deci toate au la fel? (nu mi plac masinilee)
        return mileage

    def calculate_towing_capacity(self):
        return 0  # pe net zice ca To find your truck's towing capacity, subtract your truck's curb weight from
        # its Gross Combined Vehicle Weight Rating (GCVWR), deci doar pt truck calculez?, in rest pun 0


class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self, distance_traveled, fuel_consumed):
        mileage = super().calculate_mileage(distance_traveled, fuel_consumed)
        return mileage


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self, distance_traveled, fuel_consumed):
        mileage = super().calculate_mileage(distance_traveled, fuel_consumed)
        return mileage


class Truck(Vehicle):
    def __init__(self, make, model, year, curb_weight, gcvwr):
        super().__init__(make, model, year)
        self.curb_weight = curb_weight
        self.gcvwr = gcvwr

    def calculate_towing_capacity(self):
        towing_capacity = self.gcvwr - self.curb_weight
        return towing_capacity


def ex3():
    car = Car("Ford", "Fiesta", 2015, 30)  # mileage ultima data
    car_mileage = car.calculate_mileage(100, 5)  # mileage curent
    print(f"Car Mileage: {car_mileage}")

    motorcycle = Motorcycle("Motocicleta1", "hh1te761qgu", 2023, 45)
    motorcycle_mileage = motorcycle.calculate_mileage(150, 5)
    print(f"Motorcycle Mileage: {motorcycle_mileage}")

    truck = Truck("Camion1", "7ekjwhj7", 2005, 5000, 12000)
    truck_towing_capacity = truck.calculate_towing_capacity()
    truck_mileage = truck.calculate_mileage(300, 11)
    print(f"Truck Mileage : {truck_mileage} ")
    print(f"Truck Towing Capacity: {truck_towing_capacity}")


# ex3()

# ex4---------------------------

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement this method")

    def schedule(self, day_of_week):
        if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            print(f"{self.name} is working on {day_of_week} [8-14]")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        total_salary = self.salary + self.bonus
        print(f"{self.name}, Manager, Salary: ${total_salary}")
        return total_salary

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting")

    def evaluate_team_performance(self):
        print(f"{self.name} is evaluating the team's performance")


class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        self.is_promoted = False

    def calculate_salary(self):
        if self.is_promoted:
            self.salary += self.salary * 0.2
            print(f"Engineer, {self.name}, Salary: ${self.salary}")
        return self.salary

    def promote(self):
        self.is_promoted = True
        print(f"{self.name} got a promotion!!!yey")

    def code(self):
        print(f"{self.name} is writing code")

    def debug(self):
        print(f"{self.name} is debugging code")

    def submit_code_review(self, code):
        print(f"{self.name} submitted code for review")


class Salesperson(Employee):
    def __init__(self, name, salary, commission_rate):
        super().__init__(name)
        self.salary = salary
        self.commission_rate = commission_rate
        self.made_sale = False

    def calculate_salary(self):
        total_salary = self.salary + (self.commission_rate * 1000)  # calc in functie de commision_rate
        print(f"{self.name}, Salesperson, Salary: ${total_salary}")
        return total_salary

    def make_sale(self):
        self.made_sale = True
        print(f"{self.name} made a sale")


def ex4():
    manager = Manager(name="Ana", salary=10000000, bonus=20000)
    manager_salary = manager.calculate_salary()
    print(f"Manager Salary: {manager_salary}")
    manager.evaluate_team_performance()
    manager.conduct_meeting()
    print()

    engineer = Engineer(name="Maria", salary=200000)
    engineer_salary = engineer.calculate_salary()
    print(f"Engineer Salary: {engineer_salary}")
    engineer.code()
    engineer.debug()
    engineer.promote()
    print()

    salesperson = Salesperson(name="Dan", salary=300000, commission_rate=0.2)
    salesperson_salary = salesperson.calculate_salary()
    print(f"SalesPerson Salary: {salesperson_salary}")
    salesperson.make_sale()
    print()

    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        manager.schedule(day)
        engineer.schedule(day)
        salesperson.schedule(day)


# ex4()


# ex5---------------------------

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")


class Mammal(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def give_birth(self):
        print(f"{self.name} is giving birth")  # mamif nasc pui, nu depun oua cica


class Bird(Animal):
    def __init__(self, name, age, maximum_height):
        super().__init__(name, age)
        self.maximum_height = maximum_height

    def fly(self):
        print(f"The bird {self.name} flies")

    def sing(self):
        print(f"The bird {self.name} is cipciriping")


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def swim(self):
        print(f"{self.name} is swimming")

    def hide_in_coral(self):
        print(f"{self.name} is hiding in the coral reef")


def ex5():
    elephant = Mammal(name="Elephant", age=10, habitat="Jungle")
    elephant.eat()
    elephant.give_birth()

    pigeon = Bird(name="Pigeon", age=1, maximum_height=30)
    pigeon.eat()
    pigeon.fly()
    pigeon.sing()

    goldfish = Fish(name="Nemo", age=1)
    goldfish.eat()
    goldfish.swim()
    goldfish.hide_in_coral()


# ex5()

# ex6---------------------------

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
        self.due_date = None

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.now() + timedelta(days=10)  # imprumut de 10 zile
            print(f"{self.title} has been checked out. Due date: {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            overdue_days = max(0, (datetime.now() - self.due_date).days)
            self.checked_out = False
            self.due_date = None
            print(f"{self.title} has been returned. Overdue days: {overdue_days}")
        else:
            print(f"{self.title} is not checked out.")

    def display_info(self):
        print(f"--------------Title: {self.title}")
        print(f"*Author: {self.author}")
        print(f"*Checked Out: {'Yes' if self.checked_out else 'No'}")
        if self.checked_out:
            print(f"*Due Date: {self.due_date.strftime('%Y-%m-%d')}")


class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, director)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")


class Magazine(LibraryItem):
    def __init__(self, title, number):
        super().__init__(title, "-")
        self.number = number

    def display_info(self):
        super().display_info()
        print(f"Magazine Number: {self.number}")


def ex6():
    book = Book(title="Mara", author="Ioan Slavici", genre="realist")
    book.display_info()
    book.check_out()
    book.return_item()
    book.display_info()
    print()

    dvd = DVD(title="DVD1", director="director1", duration=120)
    dvd.display_info()
    dvd.check_out()
    dvd.return_item()
    dvd.display_info()
    print()

    magazine = Magazine(title="Vogue", number=5)
    magazine.display_info()
    magazine.check_out()
    magazine.return_item()
    magazine.display_info()
    print()


#ex6()
