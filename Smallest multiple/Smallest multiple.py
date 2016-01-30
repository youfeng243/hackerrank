def main():
    T = input()
    for _ in xrange(T):
        N = input()
        dic = {}
        for i in xrange( 2, N + 1 ):
            temp = i
            for j in xrange( 2, N + 1 ):
                if temp < j:
                    break
                if temp % j == 0:
                    cnt = 0
                    while temp % j == 0:
                        temp /= j
                        cnt += 1
                    if j not in dic:
                        dic[j] = cnt
                    else:
                        dic[j] = max( dic[j], cnt )
        ans = 1
        for i in dic:
            ans *= i**dic[i]
        print ans
        
if __name__=="__main__":
    main()