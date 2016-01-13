import math
n = input()
for i in xrange(n):
    A,B = map(int, raw_input().strip().split(" "))
    A = math.sqrt(A)
    B = math.sqrt(B)
    if A > int(A):
        A = int(A) + 1
    B = int(B)
    if B - A + 1 > 0:
        print B - A + 1
    else:
        print 0
