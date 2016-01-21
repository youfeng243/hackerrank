#coding=utf-8
#Max-Sum-Subarray

N = input()
a = map(int, raw_input().strip().split())

Max = 0
temp = 0
for i in xrange(N):
    if a[i] == 0:
        if temp > 0:
            Max = max(Max, temp)
        temp = 0
        continue
    if temp + a[i] >= 0:
        temp += a[i]
    else:
        temp = 0
    if temp > 0:
        Max = max(Max, temp)
print Max