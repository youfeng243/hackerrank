#coding=utf-8
N = input()

def mycmp( a, b ):
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    return a[0] - b[0]

order = []
for i in xrange(N):
    t,d = map(int, raw_input().strip().split())
    order.append((i + 1, t+d))

order.sort(cmp=mycmp)

for i in order:
    print i[0],
print ""

#print order

#print order
