def dable_merge(x,y):
    global k
    i,j,z = 0,0,[]
    while i in range(len(x)) and j in range(len(y)):
        if len(x) == 0:
            z = y
            i+=1
            break
        if len(y) == 0:
            j+=1
            z = y
            break
        elif x[i]<=y[j]:
            z+=[x[i]]
            i+=1
        else:
            z+=[y[j]]
            j+=1
            k+=len(x)-i
    if i == len(x):
        z+=y[j::]
    else:
        z+=x[i::]
    return z

def merge_sort(A):

        if len(A) > 1:
            m = len(A) // 2
            return dable_merge(merge_sort(A[0:m]), merge_sort(A[m:]))
        else:
            return A

import sys
N = int(input())
G_list = list(map(int,sys.stdin.readline().split()))

k=0
F = merge_sort(G_list)

print(k)