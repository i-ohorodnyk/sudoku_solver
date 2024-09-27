import numpy as np
import random as rnd

from remove_duplicates import remove_duplicates_from_field

def fill_delta_by_field(field):
    """
        This function fill delta for field by replacing by 0 digital.
        This function takes only one argument that should be numpy.ndarray type.
        This function returns None.
    """
    # Type validation sectios
    assert type(field) == np.ndarray
    assert field.shape == (9, 9)

    pass


def fill_delta_by_group(field):
    """
        This function fill delta for group by replacing by 0 digital.
        This function takes only one argument that should be numpy.ndarray type.
        This function returns None.
    """
    # Type validation sectios
    assert type(field) == np.ndarray
    assert field.shape == (9, 9)

    pass

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

    d = get_delta(a)
    c = 0
    for i in range(9):
        if a[i] == 0:
            a[i] = d[c]
            c += 1

def get_delta(a):
    """
        This function computes missing digitals from range 1 to 9 numpy.int64
        and returns delta as object numpy.ndarray of shape of (9, ).
        This function takes the numpy.ndarray object with (9,) shape of 
        numpy.int64 digitals that have no duplicates.
        This function returns delta - numpy.ndarray that represent digitals
        that need to replace from 0 to get filled numpy.ndarray object without duplicates.
    """
    # Type validation section
    assert type(a) == np.ndarray
    assert a.shape == (9, )

    d = np.array([np.int64(i) for i in set(range(1, 10)) - set(a)], dtype=np.int64)
    rnd.shuffle(d)

    return d


get_field = lambda : np.array([np.array([rnd.randint(1, 9) for j in range(9)]) for i in range(9)])


def main():
    INPUT_MESSAGE = """
    Please choose type the command that need to execute.
    The table of available commands listed below:
        print_field -- This command will show current state of field
        set_random_field -- This command fill field by random digitals from 1 to 9
        remove_duplicates_from_field -- This command remove duplicates from field
        exit -- Exit from the programm
    
    !>  """
    ### NOTE! Please make sure that field should exists in context!
    context = {
        "field": get_field()
    }

    functions = {
        "print_field": lambda context: print(context.get('field', "field in context is not found")),
        "set_random_field": lambda context: context.update({"field": get_field()}),
        "remove_duplicates_from_field": lambda context: remove_duplicates_from_field(context["field"]),
        "exit": lambda context: exit()
    }


    while True:
        context.update({
            "command": input(INPUT_MESSAGE)
        })
        next_func = functions.get(context["command"], lambda context: print("Not existing command -", context["command"]))
        next_func(context)


if __name__ == "__main__":
    main()
