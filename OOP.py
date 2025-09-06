# learning oop in pyhton 

# example 1

class myclass:
    def student(self):
        print("tabee carter is here and hes student in kmclu doing batchlers degree in computer application")
#a = myclass()
#a.student()

# example 2

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Tommy", 3)
dog2 = Dog("Bruno", 5)

#dog1.bark()
#dog2.bark()
#print(dog1.age)

# example 3

class calculator:
    
    def add(self, a, b):
        return a + b
    def subtract(self, a ,b):
        return a - b
calc = calculator()

#print(calc.add(5, 3))
#print(calc.subtract(5, 3))

# example 4

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdrew(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrew {amount}. New balance: {self.balance}")

        else:
            print("Insufficent Funds")

#acc = BankAccount("Ali", 1000)
#acc.deposit(500)
#acc.withdrew(300)
#acc.withdrew(1500)

#practice 1

class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("car started")
                
car1 = car("mahindra", "xuv",2021)
#car1.start()
#print(car1.brand)

#practice 2

class rectangle:
    def area(self, length, width):
        return length * width
    
    def perimeter(self, length, width):
        return 2 * (length + width)
    
rec1 = rectangle()
#print(rec1.area(12,10))
#print(rec1.perimeter(12,10))

#practice 3

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = student("tab", 57)
s2 = student("joffery", 39)

#s1.grade()
#s2.grade()
#print(s1.name)


#practice 4

class counter:
    def __init__(self, initial):
        self.initial = initial
    def increment(self):
        print(self.initial + 1)
    def decrement(self):
        print(self.initial - 1)
    def display(self):
        print(self.initial)

start = counter(0)
#start.increment()
#start.decrement()
#start.display()

# practice 5

class Dog:
    def __init__(self, name, age):
        self.name = name   
        self.age = age     
    
    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Tommy", 3)
dog2 = Dog("Bruno", 5)
dog3 = Dog("Sabby", 14)

#dog1.bark()   
#dog2.bark()   
#dog3.bark()

#chatgpt is saying by doing all these thing you have learn 40% oop i will comeback for my 60%
