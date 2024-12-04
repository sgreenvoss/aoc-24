f = open("in.txt", "r")
list1 = [] # num : value
list2 = [] # value : num
inc = 0

for line in f:
    line = line.split("   ")
    list1.append((inc, int(line[0])))
    list2.append((inc, int(line[1].strip())))
    inc += 1

list1.sort(key=lambda item: item[1])
list2.sort(key=lambda item: item[1])
print(list2)
print(list1)

total_dist = 0
for i in range(len(list1)):
    total_dist += abs(list1[i][1] - list2[i][1])

print(total_dist)