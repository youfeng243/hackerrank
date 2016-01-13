#coding=utf-8
#Common Child
str1 = raw_input().strip()
str2 = raw_input().strip()

len1 = len(str1)
len2 = len(str2)

comlist = [[0 for i in xrange(len2 + 1)] for j in xrange(len1 + 1)]
#print comlist

for i in xrange(1, len1 + 1):
    for j in xrange(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            comlist[i][j] = comlist[i - 1][j - 1] + 1
        else:
            comlist[i][j] = max(comlist[i][j - 1], comlist[i - 1][j])
print comlist[len1][len2]
