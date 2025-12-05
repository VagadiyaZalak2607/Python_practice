#creating class

class Student:
    name = "zalak","dipen","abc","xyz"
 v
#creating object
s1= Student()
print(s1)

#constructor
student1 = Student()
print(student1.name)

#init function
class Student1:
    name = "xyz"
    def __init__(self):
        print("adding a new student in list")

s1 = Student1()

#adding value in function
class Student2:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding a new student in list")
s2 = Student2("zalak",90)
print(s2.name)
print(s2.marks)

#create a student class that takes name and marks find avg
class Student3:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for avg in self.marks:
            sum+=avg
        print("Hii",self.name,"your avg score is:",sum/3)
s3 = Student3("zalu",[90,92,93])
s3.avg()

#static method
class Hello:
    @staticmethod
    def msg():
        print("hello")
Hello.msg()

#abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def Start(self):
        self.acc = True
        self.brk = True
        print("Car Started....")

c1 = Car()
c1.Start() 

#create bank account details
class Bank():
    def __init__(self,acc,bal):
         self.account = acc
         self.balance = bal
    #debit method
    def Debit(self,amount):
         self.balance -= amount
         print(f"your{self.account} is debites by Rs{amount}")
         print("total balance = ",self.balance)

    #debit method
    def Credit(self,amount):
        self.balance += amount
        print(f"your {self.account} is debites by Rs{amount}")
        print("total balance = ",self.balance)
        
    #get balance
    def Balance(self):
         return self.balance
         

bank1 = Bank(22260711,100000)
print("your account number:",bank1.account)
print("your bank balance:",bank1.balance)
bank1.Credit(5000)
bank1.Debit(2000)

        