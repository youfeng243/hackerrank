#coding=utf-8
#String Reduction

class Reduction(object):
    def __init__( self, string ):
        self.string = string
        self.array = [["" for i in xrange(len(string))] for j in xrange(string)]
        
        length = len( string )
        
        for i in xrange( length ):
            self.array[i][i] = string[i]
        
        for i in xrange(length - 1):
            self.array[i][i + 1] = comb( self.array[i][i], self, array[i + 1][i + 1], 1, 1 )
        
        for i in xrange( 2, length ):
            for j in xrange( length ):
                if i + j >= length:
                    break
                for k in xrange( j + 1, j + i ):
                    
                    
        def comb( a, b, lena, lenb ):
            c = ""
            i = 0
            j = lenb - 1
            while i < lena and j >= 0:
                
        
    
T = input()
for _ in xrange(T):
    Reduction(raw_input())
