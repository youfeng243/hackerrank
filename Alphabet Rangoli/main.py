#coding=utf-8
from __future__ import print_function

def main():
    N = int( open("./in.txt").read() )
    
    dic = [ chr(ord('a') + i) for i in xrange(26) ]

    charlist = []
    for i in xrange( N ):
        k = N - 1
        templist = []
        M = i * 2 + 1
        for j in xrange(M):
            if j < M / 2:
                templist.append(dic[k])
                k -= 1
            elif j == M / 2:
                templist.append(dic[k])
            else:
                k += 1
                templist.append(dic[k])
        charlist.append("-".join(templist))

    #print (charlist)
    
    for i in xrange( N - 1 ):
        k = N - 1
        templist = []
        M = (N - i - 1) * 2 - 1
        for j in xrange(M):
            if j < M / 2:
                templist.append(dic[k])
                k -= 1
            elif j == M / 2:
                templist.append(dic[k])
            else:
                k += 1
                templist.append(dic[k])
        charlist.append("-".join(templist))
    #print (charlist)
    
    for i in xrange( N - 1 ):
        print( "-" * (N - i - 1) * 2,sep = "", end = "")
        print( charlist[i],sep = "", end = "")
        print( "-" * (N - i - 1) * 2)

    print (charlist[N - 1])
        
    for i in xrange( N - 1 ):
        print ("-" * (i + 1) * 2,sep = "", end = "")
        print (charlist[N + i],sep = "", end = "")
        print ("-" * (i + 1) * 2)
    

if __name__ == "__main__":
    main()
