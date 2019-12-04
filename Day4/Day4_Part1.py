def valid_pwd(candidate):
    duplicate = False
    i = 0
    while i < len(candidate) - 1:
        res = candidate[i] - candidate[i + 1]
        if res > 0:
            return False
        
        if res == 0:
            duplicate = True

        i += 1
    
    return duplicate

if __name__ == "__main__":    
    count = 0
    for i in range(134564, 585160):
        digits = list(map(int, str(i)))

        if (valid_pwd(digits)):
            count += 1
    
    print(count)
