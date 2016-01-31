import math


def getPrime( Max ):
    used = [0] * ( Max + 1 )
    length = int(math.sqrt(Max) + 1)
    
    for i in xrange( 3, length, 2 ):
        if used[i] == 1:
            continue
        for j in xrange( i * i, Max, i ):
            used[j] = 1
    
    length = Max / 10
    prime = [2]
    cnt = 1
    for i in xrange( 3, Max, 2 ):
        if used[i] == 0:
            prime.append(i)
            cnt += 1
        if cnt >= length:
            break
    
    return prime
    
def main():
    T = input()
    Q = []
    for _ in xrange(T):
        Q.append(input())
        
    Max = max(Q)
    
    prime = getPrime( Max * 12 )
    
    #print len(prime)
    
    for i in xrange(T):
        print prime[Q[i] - 1]
    

if __name__=="__main__":
    main()