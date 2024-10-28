from time import time
from _papers import paper
import _input as input
import json

with open('map_meta.json') as meta_file:
    meta = json.load(meta_file)

open_plots = [
    [5, 5]
]

meta['empty_plots'] = open_plots

paper = paper(metadata=meta)

counter = {
    'start': time(),
    'end': None
}

input.UI.paper(paper)

while paper.status == 1:
    row = input.number('Give row number: ').value - 1
    plot = input.number('Give plot number: ').value - 1

    paper.openPlot(row, plot)

    input.UI.paper(paper)

if paper.status == 0:
    input.UI.print('You lost.')
elif paper.status == 2:
    input.UI.print('You won')