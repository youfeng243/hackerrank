#coding=utf-8
#The Full Counting Sort
#from collections import deque

N = input()
A = []
dic = {}
rankstr = [ "" for _ in xrange(N) ]
count = [0 for _ in xrange(100)]

for i in xrange(N):
    text = raw_input().strip().split()
    if i < N / 2:
        text[1] = "-"
    index = int(text[0])
    A.append([index, text[1]])
    count[index] += 1
    if index in dic:
        dic[index].append(text[1])
    else:
        dic[index] = [text[1]]

for i in xrange(1, 100):
    count[i] += count[i - 1]
        
for i in xrange(N):
    count[A[i][0]] -= 1
    rankstr[count[A[i][0]]] = dic[A[i][0]].pop()
for i in xrange(N):
    print rankstr[i],
print ""
    