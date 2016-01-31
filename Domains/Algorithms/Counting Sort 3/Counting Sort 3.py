N = input()
count = [0 for i in xrange(100)]
for _ in xrange(N):
    count[int(raw_input().strip().split()[0])] += 1

for i in xrange(1, 100):
    count[i] += count[i - 1]
    
for i in xrange(100):
    print count[i],
print ""