T = input()

for _ in xrange(T):
    n,k = map(int, raw_input().strip().split())
    c = map(int, raw_input().strip().split())
    
    dp = [ 0 for i in xrange(k + 1) ]
    for i in xrange(n):
        for j in xrange( c[i], k + 1 ):
            dp[j] = max(dp[j - c[i]] + c[i], dp[j])
    print dp[k]