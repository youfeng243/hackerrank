T = input()
for _ in xrange(T):
    n = input()
    array = map(int, raw_input().strip().split())
    
    Max = 0
    MaxSub = 0
    temp = 0
    for i in xrange(n):
        if array[i] > 0:
            Max += array[i]
        if temp + array[i] > 0:
            temp += array[i]
        else:
            temp = 0
        if temp > MaxSub:
            MaxSub = temp
    if MaxSub == 0:
        MaxSub = max(array)
        Max = MaxSub
    print MaxSub, Max