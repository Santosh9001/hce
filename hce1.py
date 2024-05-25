def greet(name):
    print("hello "+name+"!")
greet("Himalayan College")

# len() function returns the length(number of items) of an object
length = len("Hello World!")
print(length)

# range() function generates a sequence of numbers within a specified range.
# commonly used in loops
for num in range(5):
    print(num)

# built in function where it denotes:  (start, end, step)
for num in range(1, 10, 2):
    print(num)


# list in python
my_list = [1, 2, 3, 'a', 'b', 'c']
print(my_list[0])
print(my_list[-1])

my_list.append(6)
my_list.remove('a')


class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print("Car: "+ self.make+ " "+self.model)
        

car1 = Car("Toyota","Corolla")
car2 = Car("Hyunday","i10")

print(car1.make)
car1.display_info()

# __init__ are called magic methods or dunder methos. They are predefined with special meaning
# they emulate built in types or operator overloading

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2024 - birth_year
        return cls(name, age)

person1 = Person.from_birth_year("Alice", 1990)
print(person1.age)  # Output: 34


class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y

print(MathOperations.add(2, 3))       # Output: 5
print(MathOperations.multiply(2, 3))  # Output: 6


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # Output: 4 6



# check pip version
# python3 -m ensurepip
# pip install virtualenv

# pip install --upgrade pip
# python -m virtualenv venv
# virtualenv venv
# python -m source venv/bin/activate
# python -m pip/pip3 install django
# pip/pip3 install library_packages {dont do this, it is ex}
# django --version

# django-admin startproject mysite
# python manage.py runserver
# ctrl + c (exit the server)

# python manage.py startapp polls
# python manage.py migrate

# python mange.py createsuperuser
# type : {deactivate} to exit the venv 

# python manage.py startapp products
# python manage.py startapp categories
# python manage.py startapp customers

# python manage.py makemigrations
# python manage.py migrate

# create folder 'templates' inside categories folder
    # create folder 'categories' inside 'templates' folder
        # create file 'category_list.html' and 'category_products.html' inside 'categories'

# get & post
# get -> url query params 
# post -> body params 

# python -m pip/pip3 install djangorestframework
# go into a specific app -> create serializers.py file 
