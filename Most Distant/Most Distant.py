#coding=utf-8
import math


n = input()

MaxX = -10 ** 10
MinX = 10 ** 10
MaxY = -10 ** 10
MinY = 10 ** 10

for i in xrange(n):
    x, y = map(int, raw_input().strip().split())
    if x == 0:
        MaxY = max(MaxY, y)
        MinY = min(MinY, y)
    elif y == 0:
        MaxX = max(MaxX, x)
        MinX = min(MinX, x)


Max = 0

array = []
if MaxX != -10 ** 10:
    array.append((MaxX, 0))
if MaxY != -10 ** 10:
    array.append( (0, MaxY) )

if MinX != 10 ** 10:
    array.append((MinX, 0))
if MinY != 10 ** 10:
    array.append( (0, MinY) )


for i in xrange(len(array)):
    for j in xrange(i + 1, len(array)):
        dis = pow(array[i][0] - array[j][0], 2) + pow(array[i][1] - array[j][1], 2)
        Max = max(Max, math.sqrt(dis))
print "%.6lf" % Max
    
#print xarray
#print yarray