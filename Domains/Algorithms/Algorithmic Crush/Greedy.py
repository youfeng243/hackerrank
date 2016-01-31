#coding=utf-8

def main():
    N,M = map(int, raw_input().strip().split())
    
    Max = 0
    A = [0] * (N + 2)
    for _ in xrange( M ):
        a,b,k = map(int, raw_input().strip().split())
        A[a] += k
        A[b + 1] += -k
        
    for i in xrange( 1, N + 1 ):
        A[i] += A[i - 1]
        Max = max(Max, A[i])
        
    print Max
    
if __name__ == "__main__":
    main()