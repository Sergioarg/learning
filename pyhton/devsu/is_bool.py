""" Question 7 """
def is_bool(i, j):
    """ Is Bool? """
    if i == 1 or j == 1 or i + j == 1:
        return True

    return False

if "__main__" == __name__:
    print(is_bool(1, 5))
    print(is_bool(2, 3))
    print(is_bool(-3, 4))
