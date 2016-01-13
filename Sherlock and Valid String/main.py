#coding=utf-8
#Sherlock and Valid String
# Enter your code here. Read input from STDIN. Print output to STDOUT
text = raw_input()
letterlist = [0 for i in xrange(26)]
for i in text:
    letterlist[ord(i) - ord('a')] += 1
dic = {}  #dic[字母重复个数] = 字母种类

for i in xrange(26):
    if letterlist[i] == 0:
        continue
    if letterlist[i] in dic:
        dic[letterlist[i]] += 1
    else:
        dic[letterlist[i]] = 1
if len(dic) >= 3:
    print "NO"
elif len(dic) <= 1:
    print "YES"
else:
    keys = dic.keys()
    values = dic.values()

    if (keys[0] == 1 and dic[keys[0]] == 1) or (keys[1] == 1 and dic[keys[1]] == 1):
        print "YES"
    elif (keys[0] - keys[1] == 1 and dic[keys[0]] == 1) or (keys[1] - keys[0] == 1 and dic[keys[1]] == 1):
        print "YES"
    else:
        print "NO"
        
        
