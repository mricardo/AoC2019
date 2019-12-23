import numpy as np

def gravity (v, p1, p2):
    if p1 < p2:
        return v + 1
    elif p1 > p2:
        return v + (-1)
    return v

def apply_gravity(pos_moons, vel_moons):    
    i = 0    

    while i < len(pos_moons):
        (x1, y1, z1) = pos_moons[i]
        
        j = 0
        while j < len(pos_moons):
            if (i != j):                
                (x2, y2, z2) = pos_moons[j]                            
                vel_moons[i] = (gravity(vel_moons[i][0], x1, x2), gravity(vel_moons[i][1], y1, y2), gravity(vel_moons[i][2], z1, z2))            
            j += 1
        i += 1

    return vel_moons

def apply_velocity(pos_moons, vel_moons):
    i = 0

    velocity = lambda pos, vel, i : (pos[i][0] + vel[i][0], pos[i][1] + vel[i][1], pos[i][2] + vel[i][2])

    while i < len(pos_moons):
        pos_moons[i] = velocity(pos_moons, vel_moons, i) 
        i += 1

    return pos_moons

def simulate(pos_moons):
    vel_moons = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

    start_pos = pos_moons.copy()    
    start_vel = vel_moons.copy()    
    period = [-1, -1, -1]    

    equal = lambda a, b, i: True if (a[0][i], a[1][i], a[2][i], a[3][i]) == (b[0][i], b[1][i], b[2][i], b[3][i]) else False
    
    time_steps = 0
    while True:                  
        time_steps += 1

        vel_moons = apply_gravity(pos_moons, vel_moons)       
        pos_moons = apply_velocity(pos_moons, vel_moons)

        for i in range(3):
            if (period[i] == -1 and equal(pos_moons, start_pos, i) and equal(vel_moons, start_vel, i)):                
                period[i] = time_steps                
        
        if (period[0] != -1 and period[1] != -1 and period[2] != -1):
            break                              
       
    return np.lcm.reduce([period[0], period[1], period[2]], dtype=np.int64)         

if __name__ == "__main__":
    pos_moons = [(3, 15, 8), (5, -1, -2), (-10, 8, 2), (8, 4, -5)]

    print("Total Steps: ", simulate(pos_moons)) 