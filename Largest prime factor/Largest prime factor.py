import math

def getPrime( Max ):
    used = [0] * Max
    length = int(math.sqrt(Max) + 1)
    for i in xrange( 3, length, 2 ):
        if used[i] == 1:
            continue
        for j in xrange( i * i, Max, i ):
            used[j] = 1
    prime = [2]
    for i in xrange( 3, Max, 2 ):
        if used[i] == 0:
            prime.append(i)
    
    return prime
    
def main():
    T = input()
    Q = []
    for _ in xrange(T):
        Q.append(input())
    Max = max(Q)
    
    prime = getPrime( int(math.sqrt(Max) + 1) ) 
    
    length = len(prime)
    for i in xrange( T ):
        t = Q[i]
        Max = 0
        for j in xrange(length):
            if prime[j] > t:
                break
            while t % prime[j] == 0:
                t /= prime[j]
                Max = prime[j]
        
        Max = max( Max, t )
        print Max
        
        
if __name__=="__main__":
    main()