N = input()
numlist = map(int, raw_input().split(" "))
numset = set(numlist)
print sum(numset) / (len(numset) * 1.0)
