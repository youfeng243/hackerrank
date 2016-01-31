#Make it Anagram
strA = raw_input().strip()
strB = raw_input().strip()

listC = list(strA)
length = len(listC)
for i in xrange(length):
    find1 = strA.find(listC[i])
    find2 = strB.find(listC[i])
    if find1 != -1 and find2 != -1:
        strA = strA[0:find1] + strA[find1 + 1 :]
        strB = strB[0:find2] + strB[find2 + 1 :]
print len(strA) + len(strB)
    
