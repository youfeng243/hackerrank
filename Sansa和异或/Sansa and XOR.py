T = input()
for _ in xrange(T):
    N = input()
    a = map(int, raw_input().strip().split())

    if N % 2 == 0:
        print 0
    else:
        Sum = a[0]
        for i in xrange(1, N):
            if i % 2 == 1:
                continue
            Sum ^= a[i]
        print Sum