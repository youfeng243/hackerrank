
def main():
    T = input()
    Q = []
    D = {}
    for _ in xrange( T ):
        Q.append(input())
        D[Q[-1]] = 0
    
    Cal = Q[:]
    Cal.sort()
    j = 0
    PreSum = 0
    Sum = 0
    fab1 = 1
    fab2 = 2
    while j < T:
        if Cal[j] >= fab1 and Cal[j] < fab2:
            D[Cal[j]] = Sum
            j += 1
            continue
        fab3 = fab2 + fab1
        fab1 = fab2
        fab2 = fab3
        if fab1 % 2 == 0:
            Sum += fab1
            
    for i in xrange( T ):
        print D[Q[i]]

if __name__=="__main__":
    main()