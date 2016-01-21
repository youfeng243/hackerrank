N = input()
C = []
for i in xrange(N):
    C.append(input())

C.append(C[N - 1])
C.insert(0, C[0])

DP = [0] * (N + 2)
DP[0] = 1
DP[N + 1] = 1

while True:
    scanFlag = True
    for i in xrange(1, N + 1):
        
        if DP[i] != 0:
            continue
            
        if C[i] <= C[i - 1]:
            if C[i] <= C[i + 1]:
                DP[i] = 1
            else:
                if DP[i + 1] != 0:
                    DP[i] = DP[i + 1] + 1
            
        if C[i] > C[i - 1]:
            if C[i] <= C[i + 1]:
                if DP[i - 1] != 0:
                    DP[i] = DP[i - 1] + 1
            else:
                if DP[i - 1] != 0 and DP[i + 1] != 0:
                    DP[i] = max(DP[i - 1], DP[i + 1]) + 1
                    
        if DP[i] == 0:
            scanFlag = False
            
    if scanFlag == True:
        break

print sum(DP[1:N + 1])