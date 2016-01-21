#coding=utf-8
#Candies

def getDP( i ):
    if i >= N or i < 0:
        return 0
    if DP[i] != 0:
        return DP[i]
    
    #默认前面比当前大 只要跟后面的进行比较
    
    if i + 1 < N:
        if C[i] > C[i + 1]:
            DP[i] = getDP(i + 1) + 1
        else:
            DP[i] = 1
    else:
        DP[i] = 1
            
    return DP[i]
    
    
global N
global C
N = input()
C = []
for i in xrange(N):
    C.append(input())

if N <= 1:
    print 1
    
else:
    DP = [0] * N
    for i in xrange(N):
        if DP[i] != 0:
            continue
        if i == 0:
            if C[i] <= C[i + 1]:
                DP[i] = 1
            else:
                DP[i] = getDP(i + 1) + 1
            continue
        
        if i + 1 >= N:
            if C[i] > C[i - 1]:
                DP[i] = DP[i - 1] + 1
            else:
                DP[i] = 1
            continue
        
        if C[i] > C[i - 1]:
            if C[i] > C[i + 1]:
                DP[i] = max(DP[i - 1], getDP(i + 1)) + 1
            elif C[i] == C[i + 1]:
                DP[i] = DP[i - 1] + 1
            elif C[i] < C[i + 1] :
                DP[i] = DP[i - 1] + 1
            continue
        
        if C[i] == C[i - 1]:
            if C[i] > C[i + 1]:
                DP[i] = getDP(i + 1) + 1
            else:
                DP[i] = 1
            continue
            
        if C[i] < C[i - 1]:
            if C[i] > C[i + 1]:
                C[i] = getDP(i + 1) + 1
            elif C[i] == C[i + 1]:
                C[i] = 1
            elif C[i] < C[i + 1] :
                C[i] = 1
        
    print sum(DP)