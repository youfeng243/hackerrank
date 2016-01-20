#coding=utf-8

N = input()
count = [0 for i in xrange(100)]
A = map(int, raw_input().strip().split())

for i in A:
    count[i] += 1
for i in xrange(100):
    print count[i],
print ""
