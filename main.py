import numpy as np
import sys
import random as rnd

from flask import Flask

from jinja2 import Environment, FileSystemLoader

from sudoku_solver.remove_duplicates import remove_duplicates_from_field
from sudoku_solver.fill_delta import fill_delta_by_field

get_field = lambda : np.array([np.array([np.uint8(rnd.randint(1, 9)) for _ in range(9)]) for _ in range(9)])

env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template("print_field.jinja")

app = Flask(__name__)

@app.route("/")
def main():
    field = get_field()
    return f"<h1>{field}</h1>"
