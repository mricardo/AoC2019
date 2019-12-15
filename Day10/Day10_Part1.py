import sys

def direct_line_sight(asteroids, center, m = None):
    slopes = []
    intersections = 0
    for asteroid in asteroids:
        if (asteroid == center):
            continue

        (cx, cy) = center
        (sx, sy) = asteroid    

        if (cy - sy) != 0 and (cx - sx) != 0:
            s = (cy - sy) / (cx - sx)
            slope = ("slope", s) if sy > cy else ("-slope", s)
        elif (cx - sx) == 0:
            slope = ("x", cx) if sy > cy else ("-x", cx)
        elif (cy - sy) == 0:
            slope = ("y", cy) if sx > cx else ("-y", cy)
               
        if slope not in slopes:
            slopes.append(slope)
            intersections += 1

            if m:                
                m[sy] = m[sy][:sx] + 'O' + m[sy][sx+1:]
       
    return intersections

if __name__ == "__main__":
    i = 0
    asteroids = []
    m = []
    with open(sys.argv[1]) as lines:
        for line in lines:
             asteroids += [(pos, i) for pos, char in enumerate(line) if char == "#"]
             i += 1
             m.append(line.rstrip("\n"))

    max_detection = -1
    max_location = None
    max_map = None
    for asteroid in asteroids:
        current_map = m.copy()
        count = direct_line_sight(asteroids, asteroid, current_map)
        if max_detection == -1 or count > max_detection:
            max_detection = count
            max_location = asteroid
            max_map = current_map        

        
    print("\n".join(max_map))
    print("Max Location: ", max_location, " Max Detection: ", max_detection)