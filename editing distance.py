def diff_C(A,B,i,j):
    if A[j-1]==B[i-1]:
        return 0
    else:
        return 1
import sys
def range_Levenstain(A,B):
    line_1 = [i for i in range(len(B)+1)]
    for j in range(1,len(A)+1):
        line_2 = [j]
        for i in range(1,len(B)+1):
            c = diff_C(A,B,i,j)
            CHECK = [line_1[i]+1,line_1[i-1]+c,line_2[i-1]+1]
            line_2.append(min(line_1[i]+1,line_1[i-1]+c,line_2[i-1]+1))
        j+=1
        line_1=line_2
    return line_2[-1]
def main():
    LIST = list(sys.stdin.readline().split() for n in range(2))
    ANS = range_Levenstain(*LIST[0],*LIST[1])
    print(ANS)
if __name__=="__main__":
    main()
