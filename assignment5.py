from abc import ABC, abstractmethod

class Movable(ABC):
    """Abstract base class for all movable objects"""
    
    @abstractmethod
    def move(self):
        pass
    
    def describe(self):
        return f"{self.__class__.__name__} is moving"

# Animal Classes
class Animal(Movable):
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        return f"{self.name} the {self.__class__.__name__}"

class Dog(Animal):
    def move(self):
        return f"{self.describe()} is running 🐕"
    
    def bark(self):
        return "Woof! Woof!"

class Bird(Animal):
    def move(self):
        return f"{self.describe()} is flying 🐦"
    
    def chirp(self):
        return "Chirp! Chirp!"

class Fish(Animal):
    def move(self):
        return f"{self.describe()} is swimming 🐠"

class Snake(Animal):
    def move(self):
        return f"{self.describe()} is slithering 🐍"

# Vehicle Classes
class Vehicle(Movable):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def describe(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def move(self):
        return f"{self.describe()} is driving 🚗"
    
    def honk(self):
        return "Beep! Beep!"

class Plane(Vehicle):
    def move(self):
        return f"{self.describe()} is flying ✈️"
    
    def take_off(self):
        return "Preparing for takeoff!"

class Boat(Vehicle):
    def move(self):
        return f"{self.describe()} is sailing ⛵"

class Bicycle(Vehicle):
    def move(self):
        return f"{self.describe()} is pedaling 🚴"
    
    def ring_bell(self):
        return "Ring! Ring!"

class Motorcycle(Vehicle):
    def move(self):
        return f"{self.describe()} is riding 🏍️"

# Demonstration
def demonstrate_movement():
    print("=== ANIMAL MOVEMENT ===")
    animals = [
        Dog("Buddy"),
        Bird("Tweety"),
        Fish("Nemo"),
        Snake("Slither")
    ]
    
    for animal in animals:
        print(animal.move())
        if isinstance(animal, Dog):
            print(f"  Sound: {animal.bark()}")
        elif isinstance(animal, Bird):
            print(f"  Sound: {animal.chirp()}")
        print()
    
    print("=== VEHICLE MOVEMENT ===")
    vehicles = [
        Car("Toyota", "Camry"),
        Plane("Boeing", "747"),
        Boat("Yamaha", "Speedboat"),
        Bicycle("Trek", "Mountain Bike"),
        Motorcycle("Harley-Davidson", "Sportster")
    ]
    
    for vehicle in vehicles:
        print(vehicle.move())
        if isinstance(vehicle, Car):
            print(f"  Sound: {vehicle.honk()}")
        elif isinstance(vehicle, Bicycle):
            print(f"  Sound: {vehicle.ring_bell()}")
        elif isinstance(vehicle, Plane):
            print(f"  Action: {vehicle.take_off()}")
        print()

# Using polymorphism
def make_them_move(movables):
    print("=== MAKING EVERYTHING MOVE ===")
    for movable in movables:
        print(movable.move())

if __name__ == "__main__":
    demonstrate_movement()
    
    # Polymorphism in action
    all_movables = [
        Dog("Rex"),
        Bird("Polly"),
        Fish("Goldie"),
        Car("Honda", "Civic"),
        Plane("Airbus", "A380"),
        Bicycle("Giant", "Road Bike")
    ]
    
    make_them_move(all_movables)