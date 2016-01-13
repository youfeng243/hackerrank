def mycmp( a, b ):
    return a[2] - b[2]
def next_move(startx, starty, dimh, dimw, board):

    dirty = []
    for i in xrange(dimh):
        for j in xrange(dimw):
            if board[i][j] == 'd':
                dirty.append((i, j, abs(i - startx) + abs(j - starty)))
    dirty.sort(cmp=mycmp)

    endx = dirty[0][0]
    endy = dirty[0][1]

    if startx == endx and starty == endy:
        print "CLEAN"
        return
    
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
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
