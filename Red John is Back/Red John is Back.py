import math
T = input()

question = []
for _ in xrange(T):
    question.append(input())
    
Max = max(question)

DP = [0] * (Max + 1)
DP[1] = 1
DP[2] = 1
DP[3] = 1
DP[4] = 2
for i in xrange(5, Max + 1):
    DP[i] = DP[i - 1] + DP[i - 4]

#print DP
    
used = [0] * (DP[Max] + 1)

for i in xrange(3, int(math.sqrt(DP[Max] + 1) + 1), 2):
    if used[i] == 1:
        continue
    for j in xrange( i * i, DP[Max] + 1, i ):
        if j % i == 0:
            used[j] = 1
            
prime = [2]
for i in xrange(3, DP[Max] + 1, 2):
    if used[i] == 0:
        prime.append(i)

#print prime
            
            
answer = [0] * T
for j in xrange(T):
    if DP[question[j]] >= 2:
        answer[j] += 1

for i in xrange(3, DP[Max] + 1, 2):
    if used[i] == 0:
        for j in xrange(T):
            if DP[question[j]] >= i:
                answer[j] += 1
for i in xrange(T):
    print answer[i]
#print DP