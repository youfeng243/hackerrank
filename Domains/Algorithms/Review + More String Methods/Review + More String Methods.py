string = raw_input().strip()
length = len(string)
patten = r"![,?.\_'@+] "

i = 0
ans = []
while i < length:
    while i < length:
        if patten.find(string[i]) != -1:
            i += 1
            continue
        break
    temp = ""
    while i < length:
        if patten.find(string[i]) == -1:
            temp += string[i]
            i += 1
            continue
        break
    if temp != "":
        ans.append(temp)
print len(ans)
for i in ans:
    print i