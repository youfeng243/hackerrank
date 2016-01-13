#coding=utf-8
import os
from collections import deque

def FindDoor( bigmap ):
    for i in xrange(200):
        for j in xrange(200):
            if bigmap[i][j] == 'e':
                return True
    return False

def PrintResult( startx, starty, findx, findy ):
    if findx == startx:
        if findy > starty:
            print "RIGHT"
        elif findy < starty:
            print "LEFT"
        else:
            print "ERROR!!!"
    elif findy == starty:
        if findx > startx:
            print "DOWN"
        elif findx < startx:
            print "UP"
        else:
            print "ERROR!!!"
    return

	
def BFS( startx, starty, bigmap, preinfo ):
	
    #如果还有路径没有走完
    if len(preinfo) > 0:
        PrintResult(startx, starty, preinfo[0][0], preinfo[0][1])
        return

    #移动的方向
    side = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    #访问路径标记
    parent = [[[-1, -1] for i in xrange(200)] for j in xrange(200)]
    
    #访问过标记
    used = [[0 for i in xrange(200)]for j in xrange(200)]

    #起始点标记已经访问
    used[startx][starty] = 1

    #遍历队列
    queue = deque([])

    #添加首个位置
    queue.append((startx, starty))
	
    eaddress = FindDoor( bigmap )
    findx = -1
    findy = -1
    while len(queue) > 0:
        tempx, tempy = queue.popleft()
        if eaddress == True:
            if bigmap[tempx][tempy] == "e":
                findx = tempx
                findy = tempy
                break
        else:
            if bigmap[tempx][tempy] == '?':
                findx = tempx
                findy = tempy
                break
        for i in side:
            willx = tempx + i[0]
            willy = tempy + i[1]
            if willx < 0 or willx >= 200 or willy < 0 or willy >= 200:
                continue
            if bigmap[willx][willy] == '#':
                continue
            if used[willx][willy] == 1:
                continue
            used[willx][willy] = 1
            parent[willx][willy][0] = tempx
            parent[willx][willy][1] = tempy
            queue.append((willx, willy))
    if findx == -1 and findy == -1:
        print "ERROR!!!!!!!!!"
        return

    while True:
        preinfo.append((findx, findy))
        if parent[findx][findy][0] == startx and parent[findx][findy][1] == starty:
            break
        findx = parent[findx][findy][0]
        findy = parent[findx][findy][1]
    preinfo.reverse()
    PrintResult(startx, starty, preinfo[0][0], preinfo[0][1])
    return
	
def loadMemory():
    #读取地图
    if os.path.exists(r"./map.txt") == False or os.path.exists(r"do.txt") == False:
        return [["?" for _ in xrange(200)] for _ in xrange(200)], []
    filehandle = open(r"./map.txt")

    bigmap = []
    for line in filehandle:
        bigmap.append(list(line.strip()))
    filehandle.close()

    #读取操作信息
    temp = []
    filehandle = open(r"./do.txt")
    for line in filehandle:
        x,y = map(int, line.strip().split())
        temp.append((x, y))

    filehandle.close()
    
    if len(temp) == 0:
        return [["?" for _ in xrange(200)] for _ in xrange(200)], []

    return bigmap, temp

def defaultInit( graph, bigmap ):
    for i in xrange(200):
        for j in xrange(200):
            if i >= 98 and i <= 100 and j >= 98 and j <= 100:
                bigmap[i][j] = graph[i - 98][j - 98]
            else:
                bigmap[i][j] = '?'

def combMap( graph, bigmap, preinfo ):
    if len(preinfo) < 1:
        defaultInit(graph, bigmap)
        return 99, 99

    centerx, centery = preinfo[0]
    for i in xrange( centerx - 1, centerx + 2 ):
        for j in xrange( centery - 1, centery + 2 ):
            bigmap[i][j] = graph[i - (centerx - 1)][j - (centery - 1)]
	
    del preinfo[0]
	
    return centerx, centery

def saveMemory( bigmap, preinfo ):
    filehandle = open(r"./map.txt", "w")

    for line in xrange(200):
        filehandle.writelines("".join(bigmap[line]) + "\n")
    
    filehandle.close()

    filehandle = open(r"./do.txt", "w")

    for line in preinfo:
        filehandle.writelines(str(line[0]) + " " + str(line[1]) + "\n")
    
    filehandle.close()

def solve(graph):
    #读取缓存文件 获得地图以及保存的移动指令
    bigmap, preinfo = loadMemory()
    
    #合成最新地图
    startx, starty = combMap(graph, bigmap, preinfo)
	
    #搜索
    BFS( startx, starty, bigmap, preinfo )
	
    #保存信息
    saveMemory(bigmap, preinfo)

def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))
    #print graph

    solve(graph)
    

if __name__ == "__main__":
    main()
