""" Variable scope """

# Rule: L.E.G.B
print("Built-in Scope") # Built-in Scopre

var_global = "Global Scope"

def fun():
    var_local = "Local Var"
    def other_func():
        inner_scope = "Enclosing Scope"

    other_func()
