f = open("in.txt", "r")

directions = {
    "ur" : (-1, 1),
    "ul" : (-1, -1),
    "dr" : (1, 1),
    "dl" : (1, -1)
}


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


def is_mas(x, y):
    # this is so garb - will refactor lator 
    try:
        assert 0 <= x < x_bound and 0 <= y < y_bound
        curr_dir = directions["ur"]
        ur = matrix[x + curr_dir[0]][y+curr_dir[1]]
        curr_dir = directions["dl"]
        dl = matrix[x + curr_dir[0]][y+curr_dir[1]]
        if (ur == dl) or not (ur in "MS" and dl in "MS"):
            return False
        curr_dir = directions["ul"]
        ul = matrix[x + curr_dir[0]][y+curr_dir[1]]
        curr_dir = directions["dr"]
        dr= matrix[x + curr_dir[0]][y+curr_dir[1]]
        if (ul == dr) or not (ul in "MS" and dr in "MS"):
            return False
        
        return True

    except:
        return False
    
    return False

trues = 0
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "A":
            trues += is_mas(x, y)

print(trues)
