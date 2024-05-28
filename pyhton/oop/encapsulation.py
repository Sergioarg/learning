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

    def alter_protected(self):
        """ doc """
        self._variable_protegida += 1
        print(f"Var Prot: {self._variable_protegida}")

    def metodo_publico(self):
        """ doc """
        self.__variable_privada += 1
        print(f"Var Priv: {self.__variable_privada}")

    def __metodo_privado(self):
        """ doc """
        print("Este es un método privado!")

class Children(MyClass):
    """ doc """
    pass

children = Children()
print(dir(children))
print(children._MyClass__metodo_privado())




obj = MyClass()
obj._variable_protegida = 12
print(obj._variable_protegida)
obj.alter_protected()

print(f"Var Protegida: {obj._variable_protegida}")
# print(f"VAr Privada: {obj.__variable_privada}")


class ProtegidoEjemplo:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}")

persona = ProtegidoEjemplo("Bob", 25)
persona.mostrar_info()  # Salida: Nombre: Bob, Edad: 25
persona._nombre = "Andres"
print(persona._nombre)  # Acceso posible, pero desaconsejado: Bob
