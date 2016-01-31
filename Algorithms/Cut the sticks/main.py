n = int(raw_input())
arr = map(int,raw_input().strip().split(" "))

arr.sort()
length = len(arr)
minarr = arr[0]
i = 0
while i < length:
    print length - i
    while i < length and minarr == arr[i]:
        i += 1
    if i >= length:
        break
    minarr = arr[i]
