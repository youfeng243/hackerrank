N = input()
a = map(int, raw_input().strip().split())
b = [0 for _ in xrange(N)]

j = 0
for i in xrange(1, N ):
    if a[i] < a[0]:
        b[j] = a[i]
        j += 1
b[j] = a[0]
j += 1
for i in xrange(1, N):
    if a[i] >= a[0]:
        b[j] = a[i]
        j += 1

for i in xrange(N):
    print b[i],
print ""