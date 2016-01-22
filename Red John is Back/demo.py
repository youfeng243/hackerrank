import math

DP = [0] * 41
DP[1] = 1
DP[2] = 1
DP[3] = 1
DP[4] = 2
for i in xrange(5, 41):
    DP[i] = DP[i - 1] + DP[i - 4]
    
used = [0] * (DP[40] + 1)
for i in xrange(3, int(math.sqrt(DP[40]) + 1), 2):
    for j in xrange( i * i, DP[40] + 1, i ):
        used[j] = 1
        
        
answer = [0] * 41

for i in xrange(1, 41):
    if DP[i] >= 2:
        answer[i] += 1
        
for i in xrange( 3, DP[40] + 1, 2 ):
    if used[i] == 0:
        for j in xrange( 1, 41 ):
            if DP[j] >= i:
                answer[j] += 1
print answer



'''
[0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 6, 8, 9, 11, 15, 19, 24, 32, 42, 53, 68, 91, 119, 155,
 462, 615, 816, 1077, 1432, 1912, 2543, 3385, 4522, 6048, 8078, 10794, 14475, 19385]
 '''