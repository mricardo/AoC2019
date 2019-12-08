import sys

def transverse_map(o, m):
    total = 0
    while True:
        if o in m:
            total += 1
            o = m[o]
        else:
            break
    return total

if __name__ == '__main__':
    orbits = open(sys.argv[1]).read().splitlines()
    
    m = {}
    for orbit in orbits:
        objects = orbit.split(")")

        m[objects[1]] = objects[0]           

    total = 0
    for o in m:
        total += transverse_map(o, m)

    print('Total: ', total)