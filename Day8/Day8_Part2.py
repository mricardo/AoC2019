import sys
import numpy as np

def deep_layer(layers, first_i):
    for l in range(len(layers)):
        curr_layer = layers[l][0]
        if curr_layer[first_i] != '2':
            return curr_layer[first_i]
    return '2'

def process_layers(first_layer, layers):   
    for i in range(len(first_layer)):
        if first_layer[i] == '0':
            continue
        elif first_layer[i] == '2':
            first_layer= first_layer[:i] + deep_layer(layers, i) + first_layer[i+1:]
        elif first_layer[i] == '1':
            continue

    return first_layer

if __name__ == "__main__":
    f = open(sys.argv[1])
    line =  f.read()       
    f.close()

    rows = 6
    cols = 25

    image = np.full((rows, cols), -1)    
    
    i = 0    
    layers = []
    min_zeros = min_layer = min_res = -1
    while i * (rows*cols) < len(line):
        start = i * (rows*cols)
        end = (i + 1) * (rows*cols)
        
        l = line[start:end]

        layers.append([l])
        
        i += 1

    first_layer = process_layers(layers[0][0], layers[1:])
    arr = np.array([" " if n == '0' else u"\u2588" for n in first_layer])
    arr = arr.reshape(rows, cols)

    for row in arr:
        print("".join(row.tolist()))
