#coding=utf-8
N, K = map(int, raw_input().strip().split(" "))
b = map(int, raw_input().strip().split(" "))
#print N,K
#print numlist
b.sort()

dic = {}
for i in xrange(N):
    dic[b[i]] = i

answer = 0
for i in xrange(N):
    if b[i] + K in dic:
        answer += 1
print answer
