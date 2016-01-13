#BotClean
startx, starty = map(int, raw_input().strip().split())
dirty = []
for i in xrange(5):
    text = raw_input().strip()
    for j in xrange(5):
        if text[j] == "d":
            x = i
            y = j
            dis = abs(startx - x) + abs(starty - y)
            dirty.append((x, y, dis))

def mycmp(a, b):
    return a[2] - b[2]
dirty.sort(cmp = mycmp)

#print dirty
if dirty[0][2] == 0:
    print "CLEAN"
else:

    endx = dirty[0][0]
    endy = dirty[0][1]
    
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
