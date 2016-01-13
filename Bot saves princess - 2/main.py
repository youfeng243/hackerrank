#Bot saves princess - 2
m = input()
startx, starty = map(int, raw_input().strip().split())

grid = []

endx = 0
endy = 0
for i in xrange(0, m):
    text = raw_input().strip()
    grid.append(text)
    indx = text.find("p")
    if indx != -1:
        endx = i
        endy = indx

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

'''
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
'''
