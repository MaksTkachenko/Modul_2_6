# Завдання 2: Інкапсуляція зі зміною значень через методи

class Person:

    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        for char in name:
            if char.isdigit():
                print("Error: name cannot contain numbers")
                break
        else:
            self.__name = name

    def set_age(self, age):
        if not(0 <= age <= 120):
            print("Error: age can be between 0 and 120")
        else:
            self.__age = age


person = Person()

person.set_name("John")
person.set_age(15)

print(person.get_name())  # Виведе "John"
print(person.get_age())   # Виведе 25

person.set_name("John123")  # Виведе повідомлення про помилку
person.set_age(150)  # Виведе повідомлення про помилку
