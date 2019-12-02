import sys
import itertools

if __name__ == "__main__":    
    f = open(sys.argv[1])

    op_original = [int(n) for n in f.read().split(',')]

    nouns = range(99)
    verbs = range(99)

    for perm in itertools.product(nouns, verbs):
        op = op_original.copy()    
        op[1] = perm[0]
        op[2] = perm[1]

        i = 0
        while i < len(op):        
            if op[i] == 1:
                op[op[i + 3]] = op[op[i + 1]] + op[op[i + 2]]
            elif op[i] == 2:
                op[op[i + 3]] = op[op[i + 1]] * op[op[i + 2]]
            elif op[i] == 99:
                break
            
            i += 4
        
        if (op[0] == 19690720):
            print("op[0]", op[0], "noun: ", op[1], " verb: ", op[2])
            break

    f.close()