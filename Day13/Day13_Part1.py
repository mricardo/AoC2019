import sys

def extend(mode, memory, ptr):
    m = int(mode)
    if m == 1:
        return

    if (ptr >= len(memory)):
        diff = ptr - len(memory) + 1
        extension = ['0'] * diff
        memory.extend(extension)    
    
def set_val(ptr, val, relative_base = None, mode = None):
    m = int(mode) if mode != None else 0
    addr = int(memory[ptr])

    if m == 2:
        addr += relative_base
   
    extend(m, memory, addr)    
    memory[addr] = val

def get_val(mode, op, i, relative_base):
    m = int(mode)
    extend(mode, op, i)
    addr = int(op[i])
    
    if m == 0:
        return int(op[addr]) 
    elif m == 2:
        return int(op[relative_base + addr]) 
    
    return addr

def program():
    ptr = 0
    relative_base = 0
    outputs = []
    while ptr < len(memory):        
        instruction = int(memory[ptr][-2:]) if len(memory[ptr]) > 1 else int(memory[ptr])      
        mode1 = memory[ptr][-3:-2] if len(memory[ptr]) > 2 else 0
        mode2 = memory[ptr][-4:-3] if len(memory[ptr]) > 3 else 0
        mode3 = memory[ptr][0] if len(memory[ptr]) > 4 else 0    

        if instruction == 1:  
            val = str(get_val(mode1, memory, ptr + 1, relative_base) + get_val(mode2, memory, ptr + 2, relative_base))
            set_val(ptr + 3, val, relative_base, mode3)
            ptr += 4       
        elif instruction == 2:            
            val = str(get_val(mode1, memory, ptr + 1, relative_base) * get_val(mode2, memory, ptr + 2, relative_base))
            set_val(ptr + 3, val, relative_base, mode3)
            ptr += 4
        elif instruction == 3:
            val = input('Input: ')
            set_val(ptr + 1, str(val), relative_base, mode1)
            ptr += 2
        elif instruction == 4:
            val = get_val(mode1, memory, ptr + 1, relative_base)
            #print('Output: ', val)
            outputs.append(val)
            ptr += 2
        elif instruction == 5:
            ptr = get_val(mode2, memory, ptr + 2, relative_base) if get_val(mode1, memory, ptr + 1, relative_base) != 0 else ptr + 3
        elif instruction == 6:
            ptr = get_val(mode2, memory, ptr + 2, relative_base) if get_val(mode1, memory, ptr + 1, relative_base) == 0 else ptr + 3
        elif instruction == 7:
            val = '1' if get_val(mode1, memory, ptr + 1, relative_base) < get_val(mode2, memory, ptr + 2, relative_base) else '0'
            set_val(ptr + 3, val, relative_base, mode3)
            ptr += 4            
        elif instruction == 8:
            val = '1' if get_val(mode1, memory, ptr + 1, relative_base) == get_val(mode2, memory, ptr + 2, relative_base) else '0'
            set_val(ptr + 3, val, relative_base, mode3)
            ptr += 4
        elif instruction == 9:
            relative_base += int(get_val(mode1, memory, ptr + 1, relative_base))
            ptr += 2
        elif instruction == 99:
            break
    return outputs

if __name__ == "__main__":    
    f = open(sys.argv[1])
    memory =  f.read().split(',')
    f.close()
    
    outputs = program()    

    empty_tiles =[]    
    walls = []
    blocks = []    
    horizontal_paddle = []
    ball = []

    i = 0
    while i < len(outputs):
        x = outputs[i]
        y = outputs[i + 1]
        tile_id = outputs[i + 2]

        if tile_id == 0:
            empty_tiles.append((x, y))

        if tile_id == 1:
            walls.append((x, y))

        if tile_id == 2:
            blocks.append((x, y))

        if tile_id == 3:
            horizontal_paddle.append((x,y))

        if tile_id == 4:
            ball.append((x,y))

        i += 3

    print("Total Empty Tiles: ", len(empty_tiles))
    print("Total Walls: ", len(walls))
    print("Total Blocks: ", len(blocks))
    print("Total Horizontal Paddles: ", len(horizontal_paddle))
    print("Total Ball: ", len(ball))
    
  