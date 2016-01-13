#coding=utf-8
#Bike Racers

N,M,K = map(int, raw_input().strip().split())
Graph = [[0 for _ in xrange(M)] for _ in xrange(N) ]

people = []
bike = []
for i in xrange(N):
    x, y = map(int, raw_input().strip().split())
    people.append((x, y))
for i in xrange(M):
    x, y = map(int, raw_input().strip().split())
    bike.append((x, y))

#计算距离
for i in xrange(N):
    for j in xrange(M):
        Graph[i][j] = abs(people[i][0] - bike[j][0]) + abs(people[i][1] - bike[j][1])
#距离从小到大排序
for i in xrange(N):
    Graph[i].sort()
    #print Graph[i]

MinDis = [10**10]
usedx = [0 for _ in xrange(N)]
usedy = [0 for _ in xrange(M)]


def DFS(choiceK, curDis):
    if choiceK >= K:
        if curDis < MinDis[0]:
            MinDis[0] = curDis
        return
    if curDis > MinDis[0]:
        return
    for i in xrange(N):
        if usedx[i] == 1:
            continue
        for j in xrange(M):
            if usedy[j] == 1:
                continue
            usedx[i] = 1
            usedy[j] = 1
            if Graph[i][j] > curDis:
                DFS(choiceK + 1, Graph[i][j])
            else:
                DFS(choiceK + 1, curDis)
            usedx[i] = 0
            usedy[j] = 0
DFS(0, 0)
print MinDis[0] ** 2

