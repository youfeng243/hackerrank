#coding=utf-8
#Running Time of Algorithms
N = input()
a = map(int, raw_input().strip().split())

cnt = 0
for i in xrange(1, N):
    if a[i - 1] <= a[i]:
        continue
    temp = a[i]
    j = i - 1
    while j >= 0 and temp < a[j]:
        a[j + 1] = a[j]
        j -= 1
        cnt += 1
    a[j + 1] = temp
'''
for i in xrange(N):
    print a[i]
'''

print cnt