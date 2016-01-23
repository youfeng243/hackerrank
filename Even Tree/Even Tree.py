import copy

class Tree(object):
    def __init__( self, N, g ):
        self.nodenum = N
        self.g = copy.deepcopy(g)
        self.used = [0 for _ in xrange(N + 1)]
        self.tree = {}
        self.cnt = 0
        self.build(1)
        self.split(1)
        
        print self.cnt
        
    def split( self, root ):
        length = len( self.tree[root] )
        for i in xrange(1, length):
            if self.tree[self.tree[root][i]][0] % 2 == 0:
                self.cnt += 1
            
            self.split( self.tree[root][i] )
            
                
        '''
        for i in self.tree:
            print i
            print self.tree[i]
        '''
        
    def build(self, root):
        self.used[root] = 1
        chirdnum = 1
        chirdlist = []
        for i in xrange( 1, self.nodenum + 1 ):
            if self.g[root][i] == 1 and self.used[i] == 0:
                chirdnum += self.build(i)
                chirdlist.append(i)
        chirdlist.insert(0, chirdnum)
        self.tree[root] = chirdlist
        return chirdnum
        
def main():
    N,M = map(int, raw_input().strip().split())
    g = [[0 for _ in xrange(N + 1)] for _ in xrange(N + 1)]

    for i in xrange(M):
        x, y = map(int, raw_input().strip().split())
        g[x][y] = g[y][x] = 1
    
    tree = Tree(N, g)
    
    
if __name__=="__main__":
    main()