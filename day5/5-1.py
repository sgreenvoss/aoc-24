class Node:
    def __init__(self, id):
        self.id = id
        self.pages_after = set()
        self.pages_before = set()

        #possibly needed:
        self.pages_not_before = set()
        self.pages_not_after = set()

def is_valid(array, graph):
    bad_after = set()
    has_before = set()
    for item in array:
        if item in graph.keys():
            curr_node = graph[item]
            bad_after.update(curr_node.pages_not_after)
            has_before.update(curr_node.id)
            # print("current id: ", curr_node.id)
            # print("bad after: ", bad_after)
            if curr_node.id in bad_after or not has_before.isdisjoint(curr_node.pages_not_before):
                return False
    # print("bad after was:", [node for node in bad_after])
    return True

graph = {}
sum_of_mid = 0

with open("in.txt", "r") as f:
    for line in f:
        if "|" in line:
            print(line)
            # be aware: this assumes nums always 2 digits
            num1 = line[0:2].strip()
            num2 = line[3:].strip()

            if num2 not in graph.keys():
                new_n2 = Node(num2)
                graph[num2] = new_n2
            else:
                new_n2 = graph[num2]

            if num1 not in graph.keys():
                n1 = Node(num1)
                graph[num1] = n1
            else:
                n1 = graph[num1]
                
            n1.pages_not_before.add(num2)
            new_n2.pages_not_after.add(num1)
        
        else:
            # we know it's an array
            pages = [value.strip() for value in line.split(",")]
            # print(pages)
            if is_valid(pages, graph):
                mp_ind = len(pages) // 2
                sum_of_mid += int(pages[mp_ind])
    # for node in graph.values():
    #     print("id: ", node.id)
    #     print("not after", [node.id for node in node.pages_not_after])
    #     print("not before", [node.id for node in node.pages_not_before])
    #     print()
    print(sum_of_mid)


