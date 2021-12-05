import sys
def packege_find(W,n,F):

    D = [[0 for i in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            D[i][w] = D[i-1][w]
            if F[i-1]<=w:
                D[i][w] = max(D[i][w],D[i-1][w-F[i-1]]+F[i-1])
    return D[n][W]
def main():
    Impt1 = [list(map(int,sys.stdin.readline().split())) for n in range(2)]
    ANS = packege_find(Impt1[0][0],Impt1[0][1],Impt1[1])
    print(ANS)
if __name__=='__main__':
    main()
