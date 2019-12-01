import sys
import math

if __name__ == "__main__":
    sum = 0
    with open(sys.argv[1]) as lines:
        for line in lines:
            number = int(line)
            sum += math.floor((number / 3)) - 2
    print(sum)