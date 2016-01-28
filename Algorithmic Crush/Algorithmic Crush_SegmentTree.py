#coding=utf-8

class Node( object ):
    def __init__(self):
        self.addmark = 0
        self.cnt = 0

class Tree( object ):
    def __init__(self, N):
        self.MAX = (N + 100) * 6
        self.Nodes = [ Node() for _ in xrange(self.MAX) ]
        
    def build( self, root, start, end ):
        if start < end:
            mid = ( start + end ) / 2
            self.build( root * 2 + 1, start, mid )
            self.build( root * 2 + 2, mid + 1, end )
            
    def pushDown( self, root ):
        if self.Nodes[root].addmark != 0:
            self.Nodes[root * 2 + 1].addmark += self.Nodes[root].addmark
            self.Nodes[root * 2 + 2].addmark += self.Nodes[root].addmark
            
            self.Nodes[root * 2 + 1].cnt += self.Nodes[root].addmark
            self.Nodes[root * 2 + 2].cnt += self.Nodes[root].addmark
            
            self.Nodes[root].addmark = 0
            
    def insert( self, root, start, end, istart, iend, cnt ):
        if start > iend or end < istart:
            return 0
        
        if start >= istart and end <= iend:
            self.Nodes[root].addmark += cnt
            self.Nodes[root].cnt += cnt
            return self.Nodes[root].cnt
        
        self.pushDown(root)
        
        mid = ( start + end ) / 2
        self.insert( root * 2 + 1, start, mid, istart, iend, cnt )
        self.insert( root * 2 + 2, mid + 1, end, istart, iend, cnt )
        
        self.Nodes[root].cnt = max( self.Nodes[root * 2 + 1].cnt, self.Nodes[root * 2 + 2].cnt )
        
        return self.Nodes[root].cnt
        
def main():
    N,M = map(int, raw_input().strip().split())
    tree = Tree(N)
    for _ in xrange( M ):
        start, end, cnt = map(int, raw_input().strip().split())
        tree.insert( 1, 1, N, start, end, cnt )
        
    print tree.Nodes[1].cnt
        
if __name__ == "__main__":
    main()