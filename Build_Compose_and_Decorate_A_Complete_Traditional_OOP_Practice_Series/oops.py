# 1. Using `self`
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


# 2. Using `cls`
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting.")


# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Global Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public
        self._salary = salary  # Protected
        self.__ssn = ssn  # Private


# 8. The `super()` Function
class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32


# 13. Composition
class Engine:
    def start(self):
        print("Engine started.")


class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car is running.")


# 14. Aggregation
class Department:
    def __init__(self, name):
        self.name = name


class EmployeeWithDepartment:
    def __init__(self, name, department):
        self.name = name
        self.department = department


# 15. Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()

    return wrapper


@log_function_call
def say_hello():
    print("Hello!")


# 17. Class Decorators
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls


@add_greeting
class Person:
    pass


# 18. Property Decorators: `@property`, `@setter`, and `@deleter`
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        print("Price deleted")
        del self._price


# 19. `callable()` and `__call__()`
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor


# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current


# Testing the implementations

# 1. Using `self`
student1 = Student("John", 85)
student1.display()

# 2. Using `cls`
counter1 = Counter()
counter2 = Counter()
Counter.display_count()

# 3. Public Variables and Methods
car1 = Car("Toyota")
print(car1.brand)
car1.start()

# 4. Class Variables and Class Methods
Bank.change_bank_name("Tech Bank")
print(Bank.bank_name)

# 5. Static Variables and Static Methods
result = MathUtils.add(5, 3)
print(result)

# 6. Constructors and Destructors
logger = Logger()
del logger

# 7. Access Modifiers: Public, Private, and Protected
employee = Employee("John", 50000, "123-45-6789")
print(employee.name)
print(employee._salary)

# 8. The `super()` Function
teacher = Teacher("Mr. Smith", "Math")
print(teacher.name, teacher.subject)

# 9. Abstract Classes and Methods
rect = Rectangle(5, 10)
print(rect.area())

# 10. Instance Methods
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

# 11. Class Methods
Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# 12. Static Methods
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(30)
print(fahrenheit)

# 13. Composition
engine = Engine()
car_with_engine = CarWithEngine(engine)
car_with_engine.start()

# 14. Aggregation
dept = Department("HR")
emp_with_dept = EmployeeWithDepartment("John", dept)
print(f"Employee: {emp_with_dept.name}, Department: {emp_with_dept.department.name}")

# 15. Method Resolution Order (MRO) and Diamond Inheritance
d = D()
d.show()

# 16. Function Decorators
say_hello()

# 17. Class Decorators
person = Person()
print(person.greet())

# 18. Property Decorators: `@property`, `@setter`, and `@deleter`
product = Product(100)
print(product.price)
product.price = 150
print(product.price)
del product.price

# 19. `callable()` and `__call__()`
multiply_by_2 = Multiplier(2)
print(callable(multiply_by_2))
print(multiply_by_2(5))

# 20. Creating a Custom Exception
try:
    check_age(15)
except InvalidAgeError as e:
    print(e)

# 21. Make a Custom Class Iterable
countdown = Countdown(5)
for number in countdown:
    print(number)
