#Mark and Toys
N,K = map(int, raw_input().strip().split())
toy = map(int, raw_input().strip().split())
toy.sort()

cnt = 0
for i in xrange(N):
    if K >= toy[i]:
        K -= toy[i]
        cnt += 1
print cnt
