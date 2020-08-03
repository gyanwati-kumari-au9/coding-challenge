# Q1. Write down about the oops principles ?
# principles of oops:-
# There are basically four principles of oops:-
# 1.Encapsulation
# 2.Inheritance
# 3.polymorphism
# 4.Abstraction
# 1.Encapsulation:-
# The concept of Encapsulation is to keep together the implementation (code) and the data it manipulates (variables). 
# Having proper encapsulation ensures that the code and data both are safe from misuse by outside entity.
# for example:
class Person:
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def display(self):
    print(self.name)
    print(self.age)
if __name__=="__main__":
    person = Person('Gyan', 20)
    #accessing using class method
    person.display()
    #accessing directly from outside
    print(person.name)
    print(person.age)


# 2.Inheritance:-
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
#for example:-
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

    # Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
#   pass
# Add the __init__() function to the Student class:
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
# Use the super() Function
        super().__init__(fname, lname)
# Add Properties
        self.graduationyear = 2020
# Add a method called welcome to the Student class:
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
   
#Use the Person class to create an object, and then execute the printname method:
# x = Person("Gyan", "Abi")
# x.printname()
x=Student("Gyan","Abi")
x.printname()
print(x.graduationyear)
x.welcome()

# 3.polymorphism:-
# The word polymorphism means having many forms. In programming, 
# polymorphism means same function name (but different signatures) 
# being uses for different types.
# there are two types:-method overriding and method overloading
# Example:-plymorphism class method
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

# Example of method overriding:-
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

# Example of method overloading:-
class Compute:
  def area(self, x = None, y = None):
    if x != None and y != None:
      return x * y
    elif x != None:
      return x * x
    else:
      return 0
# object
obj = Compute()
# zero argument
print("Area Value:", obj.area())
# one argument
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))

# 4.Abstraction:-hidding the implementation.

class Animal:
  def __init__(self,legs,has_tail):
    self.legs=legs
    self.has_tail=has_tail
    self.teeth=32

  def walk(self):
    raise NotImplementedError()
    
  def eat(self):
    raise NotImplementedError()
    
  def perform_daily_task(self):
    self.walk()
    self.eat()
class Dog(Animal):
  def __init__(self,legs,has_tail):
    self.legs=legs
    self.has_tail=has_tail
  def walk(self):
    print('Dog will be walk')
  def eat(self):
    print('dog will be eat')

if __name__=="__main__":
  dog1=Dog(4,True)
  dog1.perform_daily_task()




# Q2. Implement a real life bank by using oops concepts. 
# Eg create classes as Bank, Depositor,
# Clerk, BankAccount
class Bank:
    def __init__(self):
        self.depositors=[]
        self.clerks=[]
        self.Account=[]
    
    def addCustomer(self, customer):
        if self.depositors!=customer:
            print('Added customer')
        else:
            print('Invalid')
    
    def openAccount(self,custDetails, AccountNo):
        pass

    def deposit(self, clerk, AccountNo, amount):
        self.balance += amount 

    def withdraw(self,clerk, AccountNo, amount):
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 

    def addClerk(self, clerk):
        # is already clerk exist with id
        if self.clerks!=id:
            print('clerk added !')
        # throw error
        else:
            print('Invalid')

        self.clerks.append(clerk)
        
  
class Depositor:
    def __init__(self): 
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
        
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
class Clerk:
    def __init__(self, name, bank, id):
        self.name=name
        self.id=id
        self.bank=bank
    
    def deposit(self,accountNo,amount):
        self.bank.deposit(self.id, accountNo, amount)
    
        
class BankAccount:
    def __init__(self,custid,AccountNo,Balance):
        self.custid=custid
        self.AccountNo=[]
        self.Balance=0

    def checkBalance(self):
        Print("Balance is",self.Balance)
    def updateBalance(self,Balance):
        self.Balance+=Balance
        print("Balance updateed successfully!")




if __name__=="__main__":
    s=Bank()
    while True:
        print('Welcome to XYZ Bank, select option from below menu')
        print('1. Add New Clerk')
        print('2. Add New Depositor')
        print('3. Open New Account')
        print('4. Deposit')
        print('5. Withdrawal')
        print('6. Clerk Login')
        print('9. Quit!')
        choice=int(input('Your choice..'))
        if choice == 9:
            break

        if choice==1:
            name=input('Enter clerk name')
            id= input('Enter clerk id')
            clerk= Clerk(name,s,id)
            s.addClerk(clerk)
            print('Clerk successfully added!')
            break
        elif choice==2:
            name=input('Enter customer name')
            address= input('Enter customer address')
            customer= customer(name,s,address)
            s.addCustomer(customer)
            print('Customer successfully added!')
            break
        elif choice==3:
            custDetails=input('Enter all required details')
            # AccountNo=int(input())
            print('account opened succesfully!')
            break
        elif choice==4:
            AccountNo=int(input("Enter account number:"))
            Amount=float(input("Enter deposit amount:"))
            s.deposit()
            print('your amount is deposited successfully!')
            break
        elif choice==5:
            AccountNo=int(input("Enter account number:"))
            Amount=float(input("Enter withdraw amount:"))
            print('Transaction successfully!')
            break
        elif choice==6:
            loginid=input()
            loginpw=input()
            print()
            break
        else:
            print('Invalid')

        