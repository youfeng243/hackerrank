#coding=utf-8

import os
import copy

#有关地图信息的类
class Graph(object):
    
    MAX_ROW = 80
    MAX_COL = 80
    
    CENTER_X = MAX_ROW / 2 - 1
    CENTER_Y = MAX_COL / 2 - 1
    
    def __init__(self):
        self.bigmap = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        pass
    
    #根据题目信息合成最新地图
    def combNewGraph(self, graph):
        pass
    
    #向右旋转地图
    def rotateRight(self):
        pass
        
    #向左旋转地图
    def rotateLeft(self):
        pass
        
    #向下旋转地图
    def rotateDown(self):
        pass
    
    #地图文本化存储 注意添加换行符 返回纯文本
    def graphSerialization(self):
        pass
    
#有关文件操作的类
class File(object):
    def __init__(self):
        pass
        
    #保存信息
    def saveFile(self, text):
        pass
    
    #读取信息 返回字符串数组
    def loadFile(self):
        pass
    
class Robot(object):
    def __init__(self, graph):
        self.graph = copy.deepcopy(graph)
        
        #p = Graph()
        #f = File()
        
    
    #向右移动
    def moveRight(self):
        pass
    
    #向左移动
    def moveLeft(self):
        pass
        
    #向上移动
    def moveUp(self):
        pass
        
    #向下移动
    def moveDown(self):
        pass
    
def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))    
    robot = Robot(graph)
    

if __name__ == "__main__":
    main()
