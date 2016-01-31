#coding=utf-8
import os

def mycmp( a, b ):
    return a[2] - b[2]

def getFileInfo():
    if os.path.exists(r"./test.txt") == False:
        return False,[]
    #读取文件的地图
    Graph = []
    for line in open(r"./test.txt"):
        Graph.append(list(line.strip()))

    #print Graph
    return True,Graph

def SaveFile( board ):
    File = file(r"test.txt", "w+")
    for line in board:
        File.writelines("".join(line) + "\n")
    File.close()

def CombGraph( oriboard, fileboard ):
    
    for i in xrange(5):
        for j in xrange(5):
            if fileboard[i][j] == 'b':
                oriboard[i][j] = '-'
            elif fileboard[i][j] == '-':  
                oriboard[i][j] = '-'
            elif fileboard[i][j] == 'd':
                oriboard[i][j] = 'd'
    return oriboard

def DefaultSearch(startx, starty, board):

    dirty = []
    blind = []
    for i in xrange(5):
        for j in xrange(5):
            if board[i][j] == 'd':
                dirty.append((i, j, abs(i - startx) + abs(j - starty)))
            if board[i][j] == 'o':
                blind.append((i, j, abs(i - startx) + abs(j - starty)))
    dirty.sort(cmp=mycmp)
    blind.sort(cmp=mycmp)

    board[startx][starty] = '-'
    
    if len(dirty) != 0:
        endx = dirty[0][0]
        endy = dirty[0][1]
        if startx == endx and starty == endy:
            print "CLEAN"
            return board
        if startx == endx:
            if starty > endy:
                starty -= 1
                print "LEFT"
            elif starty < endy:
                starty += 1
                print "RIGHT"
        else:
            if startx > endx:
                startx -= 1
                print "UP"
            elif startx < endx:
                startx += 1
                print "DOWN"
        return board
    endx = blind[0][0]
    endy = blind[0][1]
    if startx == endx:
        if starty > endy:
            starty -= 1
            print "LEFT"
        elif starty < endy:
            starty += 1
            print "RIGHT"
    else:
        if startx > endx:
            startx -= 1
            print "UP"
        elif startx < endx:
            startx += 1
            print "DOWN"
    return board
    
def next_move(posr, posc, board):

    FileExist,Fileboard = getFileInfo()
    
    #如果文件不存在则按默认方式搜索
    if FileExist == False:
        newboard = DefaultSearch( posr, posc, board )
    else:#合成新地图
        newboard = CombGraph(board, Fileboard)
        DefaultSearch( posr, posc, newboard )
    #保存新地图
    SaveFile(newboard)

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
