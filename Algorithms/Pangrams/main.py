text = raw_input().strip()
text = text.lower()
alphaset = set([])
for i in text:
    if i.isalpha():
        alphaset.add(i)
#print text
#print len(alphaset)
if len(alphaset) >= 26:
    print "pangram"
else:
    print "not pangram"
