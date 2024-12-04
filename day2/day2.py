f = open("in.txt", "r")
levels = [] # value : count
safe = 0


for line in f:
    line = line.split(" ")
    line = [int(item) for item in line]
    print(line)

    i = 0
    bad = False
    canonical_sign = (line[0] - line[1]) >= 0
    while i < len(line) - 1 and not bad: 
        delta = line[i] - line[i+1]
        sign_curr = delta >= 0
        if sign_curr != canonical_sign or not(0 < abs(delta) < 4):
            bad = True
        i += 1
    if not bad: 
        safe += 1
   
    
print("safe: " + str(safe))
# for item in list1:
#     if item in list2.keys():
#         print("list 2" + str(list2[item]))
#         res += item * list2[item]

# print(res)
