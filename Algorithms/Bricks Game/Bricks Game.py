#coding=utf-8
#Bricks Game

T = input()
for _ in xrange(T):
    N = input()
    num = map(int, raw_input().strip().split())
    
    if N <= 4:
        print sum(num[0:4])
        continue
    
    DP = [0 for i in xrange(N + 1)]
    
    DP[1] = num[0]
    DP[2] = num[0] + num[1]
    DP[3] = num[0] + num[1] + num[2]
    DP[4] = max( DP[2] + num[3], DP[1] + num[3] )
    for i in xrange( 5, N + 1 ):
        DP[i] = max( DP[i - 2] + num[i - 1] , DP[i - 3] + num[i - 1], DP[i - 4] + num[i - 1] )
    print DP[N]