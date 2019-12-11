import sys
import numpy as np

if __name__ == "__main__":
    f = open(sys.argv[1])
    line =  f.read()       
    f.close()

    rows = 25
    cols = 6
    
    i = 0    
    min_zeros = min_layer = min_res = -1
    while i * (rows*cols) < len(line):
        start = i * (rows*cols)
        end = (i + 1) * (rows*cols)
        
        l = line[start:end]
        
        zeros = l.count('0')
        if min_zeros == -1 or (zeros > 0 and zeros < min_zeros):
            min_zeros = zeros
            min_layer = i + 1
            ones = l.count('1')
            twos = l.count('2')            
            min_res = ones * twos      
        
        i += 1

    print("Total Layers: ", i, " Min. Layer: ", min_layer, " Min. 1s x 2s: ", min_res)