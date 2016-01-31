#coding=utf-8
N = input()
a = map(int, raw_input().strip().split())

def quicksort( low, high, a ):
    if low >= high:
        return
    key = a[low]
    
    i = high
    j = high
    while j > low:
        if a[j] > key:
            a[j], a[i] = a[i], a[j]
            i -= 1
        j -= 1
    a[i], a[low] = a[low], a[i]
    '''
    for j in xrange(low, high):
        if a[j] <= key:
            a[j], a[i] = a[i], a[j]
            i += 1
        for k in xrange( low, high + 1):
            print a[k],
        print ""
    
    a[i], a[high] = a[high], a[i]
    '''
    
    '''
    print "操作完成一次:"
    for k in xrange( low, high + 1):
        print a[k],
    print ""
    '''
    
    quicksort(low, i - 1, a)
    quicksort(i + 1, high, a)
    
    for k in xrange( low, high + 1):
        print a[k],
    print ""
    
quicksort( 0, N - 1, a )

print "最后结果:"
for k in xrange( 0, N):
    print a[k],
print ""