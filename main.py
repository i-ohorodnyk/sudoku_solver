import numpy as np
import random as rnd

def remove_duplicates_from_ndarray(a):
    """ 
        This function removes digitals that have 1 or more occurrences in a.
        This fucntion takes only one argument that should be numpu.ndarray type.
        This function returns None.
    """
    # Type validation section
    assert type(a) == np.ndarray

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                a[i] = 0

def remove_duplicates_from_groups(field):
    """
        This function removes digitals of field by specific index group.
        This function takes the numpy.ndarray object with two dimenstion shape.
        This function returns None. 
    """
    a = np.zeros(9, dtype=np.int64)
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            c = 0
            for row in field[i:i+3]:
                a[c:c+3] = row[j:j+3]
                c += 3
            remove_duplicates_from_ndarray(a)
            c = 0
            for row in field[i:i+3]:
                row[j:j+3] = a[c:c+3]
                c += 3

get_field = lambda : np.array([np.array([rnd.randint(1, 9) for j in range(9)]) for i in range(9)])

