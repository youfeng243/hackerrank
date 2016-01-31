#coding=utf-8

A,B,N = map(int, raw_input().strip().split())

for i in xrange( 3, N + 1 ):
    C = B ** 2 + A
    A, B = B, C
print B