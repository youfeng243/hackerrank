#coding=utf-8
import os



def mycmp( a, b ):
    return a[2] - b[2]

def loadMemory():
    #读取地图
    if os.path.exists(r"./map.txt") == False:
        return [["?" for _ in xrange(200)] for _ in xrange(200)], False
    filehandle = open(r"./map.txt")

    bigmap = []
    for line in filehandle:
        bigmap.append(list(line.strip()))
    filehandle.close()

    return bigmap, True

def saveMemory( bigmap ):
    filehandle = open(r"./map.txt", "w")

    for line in xrange(200):
        filehandle.writelines("".join(bigmap[line]) + "\n")
    
    filehandle.close()

def defaultInit( graph, bigmap ):
    for i in xrange(200):
        for j in xrange(200):
            if i >= 98 and i <= 100 and j >= 98 and j <= 100:
                bigmap[i][j] = graph[i - 98][j - 98]
            else:
                bigmap[i][j] = '?'    

def FindRobot( bigmap ):
    for i in xrange(200):
        for j in xrange(200):
            if bigmap[i][j] == 'R':
                bigmap[i][j] = '-'
                return i, j
    return 0, 0
                
def combMap( graph, bigmap, isNew ):
    startx = 99
    starty = 99
    
    if isNew == False:
        defaultInit(graph, bigmap)
        return startx, starty
    
    startx, starty = FindRobot(bigmap)
    
    for i in xrange( startx - 1, startx + 2 ):
        for j in xrange( starty - 1, starty + 2 ):
            bigmap[i][j] = graph[i - (startx - 1)][j - (starty - 1)]
    
    return startx, starty

def FindDest( startx, starty, bigmap ):
    ex = -1
    ey = -1
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in xrange(200):
        for j in xrange(200):
            if bigmap[i][j] == 'e':
                ex = i
                ey = j
                break
    if ex != -1 and ey != -1:
        return ex, ey
    dest = []
    for i in xrange(200):
        for j in xrange(200):
            if bigmap[i][j] == '?':
                accord = False
                for k in dirs:
                    tempx = k[0] + i
                    tempy = k[1] + j
                    if tempx < 0 or tempy < 0 or tempx >= 200 or tempy >= 200:
                        continue
                    if bigmap[tempx][tempy] == '-':  #选取能走的地方进行排序
                        accord = True
                        break
                if accord == True:
                    dis = abs(startx - i) + abs(starty - j)
                    dest.append((i, j, dis))
    dest.sort(cmp=mycmp)
    
    ex = dest[0][0]
    ey = dest[0][1]
    return ex, ey
    
def GetDest( startx, starty, destx, desty ):
    
    dirs = "DOWN"
    therex = 0
    therey = 0
    if startx == destx:
        therex = startx
        if desty > starty:
            therey = starty + 1
            dirs = "RIGHT"
        else:
            therey = starty - 1
            dirs = "LEFT"
    else:
        therey = starty
        if startx > destx:
            therex = startx - 1
            dirs = "UP"
        else:
            therex = startx + 1
            dirs = "DOWN"
    return therex, therey, dirs

def DownMap( bigmap ):
    temp = [['?' for i in xrange(200)] for j in xrange(200)]
    
    for i in xrange( 200 ):
        for j in xrange( 200 ):
            temp[i][j] = bigmap[199 - i][199 - j]
    
    return temp

def RightMap( bigmap ):
    temp = [['?' for i in xrange(200)] for j in xrange(200)]
    
    for i in xrange( 200 ):
        for j in xrange( 200 ):
            temp[i][j] = bigmap[j][199 - i]
    return temp

def LeftMap( bigmap ):
    temp = [['?' for i in xrange(200)] for j in xrange(200)]
    
    for i in xrange( 200 ):
        for j in xrange( 200 ):
            temp[i][j] = bigmap[199 - j][i]
    
    
def RotateMap( therex, therey, dirs, bigmap ):
    bigmap[therex][therey] = 'R'
    
    if dirs == "DOWN":
        DownMap(bigmap)
    elif dirs == "RIGHT":
        RightMap(bigmap)
    elif dirs == "LEFT":
        LeftMap(bigmap)
    
def Search( startx, starty, bigmap ):
    
    #这个是记录走到的位置的
    therex = 0
    therey = 0
    
    #找到可以走的目标
    destx, desty = FindDest(startx, starty, bigmap)
    
    therex, therey, dirs = GetDest( startx, starty, destx, desty )
    
    #旋转地图
    RotateMap( therex, therey, dirs, bigmap )
    
    print dirs
    
def solve(graph):
    #读取缓存文件 获得地图以及保存的移动指令
    bigmap, isNew = loadMemory()
    
    #合成最新地图
    startx, starty = combMap(graph, bigmap, isNew)
	
    #搜索
    Search( startx, starty, bigmap )
	
    #保存信息
    saveMemory(bigmap)

def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))    
    solve(graph)
    
if __name__ == "__main__":
    main()
