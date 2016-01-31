#Count Luck

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def DFS( plat, used, startx, starty, K, turn, IsFind, N, M ):
    if IsFind == True:
        return
    if plat[startx][starty] == '*':
        IsFind = True
        if K == turn:
            print "Impressed"
        else:
            print "Oops!"
        #print turn
        return
    turnlist = []
    for i in dirs:
        x = startx + i[0]
        y = starty + i[1]
        if x < 0 or y < 0 or x >= N or y >= M:
            continue
        if used[x][y] == 1 or plat[x][y] == 'X':
            continue
        turnlist.append((x, y))
    turntimes = len(turnlist)
    #print "turntimes = %d" % turntimes 
    for i in xrange(turntimes):
        x,y = turnlist[i]
        used[x][y] = 1
        if turntimes >= 2:
            DFS(plat, used, x, y, K, turn + 1, IsFind, N, M)
        else:
            DFS(plat, used, x, y, K, turn, IsFind, N, M)
        used[x][y] = 0
    

T = input()
for _ in xrange(T):
    N,M = map(int, raw_input().strip().split())
    plat = []
    used = [[0 for i in xrange(M)] for j in xrange(N)]
    startx = 0
    starty = 0
    for i in xrange(N):
        temp = raw_input().strip()
        plat.append(temp)
        tempy = temp.find('M')
        if tempy != -1:
            startx = i
            starty = tempy
            #print startx, starty
    K = input()
    IsFind = False
    used[startx][starty] = 1
    DFS( plat, used, startx, starty, K, 0, IsFind, N, M )
