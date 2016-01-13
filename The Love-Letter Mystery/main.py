#The Love-Letter Mystery
T = input()
for t0 in xrange(T):
    text = raw_input().strip()
    textsum = 0
    length = len(text)
    for i in xrange(length):
        if text[i] == text[ -i - 1 ]:
            continue
        textsum += abs(ord(text[i]) - ord(text[-i - 1]))
    print textsum / 2
