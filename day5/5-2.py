class Node:
    def __init__(self, id):
        self.id = id
        self.pages_not_after = set()

def is_valid(array, graph):
    bad_after = set()
    has_before = set()
    for item in array:
        if item in graph.keys():
            curr_node = graph[item]
            bad_after.update(curr_node.pages_not_after)
            has_before.update(curr_node.id)
            if curr_node.id in bad_after:
                return False
    return True

def fix_array(array, graph):
    bad_after = set()
    has_before = set()
    for item in array:
        if item in graph.keys():
            curr_node = graph[item]
            c_id = curr_node.id
            bad_after.update(curr_node.pages_not_after)
            has_before.update(c_id)

            if c_id in bad_after:
                # this id came too late; move it progressively earlier
                # we only have to fix the subarray: from the start to the problem id
                ind = array.index(c_id)
                first_bit = array[:ind + 1]
                tmp = first_bit[ind]
                first_bit[ind] = array[ind-1]
                first_bit[ind-1] = tmp
                array = fix_array(first_bit, graph) + array[ind + 1:]

    return array


graph = {}
sum_of_mid = 0

with open("in.txt", "r") as f:
    for line in f:
        if "|" in line:
            # be aware: this assumes nums always 2 digits
            num1 = line[0:2].strip()
            num2 = line[3:].strip()
            if num2 not in graph.keys():
                new_n2 = Node(num2)
                graph[num2] = new_n2
            else:
                new_n2 = graph[num2]
            new_n2.pages_not_after.add(num1)
        
        elif line:
            pages = [value.strip() for value in line.split(",")]

            # this doubles work - could consolidate functions but am already so behind lol
            if not is_valid(pages, graph):
                arr = fix_array(pages, graph)
                mp_ind = len(arr) // 2
                sum_of_mid += int(arr[mp_ind])

    print(sum_of_mid)


