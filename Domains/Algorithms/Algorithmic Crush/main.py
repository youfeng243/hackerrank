#Algorithmic Crush
N,M = map(int, raw_input().strip().split())
mlist = []
for i in xrange(M):
    start, end, k = map(int, raw_input().strip().split())
    mlist.append([start, end, k])

#print mlist
mlist.sort(lambda a,b:a[1] - b[1])
#print mlist


tmp = mlist[0][2]
tmpStart = mlist[0][0]
tmpEnd = mlist[0][1]

Max = tmp
MaxStart = tmpStart
MaxEnd = tmpEnd


for i in xrange(1, M):
    if mlist[i][0] > tmpEnd:
        tmp = mlist[i][2]
        tmpStart = mlist[i][0]
        tmpEnd = mlist[i][1]
        continue
    if mlist[i][1] <= tmpEnd:
        tmp += mlist[i][0]
        tmpEnd = 
