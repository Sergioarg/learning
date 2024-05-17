""" Question 8 """

def closest_to_zero(ints):
    # Step 1: Check if ints is None
    if ints is None:
        return 0

    # Step 2: Initialize min_val and min_val_int
    min_val = float('inf')
    min_val_int = 0

    # Step 3: Iterate through each integer in ints
    for num in ints:
        abs_num = abs(num)

        # Update min_val and min_val_int if necessary
        if abs_num < min_val or (abs_num == min_val and num > 0):
            min_val = abs_num
            min_val_int = num

    # Step 4: Return min_val_int
    return min_val_int

if "__main__" == __name__:
    ints_test = [-2, -3, 0, 4]
    print(closest_to_zero(ints_test))
