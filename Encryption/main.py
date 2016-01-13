#coding=utf-8
#Encryption

from __future__ import print_function
import math

s = raw_input().strip()
length = len(s)
start = int(math.floor(math.sqrt(length)))
end = int(math.ceil(math.sqrt(length)))
#print start,end

minnum = 1000000
r = 0
c = 0
for i in xrange(start, end + 1):
    for j in xrange(i, end + 1):
        if i * j < length:
            continue
        if i * j < minnum:
            minnum = i * j
            r = i
            c = j
for i in xrange(c):
    for j in xrange(r):
        if j * c + i >= length:
            continue
        print(s[j * c + i], sep="", end="")
    print ("", sep="", end=" ")
print("")

