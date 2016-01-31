N,M = map(int, raw_input().strip().split())
A = map(int, raw_input().strip().split())
B = map(int, raw_input().strip().split())

DP = [[0 for i in xrange(M + 1)] for j in xrange(N + 1)]

answer = []

for i in xrange(1, N + 1):
    for j in xrange(1, M + 1):
        if A[i - 1] == B[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

i = N
j = M
while i >= 1 and j >= 1:
    if DP[i][j] == DP[i - 1][j - 1] + 1 and A[i - 1] == B[j - 1]:
        answer.append(A[i - 1])
        i -= 1
        j -= 1
    elif DP[i][j] == DP[i - 1][j]:
        i -= 1
    elif DP[i][j] == DP[i][j - 1]:
        j -= 1
        
length = len(answer)
for i in xrange(length):
    print answer[length - i - 1],
