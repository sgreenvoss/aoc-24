f = open("in.txt", "r")
levels = [] # value : count
safe2= 0
safe1 = 0

def check_line(line, dampening=True):
    """takes line (parsed), returns 1 (safe) or 0 (unsafe)"""
    i = 0
    canonical_sign = (line[0] - line[1]) >= 0

    while i < len(line) - 1: 
        delta = line[i] - line[i+1]
        sign_curr = delta >= 0
        
        if sign_curr != canonical_sign or not(0 < abs(delta) < 4):
            # problem encountered
            if dampening:
                test_line = line.copy()
                test_other = line.copy()
              
                del test_line[i]
                del test_other[i+1]

                return int(check_line(test_other, False) + check_line(test_line, False) >= 1)
         
            else:
                return 0
        i += 1

    return 1

for line in f:
    line = line.split(" ")
    line = [int(item) for item in line]

    safe1 += check_line(line, False)
    safe2 += check_line(line)
    
   
print("safe without dampening:", safe1)
print("safe with dampening:", safe2)

