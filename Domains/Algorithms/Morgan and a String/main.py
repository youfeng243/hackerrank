from __future__ import print_function
T = input()

for t0 in xrange(T):
    str1 = raw_input().strip()
    str2 = raw_input().strip()

    str1 += "^"
    str2 += "^"
    
    len1 = len(str1)
    len2 = len(str2)
    
    nextA = [0 for k in xrange(len1)]
    nextB = [0 for k in xrange(len2)]

    k = len1 - 2
    while k >= 0:
        if str1[k] == str1[k + 1]:
            nextA[k] = nextA[k + 1] + 1
        k -= 1

    k = len2 - 2
    while k >= 0:
        if str2[k] == str2[k + 1]:
            nextB[k] = nextB[k + 1] + 1
        k -= 1
    
    i = 0
    j = 0
    while str1[i] != "^" or str2[j] != "^":
        if str1[i] == "^":
            print (str2[j: -1], sep="", end = "")
            break
        if str2[j] == "^":
            print (str1[i: -1], sep="", end = "")
            break
        
        tempi = i
        tempj = j
        get1 = True
        while tempi < len1 and tempj < len2:

            minstep = min(nextA[tempi], nextB[tempj])
            tempi += minstep
            tempj += minstep

            if str1[tempi] == str2[tempj]:
                tempi += 1
                tempj += 1

                '''
                if tempi >= len1:
                    get1 = False
                elif tempj >= len2:
                    get1 = True
                '''
                continue
            if str1[tempi] < str2[tempj]:
                get1 = True
                break
            get1 = False
            break
        if get1 == True:
            print (str1[i], sep="", end = "")
            i += 1
        else:
            print (str2[j], sep="", end = "")
            j += 1
    print ("")
