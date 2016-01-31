T = input()
for i in xrange(T):
    text = list(raw_input().strip())
    length = len(text)
    pre = text[0]
    cnt = 0
    for j in xrange(1, length):
        if text[j] == pre:
            cnt += 1
            continue
        pre = text[j]
    print cnt
    
