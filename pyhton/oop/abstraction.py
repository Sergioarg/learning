"""
Abstraccion:
    - Clase abstracta que representa un objeto.
    - Tiene como propiedad el nombre de la clase y los atributos.
    - Todos los metodos son abstractos.
    - Todo objeto debe heredar de esta clase.
    - Esta clase no se puede instanciar.
"""
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    """ Doc """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Figura):
    """ Doc """
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio**2

rectangulo = Rectangulo(5, 3)
circulo = Circulo(2)
print(rectangulo.calcular_area())  # Salida: 15
print(circulo.calcular_area())  # Salida: 12.56636
