string = raw_input()
 
found = False

dic = {}

for i in string:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

cnt = 0
for i in dic:
    if dic[i] % 2 == 1:
        cnt += 1
if cnt <= 1:
    found = True


if not found:
    print("NO")
else:
    print("YES")
