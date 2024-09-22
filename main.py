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
    assert a.shape == (9, )

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
    assert type(field) == np.ndarray
    assert field.shape == (9, 9)

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

def fill_delta_by_rows(field):
    """
        This function replace digitals of type numpy.int64 that have value 0
        to digit that have occurance in row of field. This method can generate
        duplicates by columns order.
        This function takes the numpy.ndarray object with two dimenstion shape.
        This function returns None.
    """
    assert type(field) == np.ndarray
    assert field.shape == (9, 9)

    for i in range(field.shape[0]):
        d = get_delta(field[i])
        c = 0
        for j in range(field.shape[1]):
            if field[i][j] == np.int64(0):
                field[i][j] = d[c]
                c += 1

get_field = lambda : np.array([np.array([rnd.randint(1, 9) for j in range(9)]) for i in range(9)])
get_delta = lambda a: np.array([np.int64(i) for i in set(range(1, 10)) - set(a)], dtype=np.int64)

