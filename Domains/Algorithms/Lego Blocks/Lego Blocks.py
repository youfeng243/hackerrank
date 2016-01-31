T = input()
for _ in xrange(T):
    N,M = map(int, raw_input().strip().split())
    DP = [[0 for i in xrange(M + 1)] for j in xrange(N + 1)]
    DP[0][0] = 1
    for i in xrange(1, N + 1):
        for j in xrange(1, M + 1):
            if i >= 1 and j >= 1:
                DP[i][j] += DP[i - 1][j - 1]
            if i >= 1 and j >= 2:
                DP[i][j] += DP[i - 1][j - 2]
            if i >= 1 and j >= 3:
                DP[i][j] += DP[i - 1][j - 3]
            if i >= 2 and j >= 1:
                DP[i][j] += DP[i - 2][j - 1]
            if i >= 3 and j >= 1:
                DP[i][j] += DP[i - 3][j - 1]
    print DP[N][M] % 1000000007