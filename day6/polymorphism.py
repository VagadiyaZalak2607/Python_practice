#operator overloading (when same operator have different meaning)
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num):
        newreal = self.real + num.real
        newimg = self.img + num.img
        return Complex(newreal, newimg)

num1 = Complex(1,3)
num1.shownumber()

num2 = Complex(3,1)
num2.shownumber()

num3 = num1 + num2
num3.shownumber()

#example
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
ar = Circle(14)

print("area of circle:",ar.area())

print("area of perimeter:",ar.perimeter())


#example2
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showdetails(self):
        print("role:", self.role)
        print("dept:", self.dept)
        print("salary:", self.salary)
 
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "60,000")

    def showdetails(self):
        print("name:", self.name)
        print("age:", self.age)
        super().showdetails()

eng = Engineer("zalak", 19)
eng.showdetails()
