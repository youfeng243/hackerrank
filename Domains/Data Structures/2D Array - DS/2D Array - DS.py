
def main():
    A = []
    for i in xrange(6):
        temp = map(int, raw_input().strip().split())
        A.append(temp)
    
    Max = -10**10
    for i in xrange( 1, 5 ):
        for j in xrange( 1, 5 ):
            temp = A[i][j] + A[i - 1][j] + A[i + 1][j] + A[i - 1][j - 1] + A[i - 1][j + 1] + A[i + 1][j - 1] + A[i + 1][j + 1]
            Max = max(Max, temp);
    print Max
            
    
if __name__=="__main__":
    main()