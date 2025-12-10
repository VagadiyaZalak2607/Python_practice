def moving():
    class Vehicle:
        def move(self):
            print("Vehicle moves")

    class Car(Vehicle):         
        def move(self):         
            print("Car drives on road")

    class Boat(Vehicle):
        def move(self):
            print("Boat sails")
