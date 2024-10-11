import numpy as np
import sys
import random as rnd

from PIL import Image, ImageDraw, ImageFont

from flask import Flask, send_file

from jinja2 import Environment, FileSystemLoader

from sudoku_solver.remove_duplicates import remove_duplicates_from_field
from sudoku_solver.fill_delta import fill_delta_by_field


get_field = lambda : np.array([np.array([np.uint8(rnd.randint(1, 9)) for _ in range(9)]) for _ in range(9)])

env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template("print_field.jinja")

app = Flask(__name__)


@app.route("/")
def main():
    field = "<br/>".join([str(row) for row in get_field()])
    return f"<h1>{field}</h1>"

@app.route("/get_image")
def get_image():
    out = Image.new("RGB", (500, 500), (255, 255, 255))
    fnt = ImageFont.truetype("static/fonts/SixtyfourConvergence.ttf", 50)
    d = ImageDraw.Draw(out)
    field = get_field()
    d.multiline_text((10, 10), '\n'.join([''.join([str(i) for i in row]) for row in field]), font=fnt, fill=(0, 0, 0))
    out.save("img.png")

    return send_file("img.png", mimetype='image/png')
