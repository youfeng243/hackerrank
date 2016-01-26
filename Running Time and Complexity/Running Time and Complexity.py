import math

def main():
    T = input()
    Q = []
    prime = [2]
    for i in xrange(T):
        Q.append(input())
    Max = int(math.sqrt(max(Q)) + 2)
    used = [0] * Max
    for i in xrange( 3, int(math.sqrt(Max) + 1), 2 ):
        if used[i] == 1:
            continue
        for j in xrange(i * i, Max, i):
            used[j] = 1
    for i in xrange( 3, Max, 2 ):
        if used[i] == 0:
            prime.append(i)
    
    #print prime
    for k in xrange(T):
        judge = True
        if Q[k] == 1:
            print "Not prime"
            continue
        for i in xrange( len(prime) ):
            if Q[k] % prime[i] == 0 and Q[k] != prime[i]:
                judge = False
                break
        if judge == True:
            print "Prime"
        else:
            print "Not prime"
    
if __name__=="__main__":
    main()