f = open("in.txt", "r")
list1 = [] # value : count
list2 = {} # value : count
inc = 0

for line in f:
    line = line.split("   ")
    in1 = int(line[0])
    list1.append(in1)

    in2 = int(line[1].strip())
    if in2 not in list2:
        list2[in2] = 1
    else:
        list2[in2] += 1
    
res = 0

for item in list1:
    if item in list2.keys():
        print("list 2" + str(list2[item]))
        res += item * list2[item]

print(res)
