#coding=utf-8
N = input()
A = map(int, raw_input().strip().split())
A.sort()
dic = {}
Min = 10 ** 9
for i in xrange(1, N):
    if abs(A[i] - A[i - 1]) <= Min:
        Min = abs(A[i] - A[i - 1])
        if Min in dic:
            dic[Min].append((A[i - 1], A[i]))
        else:
            dic[Min] = [(A[i - 1], A[i])]
for i in xrange(len(dic[Min])):
    print dic[Min][i][0], dic[Min][i][1],