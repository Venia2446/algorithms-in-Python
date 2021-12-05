import sys
def hip_down(i,Tree):
    if i*2+2>len(Tree):
        return
    if Tree[i] < Tree[2 * i + 1] or Tree[i] < Tree[2 * i + 2]:
        if Tree[2 * i + 1] > Tree[2*i+2]:
            Tree[i],Tree[2 * i + 1] = Tree[2 * i + 1],Tree[i]
            hip_down(2*i+1,Tree)
        else:
            Tree[i], Tree[2 * i + 2] = Tree[2 * i + 2], Tree[i]
            hip_down(2*i+2,Tree)
def hip_up(i,Tree):
    if Tree[i] < Tree[2 * i + 1] or Tree[i] < Tree[2 * i + 2]:
        check_list = [Tree[i], Tree[2 * i + 1], Tree[2 * i + 2]]
        if Tree[2 * i + 1] == Tree[2 * i + 2]:
            Tree[i] = check_list[2]
            Tree[2 * i + 2] = check_list[0]
            check_list = []
        elif Tree[2 * i + 1] < Tree[2 * i + 2]:
            Tree[i] = check_list[2]
            Tree[2 * i + 2] = check_list[0]
            check_list = []
        elif Tree[2 * i + 1] > Tree[2 * i + 2]:
            Tree[i] = check_list[1]
            Tree[2 * i + 1] = check_list[0]
            check_list = []
    return Tree
def Insert(tree_item):
    global TREE
    TREE.append(tree_item)
def heapyfy(Tree):
    check_list = []
    if len(Tree) == 1:
        return Tree.pop(0)
    if int(len(Tree)) % 2 != 0:
        for i in range(int((len(Tree) - 2) / 2), 0, -1):
            hip_up(i,Tree)

        hip_down(0,Tree)
        Tree[-1], Tree[0] = Tree[0], Tree[-1]
        return Tree.pop(-1)
    else:
        Tree += [0]
        for i in range(int((len(Tree) - 2) / 2), -1, -1):
            hip_up(i, Tree)
        hip_down(0, Tree)
        Tree.pop()
        Tree[-1], Tree[0] = Tree[0], Tree[-1]
        return Tree.pop(-1)
n = int(input())
a = []
for x in range(n):
    a.append(sys.stdin.readline().split())
TREE = []
for obj in a:
    if obj[0] == 'Insert':
        Insert(int(obj[1]))
    if obj[0] == 'ExtractMax':
        print(heapyfy(TREE))