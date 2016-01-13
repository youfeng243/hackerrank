#Two Strings
T = input()
for t0 in xrange(T):
    A = set(raw_input().strip())
    B = set(raw_input().strip())

    if len(A & B) > 0:
        print "YES"
    else:
        print "NO"
