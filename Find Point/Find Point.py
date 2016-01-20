#coding=utf-8
#Find Point

T = input()
for _ in xrange(T):
    Px,Py,Qx,Qy = map(int, raw_input().strip().split())
    x = 2 * Qx - Px
    y = 2 * Qy - Py
    print x, y