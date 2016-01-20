#coding=utf-8
#Sherlock and Watson
N,K,Q = map(int, raw_input().strip().split())
A = map(int, raw_input().strip().split())
for i in xrange(Q):
    index = input()
    print A[(index - K) % N]