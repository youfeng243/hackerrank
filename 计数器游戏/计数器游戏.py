#coding=utf-8

T = input()
for _ in xrange(T):

    N = input()
    bitmask = [0]
    temp = 1
    for i in xrange(65):
        bitmask.append(temp)
        temp <<= 1
        temp |= 1
    answer = 1

    if N == 1:
        if answer == 1:
            print "Louise"
        else:
            print "Richard"
    else:
        while True:
            
            length = len(bin(N)[2:])
            if N & bitmask[length - 1] > 0:
                N = N & bitmask[length - 1]
            else:
                N /= 2
            if N == 1:
                if answer == 1:
                    print "Louise"
                else:
                    print "Richard"
                break
            answer = -answer