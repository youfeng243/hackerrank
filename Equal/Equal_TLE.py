T = input()

for _ in xrange(T):
    N = input()
    A = map(int, raw_input().strip().split())
    
    stepcnt = 0
    
    while True:
        MinNum = min(A)
        SecondNum = 10 ** 10
        index = -1
        for i in xrange(N):
            if A[i] < SecondNum and A[i] > MinNum:
                SecondNum = A[i]
                index = i
        if index == -1:
            break
        diff = SecondNum - MinNum
        for i in xrange(N):
            if i != index:
                A[i] += diff
        
        #count step
        stepcnt += diff / 5
        diff %= 5
        stepcnt += diff / 2
        stepcnt += diff % 2
        
    print stepcnt