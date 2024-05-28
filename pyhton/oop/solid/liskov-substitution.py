from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

def calculate_area(shape: Shape):
    print(f"Shape: {shape} - Area: {shape.calculate_area()}")

rectangle = Rectangle(1, 2)
square = Square(1)

calculate_area(rectangle)
calculate_area(square)



class Animal(ABC):

    def comer(self):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")
