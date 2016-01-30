import copy

class DFS( object ):
    def __init__( self, Map, N, M ):
        self.Map = copy.deepcopy(Map)
        self.N = N
        self.M = M
        self.Max = 1
        self.dirty = [ [0 for i in xrange(M)] for j in xrange(N) ]
        self.curFirst = 0
        
        self.search()
        
        
    def search( self ):
        for i in xrange( self.N ):
            for j in xrange( self.M ):
                #print i,j
                if self.Map[i][j] == "B":
                    continue
                self.dirty[i][j] = 1
                self.curFirst = 1
                for k in xrange(1, self.M * self.N):
                    if i + k >= self.N or i - k < 0 or j + k >= self.M or j - k < 0:
                        break
                    if self.Map[i - k][j] == "B":
                        break
                    if self.Map[i + k][j] == "B":
                        break
                    if self.Map[i][j - k] == "B":
                        break
                    if self.Map[i][j + k] == "B":
                        break
                    self.curFirst += 4
                    self.dirty[i - k][j] = 1
                    self.dirty[i + k][j] = 1
                    self.dirty[i][j - k] = 1
                    self.dirty[i][j + k] = 1
                    self.searchSecond()
                self.dirty = [ [0 for _ in xrange(self.M)] for _ in xrange(self.N) ]
    
    def searchSecond( self ):
        used = [ [0 for i in xrange(self.M)] for j in xrange(self.N) ]
        for i in xrange( self.N ):
            for j in xrange( self.M ):
                if self.Map[i][j] == "B":
                    continue
                if self.dirty[i][j] == 1:
                    continue
                curarea = 1
                self.Max = max( self.Max, curarea * self.curFirst )
                for k in xrange(1, self.M * self.N):
                    if i + k >= self.N or i - k < 0 or j + k >= self.M or j - k < 0:
                        break
                    if self.Map[i - k][j] == "B" or self.dirty[i - k][j] == 1:
                        break
                    if self.Map[i + k][j] == "B" or self.dirty[i + k][j] == 1:
                        break
                    if self.Map[i][j - k] == "B" or self.dirty[i][j - k] == 1:
                        break
                    if self.Map[i][j + k] == "B" or self.dirty[i][j + k] == 1:
                        break
                    curarea += 4
                    self.Max = max( self.Max, curarea * self.curFirst )
        
    def printAns(self):
        print self.Max
        

def main():
    N,M = map(int, raw_input().strip().split())
    Map = []
    for i in xrange(N):
        temp = list(raw_input().strip())
        Map.append(temp)
    
    dfs = DFS(Map, N, M)
    dfs.printAns()
    
            
if __name__=="__main__":
    main()