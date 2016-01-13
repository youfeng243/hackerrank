#Two arrays
T = input()
for t0 in xrange(T):
    
    N,K = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())
    A.sort()
    B.sort()
    B.reverse()

    M = N
    answer = True
    for i in xrange(N):
        j = 0
        while j < M:
            if A[i] + B[j] < K:
                break
            j += 1
        if j == 0:
            answer = False
            break
        B.remove(B[j - 1])
        M -= 1
        
    if answer == True:
        print "YES"
    else:
        print "NO"
            
    



#print A
#print B
