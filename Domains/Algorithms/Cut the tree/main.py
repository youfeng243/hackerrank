#coding=utf-8
#Cut the tree

N = input()
weight = map(int, raw_input().strip().split())
sumw = [0 for i in xrange(N + 1)]
used = [0 for i in xrange(N + 1)]
dic = {}
for i in xrange(N - 1):
    x, y = map(int, raw_input().strip().split())
    if x in dic:
        dic[x].append(y)
    else:
        dic[x] = [y]
    if y in dic:
        dic[y].append(x)
    else:
        dic[y] = [x]



def DFS( i, N ):
    if i > N:
        return 0
    
    sumw[i] = weight[i - 1]

    if i not in dic:
        return sumw[i]
    
    for j in dic[i]:
        if used[j] == 1:
            continue
        used[j] = 1
        sumw[i] += DFS(j, N)
    return sumw[i]

used[1] = 1
DFS(1, N)
Min = 10**9

#print sumw

for i in xrange(2, N + 1):
    temp = abs(sumw[1] - 2 * sumw[i])
    if temp < Min:
        Min = temp
print Min


