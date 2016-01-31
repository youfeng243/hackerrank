#coding=utf-8

def BinarySearch( first, last, DP, num ):
   
    while first <= last:
        mid = int(( first + last ) / 2)
        
        if num > DP[mid] and num <= DP[mid + 1]:
            return mid
        if num > DP[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1

N = input()
A = []
for _ in xrange(N):
    A.append(input())
    
len = 1
DP = [0] * N
DP[0] = A[0]

for i in xrange(1, N):
    if A[i] > DP[len - 1]:
        DP[len] = A[i]
        len += 1
    else:
        index = BinarySearch( 0, len - 1, DP, A[i] )
        DP[index + 1] = A[i]
print DP
print len