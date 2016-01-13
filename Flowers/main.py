#coding=utf-8
N, K = map(int, raw_input().split(" "))
C = map(int, raw_input().strip().split(" "))
C.sort()
C.reverse()
#print C
buy = [0 for i in xrange(K)]

cost = 0
for i in xrange(N):
    cost += (buy[i % K] + 1) * C[i]
    buy[i % K] += 1
print cost

