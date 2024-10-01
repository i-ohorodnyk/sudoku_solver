import numpy as np
import sys
import random as rnd

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from sudoku_solver.remove_duplicates import remove_duplicates_from_field
from sudoku_solver.fill_delta import fill_delta_by_field

get_field = lambda : np.array([np.array([rnd.randint(1, 9) for j in range(9)]) for i in range(9)])

env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template("print_field.jinja")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/', response_class=HTMLResponse)
async def root():
    return template.render(field=get_field())

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
