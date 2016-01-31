#Missing Numbers
N = input()
A = map(int, raw_input().strip().split())
M = input()
B = map(int, raw_input().strip().split())
numset = set([])
A.sort()
B.sort()
i = 0
j = 0
while i < N and j < M:
    if A[i] == B[j]:
        i += 1
        j += 1
    else:
        numset.add(B[j])
        j += 1
while j < M:
    numset.add(B[j])
    j += 1

numlist = list(numset)
numlist.sort()

for i in xrange(len(numlist)):
    print numlist[i],
print ""
        
