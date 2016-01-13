#Reverse Shuffle Merge
text = raw_input().strip()
textlist = list(text)
textlist.sort()
length = len(text)
maxA = [textlist[length - i - 1] for i in xrange(0, length, 2) ]
findlen = len(maxA)

#print maxA
used = [False for i in xrange(length)]
findindex = []

for i in xrange(findlen):
    if i == 0:
        index = text.find(maxA[i])
        used[index] = True
        findindex.append(index)
        continue
    index = text[findindex[-1] + 1:].find(maxA[i])
    if index != -1:
        used[index + findindex[-1] + 1] = True
        findindex.append(index + findindex[-1] + 1)
        continue
    index = text[:findindex[-1]].find(maxA[i])
    used[index] = True
    findindex.append(index)

#print findindex
answer = ""
for i in xrange(length):
    if used[i] == True:
        answer += text[i]
print answer[::-1]
