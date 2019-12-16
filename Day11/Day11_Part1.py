import sys

def extend(mode, memory, addr):
    m = int(mode)
    if m == 1:
        return

    if (addr >= len(memory)):
        size = addr - len(memory) + 1
        extension = ['0'] * size
        memory.extend(extension)    
    
def set_val(ptr, val, memory, relative_base = None, mode = None):
    m = int(mode) if mode != None else 0
    addr = int(memory[ptr])

    if m == 2:
        addr += relative_base
   
    extend(m, memory, addr)    
    memory[addr] = val

def get_val(mode, memory, i, relative_base):
    m = int(mode)
    
    addr = int(memory[i])
    extend(mode, memory, addr)
       
    if m == 0:
        return int(memory[addr]) 
    elif m == 2:
        return int(memory[relative_base + addr]) 
    
    return addr

def move(current_orientation, turn):
    pointing = current_orientation[0]
    (x, y) = current_orientation[1]    

    if (turn == 0): # left
        if pointing == "up":
            return ("left", (x - 1, y))            
        elif pointing =="down":
            return ("right", (x + 1, y))            
        elif pointing == "right":
            return ("up", (x, y - 1))            
        elif pointing == "left":
            return ("down", (x, y + 1))            
    elif (turn == 1): # right
        if pointing == "up":
            return ("right", (x + 1, y))            
        elif pointing =="down":
            return ("left", (x - 1, y))            
        elif pointing == "right":
            return ("down", (x, y + 1))            
        elif pointing == "left":
            return ("up", (x, y - 1))            

def program(memory, current_orientation, pannels):
    ptr = relative_base = output = colour = 0
    
    while ptr < len(memory):        
        instruction = int(memory[ptr][-2:]) if len(memory[ptr]) > 1 else int(memory[ptr])      
        mode1 = memory[ptr][-3:-2] if len(memory[ptr]) > 2 else 0
        mode2 = memory[ptr][-4:-3] if len(memory[ptr]) > 3 else 0
        mode3 = memory[ptr][0] if len(memory[ptr]) > 4 else 0    
      
        if instruction == 1:  
            val = str(get_val(mode1, memory, ptr + 1, relative_base) + get_val(mode2, memory, ptr + 2, relative_base))
            set_val(ptr + 3, val, memory, relative_base, mode3)
            ptr += 4       
        elif instruction == 2:            
            val = str(get_val(mode1, memory, ptr + 1, relative_base) * get_val(mode2, memory, ptr + 2, relative_base))
            set_val(ptr + 3, val, memory, relative_base, mode3)
            ptr += 4
        elif instruction == 3:
            colour = 0         
            if current_orientation[1] in pannels:
                colour = pannels[current_orientation[1]]
     
            set_val(ptr + 1, str(colour), memory, relative_base, mode1)            

            ptr += 2
        elif instruction == 4:
            val = get_val(mode1, memory, ptr + 1, relative_base)
                   
            if output % 2 == 0:   
                colour = val
                pannels[current_orientation[1]] = colour                 
            else:
                current_orientation = move(current_orientation, val)                
                                       
            ptr += 2
            output += 1
        elif instruction == 5:
            ptr = get_val(mode2, memory, ptr + 2, relative_base) if get_val(mode1, memory, ptr + 1, relative_base) != 0 else ptr + 3
        elif instruction == 6:
            ptr = get_val(mode2, memory, ptr + 2, relative_base) if get_val(mode1, memory, ptr + 1, relative_base) == 0 else ptr + 3
        elif instruction == 7:
            val = '1' if get_val(mode1, memory, ptr + 1, relative_base) < get_val(mode2, memory, ptr + 2, relative_base) else '0'
            set_val(ptr + 3, val, memory, relative_base, mode3)
            ptr += 4            
        elif instruction == 8:
            val = '1' if get_val(mode1, memory, ptr + 1, relative_base) == get_val(mode2, memory, ptr + 2, relative_base) else '0'
            set_val(ptr + 3, val, memory, relative_base, mode3)
            ptr += 4
        elif instruction == 9:
            relative_base += int(get_val(mode1, memory, ptr + 1, relative_base))
            ptr += 2
        elif instruction == 99:
            break
    
    return pannels


if __name__ == "__main__":    
    f = open(sys.argv[1])
    memory =  f.read().split(',')
    f.close()
    
    painted_pannels = program(memory, ("up", (0,0)), {})

    # 2172
    print("Painted panels: ", len(painted_pannels))
    