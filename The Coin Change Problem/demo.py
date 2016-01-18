
M,N = map(int, raw_input().strip().split())
coin = map(int, raw_input().strip().split())
coin.sort()
DP = [0 for _ in xrange(M + 1)]

for i in xrange(N):
    j = coin[i]
    DP[j] = 1
    while j <= M:
        DP[j]