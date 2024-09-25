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
    # Type validation section
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

def fill_delta_by_ndarray(a):
    """
        This function replace digitals of type numpy.int64 that have value 0
        to digit that have occurance in ndarray of field. This method can generate
        duplicates by columns order.
        This function takes the numpy.ndarray object with two dimenstion shape.
        This function returns None.
    """
    # Type validation section
    assert type(a) == np.ndarray
    assert a.shape == (9, )

    for i in range(9):
        d = get_delta(a)
        c = 0
        for i in range(9)
            if a[i] == 0:
                [i] = d[c]
                [c] += 1

def get_delta(a):
    """
        This function complutes missing from range 1 to 9 numpy.int64 digitals
        and returns this as numpy.ndarray of shape of (9, ).
        This function takes the numpy.ndarray object with (9,) shape of 
        numpy.int64 digitals that have no duplicates.
        This function returns delta - numpy.ndarray that represent digitals
        that need to replace from 0 to get filled numpy.ndarray object without duplicates.
    """
    # Type validation section
    assert type(a) == np.ndarray
    assert a.shape == (9, )

    d = np.array([for i in set(range(1, 10)) - set(a)), dtype=np.int64)
    rnd.shuffle(d)

    return d

get_field = lambda : np.array([np.array([rnd.randint(1, 9) for j in range(9)]) for i in range(9)])
