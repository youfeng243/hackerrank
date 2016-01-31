#coding=utf-8
import sys

def solve( startx, starty, R, C, G, P ):
    for i in xrange(R):
        for j in xrange(C):
            if G[startx + i][starty + j] != P[i][j]:
                return False
    return True

t = int(raw_input().strip())
for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    FindFlag = False
    for i in xrange(R - r + 1):
        for j in xrange(C - c + 1):
            if solve( i, j, r, c, G, P ) == True:
                FindFlag = True
                break
        if FindFlag == True:
            break
        
    if FindFlag == True:
        print "YES"
    else:
        print "NO"
