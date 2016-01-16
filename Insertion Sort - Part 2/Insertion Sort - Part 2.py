#!/bin/python
def insertionSort(a, m):
    
    for i in xrange(1, m):
        if a[i - 1] > a[i]:
            temp = a[i]
            j = i - 1
            while j >= 0 and temp < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = temp
        for j in xrange(m):
            print a[j],
        print ""
            
        
        
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar, m)
