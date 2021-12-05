import sys
FIND_LIST = [int(z) for z in sys.stdin.readline().rstrip().split()]
MEMBERS_LIST = [int(z) for z in sys.stdin.readline().rstrip().split()]
N = FIND_LIST.pop(0)
MEMBERS_LIST.pop(0)
min_memb, max_memb = 0, N-1
for numb in MEMBERS_LIST:
    while min_memb <= max_memb:
        m = ((max_memb+min_memb)//2)
        if FIND_LIST [m] == numb:
            print(m+1,end = ' ')
            min_memb, max_memb = 0, N-1
            break
        elif FIND_LIST[m] > numb:
            max_memb = m - 1
        else:
            min_memb = m+1
    if max_memb < min_memb:
        print(-1,end = ' ')
        min_memb, max_memb = 0, N - 1