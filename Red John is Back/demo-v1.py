import time
T = input()

ans = [0, 0, 0, 0, 1, 2, 2, 3, 4, 4, 6, 8, 9, 11, 15, 19, 24, 32, 42, 53, 68, 91, 119, 155,
 462, 615, 816, 1077, 1432, 1912, 2543, 3385, 4522, 6048, 8078, 10794, 14475, 19385]
 
for _ in xrange(T):
    N = input()
    time.sleep(0.5)
    print ans[N]