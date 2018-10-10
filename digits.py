import numpy as np


def read(path):
    labels = []
    pixels = []
    with open(path, 'r') as file:
        lines = iter(file)
        next(lines)
        for line in lines:
            tokens = line.split(',')
            labels.append(int(tokens[0]))
            pixels.append([int(t) for t in tokens[1:]]) 
    labels = np.asarray(labels)
    pixels = np.asarray(pixels)
    return labels, pixels