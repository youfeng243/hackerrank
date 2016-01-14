#coding=utf-8

import copy

#�йص�ͼ��Ϣ����
class Graph(object):
    
    MAX_ROW = 5
    MAX_COL = 5
    
    CENTER_X = MAX_ROW / 2 - 1
    CENTER_Y = MAX_COL / 2 - 1
    
    def __init__(self, graph):
        self.bigmap = copy.deepcopy(graph)
        pass
    
    #������Ŀ��Ϣ�ϳ����µ�ͼ
    def combNewGraph(self, graph):
        pass
    
    #������ת��ͼ
    def rotateRight(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_COL ):
            for j in xrange( Graph.MAX_ROW ):
                temp[i][j] = self.bigmap[j][Graph.MAX_COL - i - 1]
        self.bigmap = copy.deepcopy(temp)
        
    #������ת��ͼ
    def rotateLeft(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_COL ):
            for j in xrange( Graph.MAX_ROW ):
                temp[i][j] = self.bigmap[Graph.MAX_ROW - j - 1][i]
        self.bigmap = copy.deepcopy(temp)
        
    #������ת��ͼ
    def rotateDown(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_COL ):
            for j in xrange( Graph.MAX_ROW ):
                temp[i][j] = self.bigmap[Graph.MAX_COL - i - 1][Graph.MAX_ROW - j - 1]
        self.bigmap = copy.deepcopy(temp)
    
    def printGraph(self):
        for i in xrange( Graph.MAX_COL ):
            print self.bigmap[i]
        print ""
    
    #��ͼ�ı����洢 ע����ӻ��з� ���ش��ı�
    def graphSerialization(self):
        text = ""
        for i in xrange(Graph.MAX_ROW):
            text += "".join(self.bigmap[i]) + "\n"
        return text
temp = [["1", "2", "3", "4", "5"], ["6", "7", "8", "9", "10"], ["11", "12", "13", "14", "15"],["16", "17", "18", "19", "20"],["21", "22", "23", "24", "25"]]
g = Graph(temp)
g.printGraph()
g.rotateRight()
g.printGraph()
g.rotateLeft()
g.printGraph()
g.rotateDown()
g.printGraph()