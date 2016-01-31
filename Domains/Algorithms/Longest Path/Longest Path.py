#Longest Path
N = input()
c = map(int, raw_input().strip().split())

Max = 0
temp = 0
for i in xrange(N):
    if c[i] == 0:
        temp = 0
        continue
    temp += c[i]
    if temp > Max:
        Max = temp
        
print Max