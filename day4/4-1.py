f = open("in.txt", "r")

lookup = {
    "X" : "M",
    "M" : "A",
    "A" : "S",
    "S" : "yay"
}

directions = {
    "up" : (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "ur" : (-1, 1),
    "ul" : (-1, -1),
    "dr" : (1, 1),
    "dl" : (1, -1)
}
#"up", "down", "left", "right", "ur", "ul", "dr", "dl"
all_directions = ["up", "down", "left", "right", "ur", "ul", "dr", "dl"]
sums = [0 for direction in all_directions]

# set up a 2d matrix
matrix = []

ind = -1
for line in f:
    goodline = line.strip()
    matrix.append([])
    ind+=1
    for char in goodline:
        matrix[ind].append(char)

# let's establish the boundaries
x_bound = len(matrix[0])
y_bound = len(matrix)


def look_somewhere(x, y, direction, character):
    curr_dir = directions[direction]

    # try to look up:
    try:
        next_char = lookup[character]
        assert 0 <= x < x_bound and 0 <= y < y_bound
        
        next_x = x + curr_dir[0]
        next_y = y + curr_dir[1]

        if next_char == "yay":
            return 1
        
        if matrix[next_x][next_y] == next_char:
            return look_somewhere(next_x, next_y, direction, next_char)  

    except:
        return 0
    
    return 0


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "X":
            for i in range(len(all_directions)):
                sums[i] += look_somewhere(x, y, all_directions[i], "X")

print(sum(sums))
