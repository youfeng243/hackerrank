#Insertion Sort Advanced Analysis

def cmp( A, B ):
    if A[0] == B[0]:
        return A[1] - B[1]
    
    return A[0] - B[0]
    
def main():
    T = input()
    for _ in xrange(T):
        N = input()
        A = map(int, raw_input().strip().split())
        Array = []
        for i in xrange( N ):
            Array.append((A[i], i))
            
        Array.sort()
        Sum = 0
        for i in xrange(N):
            if Array[i][1] - i > 0:
                Sum += Array[i][1] - i
            #print Array[i][0], Array[i][1]
        
        print Sum
        
if __name__=="__main__":
    main()