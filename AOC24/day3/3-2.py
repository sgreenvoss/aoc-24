import re
f = open("in.txt", "r")
file = f.read()
total = 0

goodguys = ""
list_line = file.split("do()")

for item in list_line:
    splitted = item.split("don't()")
    # everything after splitted won't include do() (already splat on that thang)
    # so we can just consider the first bit before the first don't()
    goodguys += splitted[0]

# now we can run part one on the concatenated string
found = re.findall("mul\((\d*),(\d*)\)", goodguys)
print(found)
for item in found:
    res = int(item[0]) * int(item[1])
    total += res

print("total is:", total)
  