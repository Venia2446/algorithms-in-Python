
def HRP(A,n):
    prev = []
    inf = 10**10
    L = [inf]+[-inf]*(n+1)
    for i in range(n):
        left = 0
        right = n+1
        while left+1<right:
            middle = (left+right)//2
            if L[middle]>=A[i]:
                left = middle
            else:
                right = middle
        L[right] = A[i]
        prev.append([right, i, A[i]])
    i = n+1
    while L[i] == -inf:
        i-=1
    count = i
    result = []

    while count!=0:
        for items in prev[::-1]:
            if items[0] == count:
                result+=[items[1]+1]
                count-=1
    result=list(reversed(result))

    return(i,result)

n = int(input())
Q = input().split()
A = list(map(int,Q))


ANS = HRP(A,n)
print(ANS[0])
print(*ANS[1])
