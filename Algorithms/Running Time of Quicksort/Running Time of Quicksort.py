
def Insertsort( a, N ):
    cnt = 0
    for i in xrange( 1, N ):
        j = i
        key  = a[i]
        while j > 0 and key < a[j - 1]:
            a[j] = a[j - 1]
            cnt += 1
            j -= 1
        a[j] = key
    return cnt
    

def quicksort( low, high, a ):
    if low >= high:
        return 0
    
    key = a[high]
    cnt = 0
    j = low
    for i in xrange(low, high):
        if a[i] < key:
            #if i != j:
            a[i],a[j] = a[j],a[i]
            cnt += 1
            j += 1
    #if j != high:
    a[high], a[j] = a[j], a[high]
    cnt += 1
    cnt += quicksort(low, j - 1, a)
    cnt += quicksort(j + 1, high, a)
    return cnt
    
    
def main():
    N = input()
    a = map(int, raw_input().strip().split())
    b = a[:]
    
    insertstep = Insertsort(a, N)
    quickstep = quicksort(0, N - 1, b)
    
    #print a
    #print b
    
    #print "insertstep = ", insertstep
    #print "quickstep = ", quickstep
    print insertstep - quickstep
    
if __name__=="__main__":
    main()