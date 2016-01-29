def main():
    T = input()
    for _ in xrange(T):
        N,K = map(int, raw_input().strip().split())
        Array = map(int, raw_input().strip().split())
        for i in xrange(N):
            if Array[i] <= 0:
                K -= 1
        if K <= 0:
            print "NO"
        else:
            print "YES"
        
if __name__=="__main__":
    main()