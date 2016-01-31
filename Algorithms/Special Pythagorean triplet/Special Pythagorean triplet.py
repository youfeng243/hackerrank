import math

def getNum( Num ):
    
    #print "Num =", Num
    DP = [-1] * (Num + 1)
    A = B = Num / 2 + 10
    for i in xrange( 1, A ):
        for j in xrange( i + 1, B ):
            temp = i ** 2 + j ** 2
            C = int(math.sqrt(temp))
            if C ** 2 == temp and C + i + j <= Num:
                DP[C + i + j] = max( DP[C + i + j], i * j * C )
                #print "A = %d B = %d C = %d" % (i, j, C)
                #print "A = %d B = %d C = %d" % (i, j, C)
                
    
    #print DP
    return DP

def main():
    T = input()
    Q = []
    
    for i in xrange(T):
        Q.append(input())
    Max = max(Q)
    
    DP = getNum(Max)
    for i in xrange(T):
        print DP[Q[i]]
    
if __name__=="__main__":
    main()