T = input()

for _ in xrange(T):
    N = input()
    A = map(int, raw_input().strip().split())
    
    stepcnt = 0
    difftotal = 0
    
    A.sort()
    for i in xrange(1, N):
        A[i] += difftotal
        if A[i] == A[i - 1]:
            continue
            
        diff = A[i] - A[i - 1]
        difftotal += diff
        
        stepcnt += diff / 5
        diff %= 5
        stepcnt += diff / 2
        stepcnt += diff % 2
        
        #print A[i:]
        
    print stepcnt
        