#coding=utf-8
#Counting Sort 2

N = input()
A = map(int, raw_input().strip().split())
rank = [0 for i in xrange(N + 1)]
count = [0 for i in xrange(100)]

for i in xrange(N):
    count[A[i]] += 1

for i in xrange(1, 100):
    count[i] += count[i - 1]

for i in xrange(N):
    count[A[i]] -= 1
    rank[count[A[i]]] = A[i]

for i in xrange(N):
    print rank[i],
print ""
