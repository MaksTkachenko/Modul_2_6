# Завдання 6: Багатоуровневе наслідування

class Animal:
    def __init__(self, animal, species):
        self.animal = animal
        self.species = species

    """def animal(self):
        return self.animal
    
    def species(self):
        return self.species"""

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecies: {self.species}")
        

class Mammal(Animal):

    def __init__(self, animal, species, diet_type):
        super().__init__(animal, species)
        self.diet_type = diet_type

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecies: {self.species}\nDiet Type: {self.diet_type}")


class Carnivore(Mammal):

    def __init__(self, animal, species, diet_type, teeth_count):
        super().__init__(animal, species, diet_type)
        self.teeth_count = teeth_count

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecies: {self.species}\nDiet Type: {self.diet_type}\n"
              f"Teeth Count: {self.teeth_count}")


class Lion(Carnivore):

    def __init__(self, animal, species, diet_type, teeth_count, mane_size):
        super().__init__(animal, species, diet_type, teeth_count)
        self.mane_size = mane_size

    def display_info(self):
        print(f"Animal: {self.animal}\nSpecies: {self.species}\nDiet Type: {self.diet_type}\n"
              f"Teeth Count: {self.teeth_count}\nMane Size: {self.mane_size}")


# Створюємо об'єкти різних класів
lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")
# Виводимо інформацію про кожну тварину
lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()
        