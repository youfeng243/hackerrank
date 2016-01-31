text = list(raw_input().strip())

length = len(text)
cnt = 0
while cnt < length:
    while cnt < length and text[cnt] == " ":
        cnt += 1
    if cnt >= length:
        break
    text[cnt] = text[cnt].upper()
    while cnt < length and text[cnt] != " ":
        cnt += 1
print "".join(text)
