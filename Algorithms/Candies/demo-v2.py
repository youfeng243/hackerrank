N = input()
C = []
for i in xrange(N):
    C.append(input())

C.append(C[N - 1])
C.insert(0, C[0])

DP = [0] * (N + 2)
DP[0] = 1
DP[N + 1] = 1

for i in xrange(1, N + 1):
    if C[i] > C[i - 1]:
        if C[i] > C[i + 1]:
            continue
        if DP[i - 1] != 0:
            DP[i] = DP[i - 1] + 1
            continue
    if C[i] <= C[i - 1]:
        if C[i] > C[i + 1]:
            continue
        DP[i] = 1
        
i = N 
while i >= 1:
    
    if C[i] > C[i + 1]:
        if C[i] > C[i - 1]:
            if DP[i - 1] != 0 and DP[i + 1] != 0:
                DP[i] = max(DP[i - 1], DP[i + 1]) + 1
                i -= 1
                continue
        else:
            if DP[i + 1] != 0:
                DP[i] = DP[i + 1] + 1
                i -= 1
                continue
    else:
        if C[i] > C[i - 1]:
            if DP[i - 1] != 0:
                DP[i] = DP[i - 1] + 1
                i -= 1
                continue
        else:
            DP[i] = 1
    i -= 1
    
print sum(DP[1:N + 1])