#!/bin/python

from __future__ import print_function 

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
for i in s:
    if i.isalpha() == False:
        print(i, sep="", end="")
        continue
    if i.isupper() == True:
        print (chr(ord('A') + (k + ord(i) - ord('A')) % 26 ), sep = "", end = "")
    else:
        print (chr(ord('a') + (k + ord(i) - ord('a')) % 26 ), sep = "", end = "")
    print ("")
