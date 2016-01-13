#Make it Anagram
N = input()

for t0 in xrange(N):
    text = raw_input()
    length = len(text)
    if length % 2 == 1:
        print -1
        continue
    str1 = text[0:length / 2]
    str2 = text[length / 2: ]
    teststr = str1[:]
    #print str1
    #print str2
    for i in teststr:
        find1 = str1.find(i)
        find2 = str2.find(i)
        if find1 != -1 and find2 != -1:
            str1 = str1[0:find1] + str1[find1 + 1 :]
            str2 = str2[0:find2] + str2[find2 + 1 :]
    print len(str1)
