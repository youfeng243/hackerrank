#coding=utf-8
global N
N = input()
a = map(int, raw_input().strip().split())

def quicksort( low, high, a):
    if low >= high:
        return
    
    key = a[high]
    j = low
    for i in xrange(low, high):
        if a[i] < key:
            a[j], a[i] = a[i], a[j]
            j += 1
    a[high], a[j] = a[j], a[high]
    
    for i in xrange(0, N):
        print a[i],
    print ""
    
    quicksort( low, j - 1, a)
    quicksort( j + 1, high, a)
    

quicksort(0, N - 1, a)