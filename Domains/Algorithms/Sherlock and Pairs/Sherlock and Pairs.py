#coding=utf-8
T = input()

for _ in xrange(T):
    dic = {}
    N = input()
    A = map(int, raw_input().strip().split())
    for i in xrange(N):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    Sum = 0
    for i in dic:
        if dic[i] > 1:
            Sum += dic[i] * ( dic[i] - 1 )
    print Sum