#coding=utf-8
#Find the Median

N = input()

A = map(int, raw_input().strip().split())
mid = N / 2

Max = max(A)
Min = min(A)

num = Max - Min + 1
count = [0 for i in xrange(num)]
for i in xrange(N):
    A[i] -= Min
    count[A[i]] += 1
for i in xrange( num ):
    if mid >= count[i]:
        mid -= count[i]
    else:
        mid = i
        break
print mid + Min
        