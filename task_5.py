# Завдання 5: Перевизначення методів

class Shape:

    def __init__(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height

    def display_color(self):
        print(f"Color: {self.color}, Width: {self.width}, Height: {self.height}")


rectangle = Rectangle("Blue", 10, 5)
rectangle.display_color()  # Виведе "Color: Blue, Width: 10, Height: 5"
