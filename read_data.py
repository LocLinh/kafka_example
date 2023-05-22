import numpy as np

def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        data = f.readlines()

    print(len(data))
    return data
