T = input()
dic = {}
for i in xrange(T):
    name = raw_input().strip()
    phone = raw_input().strip()
    dic[name] = phone

#print dic
while True:
    try:
        name = raw_input().strip()
    except:
        break
    if name in dic:
        print name + "=" + dic[name]
    else:
        print "Not found"
