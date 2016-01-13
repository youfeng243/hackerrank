#coding=utf-8
T = input()
for t0 in xrange(T):
    N = input()
    G = []
    for i in xrange(N):
        text = list(raw_input().strip())
        text.sort()
        G.append(text)
    answer = True
    for i in xrange(N):
        for j in xrange(1, N):
            if G[j][i] < G[j - 1][i]:
                answer = False
                break
        if answer == False:
            break
    if answer == True:
        print "YES"
    else:
        print "NO"
    
    
    #print G
