#Bot saves princess
#!/bin/python

dirs = {"UP":(-1, 0),"DOWN":(1, 0),"LEFT":(0, -1),"RIGHT":(0, 1)}


def DFS(startx, starty, n, grid, used, answer, tempanswer):
    if grid[startx][starty] == 'p':
        if len(answer) < len(tempanswer) or len(tempanswer) == 0:
            while len(tempanswer) > 0:
                tempanswer.pop()
            for i in answer:
                tempanswer.append(i)
        return
    for i in dirs:
        x = startx + dirs[i][0]
        y = starty + dirs[i][1]
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if used[x][y] == 1:
            continue
        used[x][y] = 1
        answer.append(i)
        DFS(x, y, n, grid, used, answer, tempanswer)
        used[x][y] = 0
        answer.pop()
    
def displayPathtoPrincess(n, grid, startx, starty):
    tempanswer = []
    answer = []
    used = [[0 for _ in xrange(n)] for _ in xrange(n)]
    used[startx][starty] = 1
    isFind = [False]
    DFS(startx, starty, n, grid, used, answer, tempanswer)
    for i in tempanswer:
        print i
    
    
#print all the moves here
m = input()

grid = []
startx = 0
starty = 0
endx = 0
endy = 0
for i in xrange(0, m):
    text = raw_input().strip()
    grid.append(text)
    indx = text.find("m")
    if indx != -1:
        startx = i
        starty = indx
    indx = text.find("p")
    if indx != -1:
        endx = i
        endy = indx
while startx != endx and starty != endy:
    if startx > endx:
        startx -= 1
        print "UP"
    elif startx < endx:
        startx += 1
        print "DOWN"
        
    if starty > endy:
        starty -= 1
        print "LEFT"
    elif starty < endy:
        starty += 1
        print "RIGHT"

#displayPathtoPrincess(m,grid, startx, starty)
