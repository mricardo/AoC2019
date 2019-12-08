import sys

if __name__ == "__main__":    
    f = open(sys.argv[1])
    op =  f.read().split(',')
    f.close()

    pos = lambda mode, op, i : int(op[int(op[i])]) if int(mode) == 0 else int(op[i])

    i = 0
    
    while i < len(op):        
        instruction = int(op[i][-2:]) if len(op[i]) > 1 else int(op[i])      
        mode1 = op[i][-3:-2] if len(op[i]) > 2 else 0
        mode2 = op[i][-4:-3] if len(op[i]) > 3 else 0
        mode3 = op[0] if len(op[i]) > 4 else 0        

        if instruction == 1:
            op[int(op[i + 3])] = str(pos(mode1, op, i + 1) + pos(mode2, op, i + 2))
            i += 4       
        elif instruction == 2:            
            op[int(op[i + 3])] = str(pos(mode1, op, i + 1) * pos(mode2, op, i + 2))
            i += 4
        elif instruction == 3:
            val = input('Input: ')
            op[int(op[i + 1])] = str(val)
            i += 2
        elif instruction == 4:
            print('Output: ', pos(mode1, op, i + 1))            
            i += 2
        elif instruction == 5:
            i = pos(mode2, op, i + 2) if pos(mode1, op, i + 1) != 0 else i + 3
        elif instruction == 6:
            i = pos(mode2, op, i + 2) if pos(mode1, op, i + 1) == 0 else i + 3
        elif instruction == 7:
            op[int(op[i + 3])] = '1' if pos(mode1, op, i + 1) < pos(mode2, op, i + 2) else '0'
            i += 4
        elif instruction == 8:
            op[int(op[i + 3])] = '1' if pos(mode1, op, i + 1) == pos(mode2, op, i + 2) else '0'
            i += 4
        elif instruction == 99:
            break