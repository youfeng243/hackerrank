#Maximise Sum
for _ in xrange(int(raw_input().strip())):
    N,M = map(int, raw_input().strip().split())
    Array = map(int, raw_input().strip().split())

    Max = 0
    for i in xrange(N):
        Sum = 0
        for j in xrange(i, N):
            Sum = (Sum + Array[j]) % M
            if Sum > Max:
                Max = Sum
    print Max
