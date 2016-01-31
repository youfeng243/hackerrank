N = input()
count = [0 for i in xrange(100)]
A = [[] for i in xrange(100)]

for i in xrange(N):
    text = raw_input().strip().split()
    index = int(text[0])
    count[index] += 1
    A[index].append( (i, text[1]) )

for i in xrange( 100 ):
    for j in xrange( count[i] ):
        if A[i][j][0] < N / 2:
            print "-",
        else:
            print A[i][j][1],

