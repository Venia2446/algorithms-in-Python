def binarycount(lst, x, n):
    l, r = 0, len(lst) - 1
    while l <= r:
        m = l + (r - l) // 2
        if lst[m] <= x - n:
            l = m + 1
        elif lst[m] > x - n:
            r = m - 1
    return l
def binary_serch_R(A,p):
        if p>A[len(A)-1]:
            return len(A)
        if p<=A[0]:
            return 0
        if p==A[len(A)-1]:
            i=len(A)
            while p == A[i-1] and i!= 0:
                i-=1
            return i

        else:
            l,r = 0,len(A)-1
            while l<=r:
                m = l + (r - l) // 2
                if A[m] == p:
                    while p == A[m-1] and m!= 0:
                        m-= 1
                    return m
                elif A[m]>p:
                    r = m-1
                else:
                    l = m+1
            if A[m]<p<A[m+1]:
                return m+1

            elif A[m]>p:
                while A[m]<p<A[m+1]:
                    m-=1
                return m
            if A[m]<p:
                while A[m]<p<A[m+1]:
                    m+=1
                return m
def lines_lr_p(LINES):
    l_points, r_points = [], []
    for items in LINES:
        l_points.append(items[0])
        r_points.append(items[1])
    return sorted(l_points), sorted(r_points)
import sys

N_M = [int(i) for i in input().split()]
LINES = [[int(i) for i in sys.stdin.readline().split()] for n in range(N_M[0])]
DOTS = [int(z) for z in input().split()]
GL_ANS = []
ASS_POPINTS = lines_lr_p(LINES)

for p in DOTS:
    left_ANS = binarycount(ASS_POPINTS[0],p,0)
    right_ANS = binarycount(ASS_POPINTS[1], p,1) 
    print (left_ANS-right_ANS, end = ' ')