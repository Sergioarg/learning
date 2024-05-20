"""
Pilar Encapsulamiento:

Es un principio de diseño que nos permite ocultar la implementación detrás de una interfaz.
Esto nos permite cambiar el comportamiento interno sin afectar a las clases que usan nuestra clase.

Publica: visibles para todos

Protegida:
    Los miembros protegidos de una clase son accesibles desde la propia clase y
    también desde sus subclases.

Privada:
    Los miembros privados de una clase son solo accesibles desde la propia clase.
"""

class MyClass:
    """ Doc """
    def __init__(self):
        self.variable_publica = 10
        self._variable_protegida = 20
        self.__variable_privada = 30

    def get_variable_privada(self):
        """Getter """
        return self.__variable_privada

    def metodo_publico(self):
        """ doc """
        print("Este es un método público")

    def __metodo_privado(self):
        """ doc """
        print("Este es un método privado")


obj = MyClass()
print(obj._variable_protegida)
print(obj.get_variable_privada())
