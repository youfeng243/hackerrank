#2D-Arrays + More Review!

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

MaxNum = -100000
for i in xrange(1, 5):
    for j in xrange(1, 5):
        temp = arr[i][j] + arr[i - 1][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 1][j - 1] + arr[i - 1][j + 1] + arr[i - 1][j - 1]
        if temp > MaxNum:
            MaxNum = temp

print MaxNum
