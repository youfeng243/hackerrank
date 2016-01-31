T = input()

def findMax( A, start, end ):
    Max = -1
    index = -1
    for i in xrange(start, end + 1):
        if A[i] > Max:
            Max = A[i]
            index = i
    return index

for _ in xrange(T):
    N = input()
    a = map(int, raw_input().strip().split())
    
    stock = 0
    j = 0
    index = 0
    while j < N:
        index = findMax(a, j, N - 1)
        if index == j:
            j += 1
            continue
        cost = 0
        cnt = 0
        for i in xrange(j, index):
            cost += a[i]
            cnt += 1
        stock += a[index] * cnt - cost
        j = index + 1
    print stock