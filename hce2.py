# this is a function
def dontshow(value):
    print(value)

dontshow("Hello friends")

#len() function returns the length(number of items) of an object
length = len("Hello World!")
print(length)

# range() function generates a sequence of numbers within a specified range.
# commonly used in loops
# for (int i = 0; i<10; i++)
# for(number in range starting from 0 to 4)
for num in range(5):
    print(num)

for value in range(1,20,3):
    print(value)

# lists in python
my_list = [1,2,4,6,'a','b','c','d']
length = len(my_list)

print(my_list[3])
print(my_list[1])
print(my_list[-2]) # is this possible ? 

# __init__(), __abc__() (magic methods, dunder methods)
# this.name = name
class Car:
    def __init__(self,make,model): # constructor, self
        self.make = make
        self.model = model
    # this is a method
    def show_info(self):
        print("Car : "+ self.make +" "+self.model)

    def __add__(self):
        print("This is add merhod")
    # does not require object to access it
    @classmethod
    def divide(cls):
        print("Class method")

    #requires object to access this method
    @staticmethod
    def multiply():
        print("Multiply method") 

car1 = Car("Toyota","Corolla")
car2 = Car("Hyundai","Zen")
Car.divide()

print(car1.make)
car2.show_info()

# @classmethod, @staticmethod {difference identify}, {cls}
# static,  non static