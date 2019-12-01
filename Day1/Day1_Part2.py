import sys
import math

if __name__ == "__main__":
    total = 0
    with open(sys.argv[1]) as lines:
        for line in lines:
            fuel = int(line)          
            while (fuel > 5):  
                fuel = math.floor(fuel / 3) - 2                
                total += fuel

    print(total)