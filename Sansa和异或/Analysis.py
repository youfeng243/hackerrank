def main():
    while True:
        N = input()
        a = [i for i in xrange(1, N + 1)]
        dic = {}
        for i in xrange( 1, N + 1 ):
            for j in xrange( N - i + 1 ):
                for k in xrange( j, j + i ):
                    if a[k] in dic:
                        dic[a[k]] += 1
                    else:
                        dic[a[k]] = 1
        
        for i in xrange(N):
            print a[i],
        print ""
        
        for i in xrange(N):
            print dic[a[i]],
        print ""
            
        
    
if __name__ == "__main__":
    main()