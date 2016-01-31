N,K = map(int, raw_input().strip().split())
binary = map(int, list(raw_input().strip()))
answer = [0 for i in xrange(N)]

temp = 0
for i in xrange(N):
    answer[i] = temp ^ binary[i]
    temp ^= answer[i]
    if i >= K - 1:
        temp ^= answer[i - K + 1]
print "".join([str(answer[i]) for i in xrange(N)])