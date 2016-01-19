
M,N = map(int, raw_input().strip().split())
coin = map(int, raw_input().strip().split())
#coin.sort()
DP = [0 for _ in xrange(M + 1)]
DP[0] = 1
for i in xrange( N ):
    for j in xrange(coin[i],  M + 1 ):
        DP[j] += DP[j - coin[i]]
print DP[M]