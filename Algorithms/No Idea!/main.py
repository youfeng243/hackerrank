# Enter your code here. Read input from STDIN. Print output to STDOUT
(n, m) = map(int, raw_input().strip().split(" "))
#print n, m
array = raw_input().strip().split(" ")
#print array
A = set(raw_input().strip().split(" "))
B = set(raw_input().strip().split(" "))
#print A
#print B
cnt = 0
for i in array:
    if i in A:
        cnt += 1
    if i in B:
        cnt -= 1
print cnt
