N = input()
a = map(int, raw_input().strip().split())

def quicksort( start, end, a ):
    if start >= end:
        return
    
    first = start
    last = end
    key = a[first]
    
    while first  < last:
        while first < last and a[last] >= key:
            last -= 1
        a[first] = a[last]
        
        while first < last and a[first] <= key:
            first += 1
        a[last] = a[first]
        
    a[first] = key
    
    quicksort( start, first - 1, a )
    quicksort( first + 1, end, a )
    
    for i in xrange( start, end + 1 ):
        print a[i],
    print ""
    
quicksort(0, N - 1, a)