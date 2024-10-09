#!venv/bin/python
from sudoku_solver.remove_duplicates import remove_duplicates_from_field
from sudoku_solver.fill_delta import fill_delta_by_field


def main():
    INPUT_MESSAGE = """
    Please choose type the command that need to execute.
    The table of available commands listed below:
        print_field -- This command will show current state of field
        set_random_field -- This command fill field by random digitals from 1 to 9
        remove_duplicates_from_field -- This command remove duplicates from field
        fill_delta_by_field -- This command add delta onto field
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
        "fill_delta_by_field": lambda context: fill_delta_by_field(context["field"]),
        "exit": lambda context: sys.exit()
    }


    while True:
        context.update({
            "command": input(INPUT_MESSAGE).strip()
        })
        next_func = functions.get(context["command"], lambda context: print("Not existing command -", context["command"]))
        next_func(context)


if __name__ == "__main__":
    main()


