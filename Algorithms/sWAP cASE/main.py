'''
from __future__ import print_function
text = raw_input()

textlen = len(text)
for i in xrange(textlen):
    if text[i].islower():
        print (text[i].upper(),sep="",end="")
    else:
        print (text[i].lower(),sep="",end="")
        

for i in text:
    if i.islower():
        print (i.upper(),sep="",end="")
    else:
        print (i.lower(),sep="",end="")
        '''
print (''.join([ i.lower() if i.isupper() else i.upper() for i in raw_input() ]))
