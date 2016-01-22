T = input()

for _ in xrange(T):
    N = input()
    A = map(int, raw_input().strip().split())
    
    A.sort()
    
    step = 0
    for i in xrange( 1, N ):
        if A[i] == A[i - 1]:
            continue
        diff = A[i] - A[i - 1]
        
        print "diff = ", diff
        for j in xrange( 0, N ):
            if j != i:
                A[j] += diff
        step += diff / 5
        diff %= 5
        step += diff / 2
        step += diff % 2
        print A
    print step