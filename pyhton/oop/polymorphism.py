"""
Polimorfismo:
    Es el principio que nos permite tener una clase base y varias subclases.
    Cada subclase puede tener su propia implementación de los métodos definidos en la clase base.
"""

class Animal:
    """ Animal """
    def hacer_sonido(self):
        """ Doc """
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau!")

def hacer_sonidos(animales):
    for animal in animales:
        animal.hacer_sonido()

perro = Perro()
gato = Gato()

hacer_sonidos([perro, gato])  # Llamada polimórfica al método hacer_sonido()
