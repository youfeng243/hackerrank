T = input()
for t0 in xrange(T):
    N = input()
    A = map(int, raw_input().strip().split())

    LeftSum = [0 for i in xrange(N)]
    RightSum = [0 for i in xrange(N)]

    LeftSum[0] = A[0]
    RightSum[-1] = A[-1]

    for i in xrange(1, N):
        LeftSum[i] = LeftSum[i - 1] + A[i]
        RightSum[-i - 1] = RightSum[-i] + A[N - i - 1]

    if N == 1:
        print "YES"
    else:
        IsTrue = False
        for i in xrange(N):
            if i == 0:
                if RightSum[i + 1] == 0:
                    IsTrue = True
                    break
                continue
            if i == N - 1:
                if LeftSum[i - 1] == 0:
                    IsTrue = True
                    break
                continue
            if RightSum[i + 1] == LeftSum[i - 1]:
                IsTrue = True
                break
        if IsTrue == True:
            print "YES"
        else:
            print "NO"
