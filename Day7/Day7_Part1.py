import sys

def run_program(op, inputs = [], outputs = None):
    op = op.copy()
    pos = lambda mode, op, i : int(op[int(op[i])]) if int(mode) == 0 else int(op[i])

    i = 0

    idx_inputs = 0    

    while i < len(op):        
        instruction = int(op[i][-2:]) if len(op[i]) > 1 else int(op[i])      
        mode1 = op[i][-3:-2] if len(op[i]) > 2 else 0
        mode2 = op[i][-4:-3] if len(op[i]) > 3 else 0
        _ = op[0] if len(op[i]) > 4 else 0        

        if instruction == 1:
            op[int(op[i + 3])] = str(pos(mode1, op, i + 1) + pos(mode2, op, i + 2))
            i += 4       
        elif instruction == 2:            
            op[int(op[i + 3])] = str(pos(mode1, op, i + 1) * pos(mode2, op, i + 2))
            i += 4
        elif instruction == 3:
            if not inputs:
                val = input('Input: ')
            else:
                val = inputs[idx_inputs]
                idx_inputs += 1

            op[int(op[i + 1])] = str(val)
            i += 2
        elif instruction == 4:   
            val = pos(mode1, op, i + 1)
            if outputs == None:
                print('Output: ', val)            
            else:
                outputs.append(str(val))

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

def run_amplifier(amp, curr_phases, signal, op): 
     curr_phases = curr_phases.copy()        
     current_setting = [(-1, -1)]
     max_all_amplifiers = []
     for phase in range(5):        
        if phase in curr_phases:
            continue

        curr_phases.append(phase)
        op = op.copy()    

        inputs = [phase, signal]    
        outputs = []
        run_program(op, inputs, outputs)
       
        if (amp + 1 < 5):
            all_amplifiers = run_amplifier(amp + 1, curr_phases, outputs[0], op)
        else:
            all_amplifiers = [(phase, outputs[0])]

        exit_signal = all_amplifiers[-1][1]
            
        if len(max_all_amplifiers) == 0 or (int(exit_signal) > int(max_all_amplifiers[-1][1])):
            current_setting = [(phase, outputs[0])]
            max_all_amplifiers = all_amplifiers
        
        curr_phases.remove(phase)
         
     if (amp + 1 < 5):
        current_setting += max_all_amplifiers
     
     return current_setting

if __name__ == "__main__":    
    f = open(sys.argv[1])
    op =  f.read().split(',')
   
    f.close()

    amp = 0
    curr_phase = []
    signal = 0
    
    final_setting = run_amplifier(amp, curr_phase, signal, op)
    
    phases = "".join([str(phase) for (phase, signal) in final_setting])
    print("Phase: ", phases)
    print("Highest Signal: ", final_setting[-1][1])

    
    
   