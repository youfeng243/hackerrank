
def main():
    N = input()
    
    A = map(int, raw_input().strip().split())
    
    for i in xrange(N - 1, -1, -1):
        print A[i],
        
        
if __name__=="__main__":
    main()