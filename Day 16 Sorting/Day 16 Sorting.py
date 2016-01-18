N = input()
a = map(int, raw_input().strip().split())

a.sort()

answer = []
Min = 10 ** 10
for i in xrange(0, N - 1):
    Min = min(Min, abs(a[i] - a[i + 1]))
for i in xrange(0, N - 1):
    if abs(a[i] - a[i + 1]) == Min:
        answer.append((a[i], a[i + 1]))
for i in xrange(len(answer)):
    print answer[i][0], answer[i][1],
print ""