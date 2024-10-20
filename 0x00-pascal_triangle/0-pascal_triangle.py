#!/usr/bin/python3
""" Pascal triangle
"""


def pascal_triangle(n):
    """ Returns pascal triangle
    """
    if n <= 0:
        return []

    pasTran = []

    for i in range(n):
        # The first element
        my_List = [1]
        if i == 0:
            pasTran.append(my_List)
            continue

        k = i - 1
        for j in range(len(pasTran[k])):
            if j + 1 == len(pasTran[k]):
                # The last element
                my_List.append(1)
                break
            # Add two values to get the current next value
            nextVal = pasTran[k][j] + pasTran[k][j + 1]
            my_List.append(nextVal)
        pasTran.append(my_List)

    return pasTran
