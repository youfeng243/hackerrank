
def main():
    T = input()
    Q = []
    
    Max = 0
    for _ in xrange(T):
        Q.append(input())
    Max = max(Q)
    
    S = [0] * (Max + 1)
    for i in xrange( 1, Max + 1 ):
        S[i] = i * i
    
    for i in xrange( 2, Max + 1 ):
        S[i] += S[i - 1]
    
    for i in xrange(T):
        print ( (1 + Q[i]) * Q[i] / 2 ) ** 2 - S[Q[i]]
        
    
if __name__=="__main__":
    main()