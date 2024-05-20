"""
- map() take a function and a list as arguments.
    It applies the function to each element of the list, returning a new list with the results.

- filter(): do the same as map(), but it returns only the elements that make the function return True.
"""
menu = ["americano", "cortado", "cappuccino", "latte", "mocha", "espresso"]

def find_coffe(coffe):

    if coffe[0] == 'c':
        return coffe

map_coffe = map(find_coffe, menu)

filter_coffe = filter(find_coffe, menu)

print("Map: ", list(map_coffe))

print("Filter: ", list(filter_coffe))
