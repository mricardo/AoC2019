import sys


if __name__ == "__main__":    
    f = open(sys.argv[1])

    op = [int(n) for n in f.read().split(',')]

    i = 0
    while i < len(op):        
        if op[i] == 1:
            op[op[i + 3]] = op[op[i + 1]] + op[op[i + 2]]
        elif op[i] == 2:
            op[op[i + 3]] = op[op[i + 1]] * op[op[i + 2]]
        elif op[i] == 99:
            break
        
        i += 4
    
    print(op)
    print(op[0])

    f.close()