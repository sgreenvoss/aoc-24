import re
f = open("in.txt", "r")
total = 0

for line in f:
    found = re.findall("mul\((\d*),(\d*)\)", line)
    for item in found:
        res = int(item[0]) * int(item[1])
        total += res

print("total is", total)