N = input()
a = map(int, raw_input().strip().split())

def quicksort( start, end, a ):
    if start >= end:
        return
    
    keyindex = start
    while True:
        index = keyindex
        
        for i in xrange( index + 1, end + 1 ):
            if a[i] < a[index]:
                a[i], a[index] = a[index], a[i]
                index = i
        if index == keyindex:
            break
        
        keyindex = index
        i = index - 1
        while i >= start:
            if a[i] > a[index]:
                a[i], a[index] = a[index], a[i]
                index = i
            i -= 1
        if index == keyindex:
            break
        keyindex = index
    '''        
    for i in xrange( start, end + 1 ):
        print a[i],
    print ""
    '''
    
    quicksort( start, keyindex - 1, a )
    quicksort( keyindex + 1, end, a )
    
    for i in xrange( start, end + 1 ):
        print a[i],
    print ""
    
quicksort(0, N - 1, a)