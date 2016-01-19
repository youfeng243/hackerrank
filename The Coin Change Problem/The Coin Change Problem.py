#错误的
#coding=utf-8
#a[n] += a[n - c[i]]
#a[1] = 1

M,N = map(int, raw_input().strip().split())
coin = map(int, raw_input().strip().split())
coin.sort()
DP = [0 for _ in xrange(M + 1)]

'''
for j in xrange(N):
    if coin[j] <= M:
        DP[coin[j]] = 1
'''
#print DP
#DP[coin[0]] = 1
for i in xrange(0, M + 1):
    for j in xrange(N):
        if i >= coin[j]:
            if i - coin[j] == 0:
                DP[i] += 1
            else:
                DP[i] += DP[i - coin[j]]
            
print DP[M]