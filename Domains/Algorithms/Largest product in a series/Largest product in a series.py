
def main():
    T = input()
    for _ in xrange(T):
        N, K = map(int, raw_input().strip().split())
        string = raw_input().strip()
        
        Max = 0
        for i in xrange(N - K + 1):
            temp = 1
            for j in xrange(K):
                temp *= (ord(string[i + j]) - ord("0"))
            Max = max(Max, temp)
        
        print Max
        
if __name__=="__main__":
    main()