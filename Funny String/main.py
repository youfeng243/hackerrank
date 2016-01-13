#Funny String
T = input()

for i in xrange(T):
    text = raw_input().strip()
    Funny = True
    length = len(text)
    for j in xrange(1, length):
        if abs(ord(text[j - 1]) - ord(text[j])) != abs(ord(text[ - j ]) - ord(text[- j - 1])):
            Funny = False
    if Funny == True:
        print "Funny"
    else:
        print "Not Funny"
