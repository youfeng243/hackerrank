
def Print( A, curIndex, Size ):
    if curIndex >= Size:
        return
    
    Print( A, curIndex + 1, Size )
    print A[curIndex],
    
def main():
    N = input()
    A = map(int, raw_input().strip().split())
    
    Print(A, 0, N)

if __name__=="__main__":
    main()