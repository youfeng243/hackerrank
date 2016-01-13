#Largest Permutation
N,K = map(int, raw_input().strip().split())
array = map(int, raw_input().strip().split())

if K >= N:
    for i in xrange(N):
        print N - i,
    print ""
else:
    dic = {}
    for i in xrange(N):
        dic[array[i]] = i
    i = 0
    j = 0
    while i < K and j < N:
        if array[j] == N - j:
            j += 1
            continue
        tempValue = array[j]
        array[dic[N - j]], array[j] = array[j], array[dic[N - j]]
        tempIndex = dic[N - j]
        dic[N - j] = j
        dic[tempValue] = tempIndex
        i += 1
    for t in xrange(N):
        print array[t],
    print ""

'''
if K >= N:
    array.sort()
    array.reverse()
else:
    temp = array[:]
    temp.sort()
    temp.reverse()
    i = 0
    j = 0
    while i < K and j < N:
        if array[j] == temp[j]:
            j += 1
            continue
        Max = array[j]
        position = j
        for k in xrange(j, N):
            if Max < array[k]:
                Max = array[k]
                position = k
                if Max == temp[j]:
                    break
        array[j], array[position] = array[position], array[j]
        i += 1
for t in xrange(N):
    print array[t],
print ""
'''
