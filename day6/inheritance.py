#single inheritance (only one child class can inherit properties from parent class)
class Parent:
    def show(self):
        print("Parent class")
class Child(Parent):
    pass
c = Child()
c.show()

#multilevel inheritance (Grandparent → Parent → Child)
class Grandfather:
    def house(self):        
        print("Grandfather's house")
class Father(Grandfather):
    def car(self):
        print("Father's car")
class Child(Father):
    def bike(self):
        print("Child's bike")
c2 = Child()
c2.house()
c2.car()
c2.bike()

#multiple inheritance (child class can inherit properties from multiple parent class)
class Father:
    def skills(self):
        print("Father's skills")
class Mother:
    def cooking(self):
        print("Mother's cooking")
class Child(Father, Mother):
    pass
c = Child()
c.skills()
c.cooking()

#hierarchical inheritance (multiple child can inherit properties from same parent class)
class Vehicle:
    def fuel(self):
        print("Uses fuel")
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass
car = Car()
bike = Bike()
car.fuel()
bike.fuel()

#example1 (multiple inheritance)
class Vehicle:
        def move(self):
            print("Vehicle moves")
class Car(Vehicle):
        def move(self):
            print("Car drives on road")
class Boat(Vehicle):
        def move(self):
            print("Boat sails")
c4 = Car()
b1 = Boat()
c4.move()
b1.move()

#example2 (single inheritance)
class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.speak()
d.bark()

#example3 (multilevel inheritance)
class Grandfather:
    def house(self):
        print("Grandfather owns a house")

class Father(Grandfather):
    def car(self):
        print("Father owns a car")
class Child(Father):
    def bike(self):
        print("Child owns a bike")
c5 = Child()
c5.house()
c5.car()
c5.bike()

