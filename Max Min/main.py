#Max Min
N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()
min_diff = 10**9


for i in xrange(0, N - K + 1):
    min_diff = min(min_diff, lists[i + K - 1] - lists[i])

    

    
print min_diff
