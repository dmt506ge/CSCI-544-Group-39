from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

def convert(input_path, output_path):
    drawing = svg2rlg(input_path)
    renderPM.drawToFile(drawing, output_path, fmt="PNG")

def text_reader(path):
    with open(path, "r") as f:
        return f.read()

text_data = {}
index = 0
for d in os.listdir("./data/svg"):
    for f in os.listdir("./data/svg/" + d):
        for s in os.listdir("./data/svg/" + d + "/" + f):
            if s.endswith("svg"):
                convert(f"./data/svg/{d}/{f}/{s}",f"./digram/output_{index}.png")
            if s.endswith('txt'):
                text = text_reader(f"./data/svg/{d}/{f}/{s}")
                text_data[index] = text
            index+=1

