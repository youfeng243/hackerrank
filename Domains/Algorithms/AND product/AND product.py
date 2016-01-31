T = input()
for _ in xrange(T):
    A,B = map( int, raw_input().strip().split() )
    for i in xrange(A, B + 1):
        print bin(i)[2:]