#coding=utf-8

def main():
    N = int(open("./in.txt").read())

    dic = [chr(ord('a') + i) for i in xrange(26) ]

    for i in xrange( N - 1 ):
        print (N - i - 1) * 2 * '-',
        M = ( i + 1 ) * 2 - 1
        alpha = []
        for j in xrange(M):
            if j < M / 2 + 1:
                alpha.append(dic[M - j - 1])
            else:
                alpha.append(dic[j - M / 2 + 1])
        print "-".join(alpha)
    
    #print N

if __name__ == "__main__":
    main()
