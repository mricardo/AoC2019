def gravity (v, p1, p2):
    if p1 < p2:
        return v + 1
    elif (p1 > p2):
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

def calculate_total_energy(pos_moons, vel_moons):
    total_energy = potential_energy = kinetic_energy = 0

    i = 0 
    while i < len(pos_moons):          
        potential_energy = abs(pos_moons[i][0]) + abs(pos_moons[i][1]) + abs(pos_moons[i][2])
        kinetic_energy = abs(vel_moons[i][0]) + abs(vel_moons[i][1]) + abs(vel_moons[i][2])        

        total_energy += potential_energy * kinetic_energy

        i += 1         

    return total_energy

def simulate(pos_moons, total_time_steps):
    time_steps = 0

    vel_moons = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]    

    while (time_steps < total_time_steps):        
        vel_moons = apply_gravity(pos_moons, vel_moons)        
        pos_moons = apply_velocity(pos_moons, vel_moons)    

        time_steps += 1

    return calculate_total_energy(pos_moons, vel_moons)            

if __name__ == "__main__":
    pos_moons = [(3, 15, 8), (5, -1, -2), (-10, 8, 2), (8, 4, -5)]

    total_time_steps = 1000

    total_energy = simulate(pos_moons, total_time_steps)

    print("Total Energy: ", total_energy)