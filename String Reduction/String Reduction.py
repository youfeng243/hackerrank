#coding=utf-8
#String Reduction

class Reduction(object):
    def __init__( self, string ):
        self.string = string
        self.array = [["" for i in xrange(len(string))] for j in xrange(string)]
        
        for i in xrange( len(string) ):
            for j in xrange(i, len(string) ):
                self.array[i][j] = string[i : j + 1]
    
    def cal( self, start, end ):
        if start == end:
            return self.array[start][end]
        
    
T = input()
for _ in xrange(T):
    Reduction(raw_input())
