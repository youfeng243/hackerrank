
def BinarySearch( first, last, num, P ):
    while first <= last:
        mid = (first + last) / 2
        if num > P[mid] and num <= P[mid + 1]:
            return P[mid]
        if num == P[mid]:
            return P[mid - 1]
        if num > P[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1

def main():
    T = input()
    Q = []
    for _ in xrange(T):
        Q.append(input())
    
    P = []
    for i in xrange( 100, 1000 ):
        for j in xrange( i, 1000 ):
            K = i * j
            string = str(K)
            if string == string[::-1]:
                P.append(K)
                #print K
    P.sort()
    P.append(1000000)
    length = len(P)
    for i in xrange( T ):
        print BinarySearch( 0, length - 1, Q[i], P )
    
if __name__=="__main__":
    main()