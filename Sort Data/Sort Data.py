N,M = map(int, raw_input().strip().split())
List = []
for i in xrange(N):
    List.append(map(int, raw_input().strip().split()))
    #print List[i]
K = input()    

List.sort( lambda x, y: x[K] - y[K] )
for i in xrange(N):
    for j in xrange(M):
        print List[i][j],
    print ""