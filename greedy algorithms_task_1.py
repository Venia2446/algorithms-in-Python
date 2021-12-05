from operator import itemgetter
def Global_Answer(list):
    print(len(list))
    print(*list)
def find_min(a):
    z = []
    for lines in a:
        z += [lines[1]]
    return min(z)
def find_points(a):
    global Global_list
    q = a.copy()
    global i
    if len(a) == 0:
        return Global_Answer((Global_list))
    else :
        new = find_min(a)
        for lines in a:
            if lines[0]<= new:
                q.remove(lines)
        Global_list+=[new]
        return find_points(q)
n = int(input())
a = [[int(i) for i in input().split()] for n in range (n)]
a = sorted(a,key = itemgetter(1))
Global_list = []
find_points(a)