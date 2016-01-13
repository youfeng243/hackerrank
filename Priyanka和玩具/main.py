#coding=utf-8
N = input()
weight = map(int, raw_input().strip().split())
weight.sort()
cnt = 0
i = 0
while i < N:
    start = weight[i]
    end = start + 4
    while i < N:
        if weight[i] >= start and weight[i] <= end:
            i += 1
            continue
        break
    cnt += 1
print cnt
