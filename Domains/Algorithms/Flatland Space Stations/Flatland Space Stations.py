
def BinarySearch( num, first, last, C ):
    
    dis = 10 ** 6
    while first <= last:
        mid = ( first + last ) / 2
        dis = min( dis, abs(num - C[mid]) )
        if num > C[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return dis
    
def main():
    N,M = map(int,raw_input().strip().split())
    C = map(int,raw_input().strip().split())
    
    if M == N:
        print 0
        return
    
    C.sort()
    A = [0] * N
    
    for i in C:
        A[i] = 1
    
    Max = 0
    for i in xrange( N ):
        if A[i] == 1:
            continue
        
        dis = BinarySearch( i, 0, M - 1, C )
        Max = max( Max, dis )
        #print dis
    
    print Max
    
    
if __name__=="__main__":
    main()