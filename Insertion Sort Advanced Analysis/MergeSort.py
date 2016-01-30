def Merge( start, mid, end, List ):
    
    k = 0
    i = 0
    j = 0
    cnt = 0
    
    Left = List[start : mid + 1]
    Right = List[mid + 1 : end + 1]
    
    llen = mid - start + 1
    rlen = end - mid
    while i < llen and j < rlen:
        if Left[i] <= Right[j]:
            List[start + k] = Left[i]
            i += 1
        else:
            List[start + k] = Right[j]
            j += 1
            cnt += llen - i
        k += 1
    
    while i < llen:
        List[start + k] = Left[i]
        k += 1
        i += 1
        
    while j < rlen:
        List[start + k] = Right[j]
        k += 1
        j += 1
        
    return cnt
    
def MergeSort( start , end, List ):
    
    length = end - start + 1
    if length == 1:
        return 0
    
    cnt = 0
    mid = ( start + end ) / 2
    
    left = MergeSort( start, mid, List )
    right = MergeSort( mid + 1, end, List )
    
    cnt = Merge( start, mid, end, List )
    return cnt + left + right
    
def main():
    T = input()
    for _ in xrange(T):
        N = input()
        List = map(int, raw_input().strip().split())
        print MergeSort( 0, len(List) - 1, List )
        
if __name__=="__main__":
    main()