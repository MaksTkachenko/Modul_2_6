# Завдання 1: Проста інкапсуляція


class Person:

    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


person = Person()

person.set_name("John")
person.set_age(25)

print(person.get_name())
print(person.get_age())
