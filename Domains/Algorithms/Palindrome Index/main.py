#Palindrome Index
T = input()

for t0 in xrange(T):
    text = raw_input().strip()
    length = len(text)
    i = 0
    j = length - 1

    #findflag = False
    findindex = -1
    findtemp = -1
    while i <= j:
        if text[i] == text[j]:
            i += 1
            j -= 1
            continue
        findindex = i
        findtemp = j
        i += 1
        while i <= j:
            if text[i] == text[j]:
                i += 1
                j -= 1
            else:
                break
        if i <= j:
            findindex = findtemp
            break        
        
    print findindex
        
