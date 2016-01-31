#coding=utf-8
#[Algo] Matrix Rotation

def getInfo( x, y, M, N, rotate ):
    minseg = min( x, M - x - 1, y, N - y - 1 )
    R = M - 2 * minseg
    C = N - 2 * minseg
    P = R * 2 + C * 2 - 4

    step = rotate % P

    if step == 0:
        return x, y
    
    #算出四个角的坐标
    lefttop_x = minseg
    lefttop_y = minseg

    leftbottom_x = M - minseg - 1
    leftbottom_y = minseg

    rightbottom_x = M - minseg - 1
    rightbottom_y = N - minseg - 1

    righttop_x = minseg
    righttop_y = N - minseg - 1

    for i in xrange(step):
        #最左边
        if y == lefttop_y and x >= lefttop_x and x < leftbottom_x:
            x += 1
            continue
        if x == leftbottom_x and y >= leftbottom_y and y < rightbottom_y:
            y += 1
            continue
        if y == rightbottom_y and x > righttop_x and x <= rightbottom_x:
            x -= 1
            continue
        if x == righttop_x and y > lefttop_y and y <= righttop_y:
            y -= 1
            continue

    return x, y
    
M,N,R = map(int, raw_input().strip().split(" "))

numlist = []
for i in xrange(M):
    numlist.append(list(map(int, raw_input().strip().split())))

changelist = [[i * j for j in xrange(N)] for i in xrange(M)]
for i in xrange(M):
    for j in xrange(N):
        #先计算旋转周期
        x , y = getInfo( i, j, M, N, R )
        changelist[x][y] = numlist[i][j]
        
for i in xrange(M):
    for j in xrange(N):
        print changelist[i][j],
    print ""

        
