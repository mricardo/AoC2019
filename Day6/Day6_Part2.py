import sys

def transverse_map(o, m):
    orbits = []
    while True:
        if o in m:
            orbits.append(o)
            o = m[o]
        else:
            orbits.append(o)
            break
    return orbits

if __name__ == '__main__':
    orbits = open(sys.argv[1]).read().splitlines()
    
    m = {}
    for orbit in orbits:
        objects = orbit.split(")")

        m[objects[1]] = objects[0]       

    you = transverse_map('YOU', m)
    san = transverse_map('SAN', m)
   
    min = None
    for y in you:        
        if y in san:
            idx_you = you.index(y) - 1
            idx_sam = san.index(y) - 1
            if not min or min > idx_you + idx_sam:
                min = idx_you + idx_sam

    print("Minimum: ", min)                