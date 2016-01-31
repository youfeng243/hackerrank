from __future__ import print_function

N,K = map(int, raw_input().strip().split())
binary = map(int, list(raw_input().strip()))

length = N
prelength = K - 1

answer = []
start = 0
end = 0
dic = [0, 0]

for i in xrange( length ):
    
    if i == 0:
        answer.append(binary[i])
        dic[binary[i]] += 1
        if i >= K - 1:
            dic[answer[start]] -= 1
            start += 1        
        continue

    if dic[0] % 2 == 0 and dic[1] % 2 == 0:
        answer.append(binary[i])
        dic[binary[i]] += 1
        if i >= K - 1:
            dic[answer[start]] -= 1
            start += 1
        continue
        
    if dic[0] % 2 == 0 and dic[1] % 2 == 1:
        answer.append( binary[i] ^ 1 )
        dic[binary[i] ^ 1] += 1
        if i >= K - 1:
            dic[answer[start]] -= 1
            start += 1
        continue
        
    if dic[0] % 2 == 1 and dic[1] % 2 == 0:
        answer.append( binary[i] )
        dic[binary[i]] += 1
        if i >= K - 1:
            dic[answer[start]] -= 1
            start += 1
        continue
        
    if dic[0] % 2 == 1 and dic[1] % 2 == 1:
        answer.append( binary[i] ^ 1 )
        dic[binary[i] ^ 1] += 1
        if i >= K - 1:
            dic[answer[start]] -= 1
            start += 1
        continue
for i in xrange( length ):
    print( answer[i], sep="", end="" )
print ("")
    #print answer