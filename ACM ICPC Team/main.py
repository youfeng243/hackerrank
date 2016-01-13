#coding=utf-8
#!/bin/python

import sys

def comb( str1, str2, length ):

    cnt = 0
    str3 = ""
    for i in xrange(length):
        if str1[i] == '1' or str2[i] == '1':
            str3 += "1"
            cnt += 1
        else:
            str3 += "0"
    return cnt, str3
n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    topic.append(topic_t)

dic = {}
maxtopic = 0
for i in xrange(n):
    for j in xrange(i, n):
        cnt, string = comb(topic[i], topic[j], m) #返回合成的字符串 以及技能个数
        if cnt > maxtopic:
            maxtopic = cnt
        if cnt not in dic:
            dic[cnt] = []
        dic[cnt].append(string)
        
print maxtopic
print len(dic[maxtopic])
