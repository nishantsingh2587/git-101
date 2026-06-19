"""
classes an object --> Blueprint(class)->instances(object)
"""
"""class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

rex=Dog("Rex","Labrador")
kallu=Dog("Kallu","Desi")

kallu.name="Dogesh"
print(rex.name,rex.breed)
print(kallu.name,kallu.breed)"""

"""create a class student name roll no email"""
"""class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
s=Student("nishant",202310101150022)
print(s.name,s.rollno)"""

"""
instances methods and attributes
"""
class BankAccount:
    bank_name="SBI"
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance

tom=BankAccount("Tom",1000)
ketan=BankAccount("ketan")

tom.deposit(5000)
print(tom.balance)