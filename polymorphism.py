# Polymorphism Challenge (Animals and Vehicles)
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def speak(self):
        print(f"{self.name} makes a sound.")


class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🦅")

    def speak(self):
        print(f'{self.name} says "Chirp chirp!" 🎵')


class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐠")

    def speak(self):
        print(f'{self.name} says "Blub blub!" 💧')


class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")

    def speak(self):
        print(f'{self.name} says "Hiss hiss!" 🎶')


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def start_engine(self):
        print(f"Starting the {self.vehicle_type}'s engine.")


class Car(Vehicle):
    def __init__(self):
        super().__init__("car")

    def move(self):
        print("Driving on the road! 🚗")


class Airplane(Vehicle):
    def __init__(self):
        super().__init__("airplane")

    def move(self):
        print("Flying through the sky! ✈️")


class Boat(Vehicle):
    def __init__(self):
        super().__init__("boat")

    def move(self):
        print("Sailing on the water! ⛵")


if __name__ == "__main__":
    # Demo of polymorphism with animals
    animals = [
        Bird("Eagle"),
        Fish("Nemo"),
        Snake("Viper")
    ]

    print("--- Animal Movements ---")
    for animal in animals:
        animal.move()
        animal.speak()

    # Demo of polymorphism with vehicles
    vehicles = [
        Car(),
        Airplane(),
        Boat()
    ]

    print("\n--- Vehicle Movements ---")
    for vehicle in vehicles:
        vehicle.start_engine()
        vehicle.move()