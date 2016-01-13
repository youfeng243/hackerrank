#coding=utf-8
#Modified Kaprekar Numbers
p = int(raw_input().strip())
q = int(raw_input().strip())

cnt = False
for i in xrange(p, q + 1):
    if i == 1:
        print i,
        cnt = True 
        continue
    
    tempstr = str(i * i)
    length = len(tempstr)

    if length < 2:
        continue
    
    l = int(tempstr[:length / 2])
    r = int(tempstr[length / 2 : ])
    if l + r == i:
        print i,
        cnt = True
if cnt == False:
    print "INVALID RANGE",
print ""
    
