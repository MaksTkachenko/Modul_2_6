# Завдання 4: Просте наслідування


class Shape:

    def __init__(self, color):
        self.color = color

    def display_color(self):
        print(f"Color is {self.color}")


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height


shape = Shape("Red")

shape.display_color()  # Виведе "Color: Red"
rectangle = Rectangle("Blue", 10, 5)

rectangle.display_color()  # Виведе "Color: Blue"

print(rectangle.width)  # Виведе 10
print(rectangle.height)  # Виведе 5
