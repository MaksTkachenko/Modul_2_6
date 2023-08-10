# Завдання 8: Автосалон

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model


class Sedan(Car):

    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        print(f"Car: {self.make} {self.model}\nDoors: {self.doors}")


class Suv(Car):

    def __init__(self, make, model, passenger_seats):
        super().__init__(make, model)
        self.passenger_seats = passenger_seats

    def display_info(self):
        print(f"Car: {self.make} {self.model}\nSeats: {self.passenger_seats}")


class SportsCar(Car):

    def __init__(self, make, model, max_speed):
        super().__init__(make, model)
        self.max_speed = max_speed

    def display_info(self):
        print(f"Car: {self.make} {self.model}\nMax Speed: {self.max_speed} km/h")


# Створюємо об'єкти різних класів
sedan = Sedan("Toyota", "Camry", 4)
suv = Suv("Ford", "Explorer", 7)
sports_car = SportsCar("Ferrari", "488 GTB", 330)

# Виводимо інформацію про кожен автомобіль
sedan.display_info()
print("-------------------------")
suv.display_info()
print("-------------------------")
sports_car.display_info()
