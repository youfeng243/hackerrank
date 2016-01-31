#Cutting Boards
#coding:utf-8
T = input()

for t0 in xrange(T):
    m,n = map(int, raw_input().strip().split())
    Y = map(int, raw_input().strip().split())
    X = map(int, raw_input().strip().split())
    
    Y.sort()
    X.sort()
    Y.reverse()
    X.reverse()
    
    
    i = 0
    j = 0

    Cost = 0
    while i < m - 1 and j < n - 1:
        if Y[i] > X[j]:
            Cost += Y[i] * (j + 1)
            i += 1
        else:#增加的都一样，选切割哪边都是一样的结果
            Cost += X[j] * (i + 1)
            j += 1

    while i < m - 1:
        Cost += Y[i] * n
        i += 1
    while j < n - 1:
        Cost += X[j] * m
        j += 1
    
    print Cost % (10**9 + 7)
