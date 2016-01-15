#!/bin/python
def insertionSort(ar, m):
    
    temp = ar[-1]
    for i in xrange(1, m):
        if ar[-i - 1] > temp:
            ar[-i] = ar[-i - 1]
            for j in xrange(m):
                print ar[j],
            print ""
        else:
            ar[-i] = temp
            for j in xrange(m):
                print ar[j],
            print ""
            return
    ar[0] = temp
    for j in xrange(m):
        print ar[j],
    print ""
        
    #return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar, m)
