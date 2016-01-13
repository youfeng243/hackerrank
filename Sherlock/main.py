#Sherlock
T = input()

for t0 in xrange(T):
    text = raw_input().strip()
    length = len(text)
    dic = {}
    for i in xrange(length):
        for j in xrange(i + 1, length + 1):
            textlist = list(text[i:j])
            textlist.sort()
            textlist = ''.join(textlist)
            if textlist in dic:
                dic[textlist] += 1
            else:
                dic[textlist] = 1
            #print textlist
            
    cnt = 0
    for i in dic:
        if dic[i] >= 2:
            cnt += dic[i] * (dic[i] - 1) / 2
    print cnt
