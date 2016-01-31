#coding=utf-8
#Almost Sorted
N = input()
A = map(int, raw_input().strip().split())
B = A[:]
A.sort()
leftindex = -1
rightindex = -1
count = 0
for i in xrange(N):
    if A[i] == B[i]:
        continue
    count += 1
    if leftindex == -1:
        leftindex = i
        continue
    rightindex = i
if count <= 0:
    print "yes"
else:
    if count <= 2:
        print "yes"
        print "swap %d %d" %(leftindex + 1, rightindex + 1)
    else:
        judgeflag = True
        for i in xrange(leftindex, rightindex + 1):
            if A[i] == B[rightindex - (i - leftindex)]:
                continue
            judgeflag = False
            break
        if judgeflag == True:
            print "yes"
            print "reverse %d %d" % (leftindex + 1, rightindex + 1)
        else:
            print "no"
