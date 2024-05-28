"""
Herencia:
    - Es la forma de crear clases que heredan de otras.
    - Una clase puede heredar de otra, pero una clase no puede heredar de varias.
"""
class Parent:
    """ doc """
    # Members of the parent class
    pass

class Child(Parent):
    """ doc """
    # Inherited members from parent class
    # Additional members of the child class
    pass


class A:
    def b(self):
        return "Function inside A!"

class B:
    pass

class C(B, A):
    pass

class D(C):
    pass

print(C().b())
d = D()
print(d.b())
