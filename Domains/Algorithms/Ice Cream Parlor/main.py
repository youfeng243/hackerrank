#Ice Cream Parlor
T = input()
for _ in xrange(T):
    M = input()
    N = input()
    c = map(int, raw_input().strip().split())
    C = [(c[i], i + 1) for i in xrange(N)]
    #print C
    C.sort(lambda x, y: x[0] - y[0])
    #print C

    answer1 = 0
    answer2 = 0
    IsFind = False
    
    for i in xrange(N):
        answer1 = C[i][1]
        c1 = C[i][0]
        c2 = M - c1
        first = i + 1
        end = N - 1
        while first <= end:
            mid = (first + end) / 2
            if C[mid][0] == c2:
                answer2 = C[mid][1]
                IsFind = True
                break
            elif C[mid][0] > c2:
                end = mid - 1
            else:
                first = mid + 1
        if IsFind == True:
            break
    print min(answer1, answer2), max(answer1, answer2)
