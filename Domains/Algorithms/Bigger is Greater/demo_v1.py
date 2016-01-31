from itertools import permutations



N = input()
for _ in xrange(N):
    string = list(raw_input())
    
    p = permutations(string)
    
    print "".join(p.next())
    print "".join(p.next())
    