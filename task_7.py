# Завдання 7: Використання super()

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square(Rectangle):

    def __init__(self, color, side_length):
        super().__init__(side_length, side_length)
        self.color = color
        self.side_length = side_length

    def display_color(self):
        print(f"Color: {self.color}")


square = Square("Green", 8)

square.display_color()  # Виведе "Color: Green"

print(square.width)  # Виведе 8
print(square.height)  # Виведе 8
print(square.side_length)  # Виведе 8
