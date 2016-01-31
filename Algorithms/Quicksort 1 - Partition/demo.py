N = input()
a = map(int, raw_input().strip().split())

key = a[0]
first = 0
last = N - 1

while first  < last:
    while first < last and a[last] >= key:
        last -= 1
    a[first] = a[last]
    
    for i in xrange(N):
        print a[i],
    print ""
    
    while first < last and a[first] <= key:
        first += 1
    a[last] = a[first]
    
    for i in xrange(N):
        print a[i],
    print ""
    
a[first] = key
for i in xrange(N):
    print a[i],
print ""