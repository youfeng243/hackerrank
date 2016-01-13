#coding=utf-8
N = input()

A = map(int, raw_input().strip().split())
P,Q = map(int, raw_input().strip().split())

A.sort()

MaxLen = 0
MaxPoint = 0
#先判断端点
tempMin = 10**10
for i in xrange(N):
    tempMin = min(tempMin, abs(P - A[i]))

Maxlen = tempMin
MaxPoint = P

tempMin = 10**10
for i in xrange(N):
    tempMin = min(tempMin, abs(Q - A[i]))

if Maxlen < tempMin:
    Maxlen = tempMin
    MaxPoint = Q

for i in xrange(1, N):
    temp = (A[i - 1] + A[i]) / 2
    if temp >= P and temp <= Q:
        mintemp = min(abs(A[i - 1] - temp), abs(A[i] - temp))
        if mintemp > Maxlen:
            Maxlen = mintemp
            MaxPoint = temp
        elif mintemp == Maxlen:
            if temp < MaxPoint:
                MaxPoint = temp
print MaxPoint


'''
if Q <= A[0]:
    print P
elif P >= A[-1]:
    print Q
elif N == 1:  #当只有一个数时
    if abs(Q - A[0]) > abs(P - A[0]):
        print Q
    else:
        print P
else:
    Maxlen = 0
    Maxpoint = 0
    if P <= A[0] and Q >= A[0]:
'''
        
    
            
