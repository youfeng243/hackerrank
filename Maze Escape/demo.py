#coding=utf-8

import os
import copy

#有关地图信息的类
class Graph(object):
    
    MAX_ROW = 80
    MAX_COL = 80
    
    CENTER_X = MAX_ROW / 2 - 1
    CENTER_Y = MAX_COL / 2 - 1
    
    #机器人标志
    ROBOTFLAG = "b"
    
    #门的标志
    DOORFLAG = "e"
    
    #当前需要移动的目标
    DESTFLAG = "d"
    
    #存储地图的位置
    FILEPATH = r"./graph.txt"
    
    def __init__(self, graph):
        self.bigmap = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        #加载地图
        self.loadGraph()
        
        #合成最新地图
        self.combNewGraph(graph)
        
    #从存储中加载地图
    def loadGraph(self):
        m = Memory()
        
        meminfo = m.loadMemory(Graph.FILEPATH)
        if len(meminfo) <= 0:
            self.bigmap[Graph.CENTER_X][Graph.CENTER_Y] = self.ROBOTFLAG
            return
        
        for i in xrange(Graph.MAX_ROW):
            for j in xrange(Graph.MAX_COL):
                self.bigmap[i][j] = meminfo[i][j]
        
    
    #根据题目信息合成最新地图
    def combNewGraph(self, graph):
        #现在存储的地图上找到机器人的具体位置
        x,y = self.findRobot()
        if x == -1 and y == -1:
            print "ERROR!"
            raise Exception("查找RobotPosition失败")
        for i in xrange( x - 1, x + 2 ):
            for j in xrange( y - 1, y + 2 ):
                if self.bigmap[i][j] == Graph.ROBOTFLAG:
                    continue
                if self.bigmap[i][j] == Graph.DESTFLAG:
                    continue
                self.bigmap[i][j] = graph[i - (x - 1)][j - (y - 1)]
    
    #设置机器人位置
    def setRobotPosition( self, x, y ):
        tempx, tempy = self.findRobot()
        if tempx != -1 and tempy != -1:
            self.bigmap[tempx][tempy] = "-" 
        
        self.bigmap[x][y] = Graph.ROBOTFLAG
        
    #设置目标位置
    def setDestPosition( self, x, y ):
        tempx, tempy = self.findDest()
        if tempx != -1 and tempy != -1:
            self.bigmap[tempx][tempy] = "-"
        self.bigmap[x][y] = "d"
        
    #查找机器人位置
    def findRobot(self):
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                if self.bigmap[i][j] == Graph.ROBOTFLAG:
                    return i,j
        return -1, -1
    
    #查找门的位置
    def findDoor(self):
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                if self.bigmap[i][j] == Graph.DOORFLAG:
                    return i,j
        return -1, -1
    
    #查找移动目标的位置
    def findDest(self):
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                if self.bigmap[i][j] == Graph.DESTFLAG:
                    return i,j
        return -1, -1
    
    #机器人向右旋转
    def rotateRight(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                temp[i][j] = self.bigmap[j][Graph.MAX_ROW - i - 1]
        self.bigmap = copy.deepcopy(temp)
        
    #机器人向左旋转
    def rotateLeft(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                temp[i][j] = self.bigmap[Graph.MAX_COL - j - 1][i]
        self.bigmap = copy.deepcopy(temp)
        
    #机器人向下旋转
    def rotateDown(self):
        temp = [["?" for _ in xrange(Graph.MAX_COL)] for _ in xrange(Graph.MAX_ROW)]
        
        for i in xrange( Graph.MAX_ROW ):
            for j in xrange( Graph.MAX_COL ):
                temp[i][j] = self.bigmap[Graph.MAX_ROW - i - 1][Graph.MAX_COL - j - 1]
        self.bigmap = copy.deepcopy(temp)
    
    #旋转地图
    def rotateGraph( self, dirs ):
        if dirs == "UP":
            return
        if dirs == "DOWN":
            rotateDown()
            return
        if dirs == "RIGHT":
            rotateRight()
            return
        if dirs == "LEFT":
            rotateLeft()
            return
        
    #地图文本化存储 注意添加换行符 返回纯文本
    def graphSerialization(self):
        text = ""
        for i in xrange(Graph.MAX_ROW):
            text += "".join(self.bigmap[i]) + "\n"
        return text
        
#有关文件操作的类
class Memory(object):
    def __init__(self):
        pass
        
    #保存信息
    def saveMemory(self, text, fileName):
        file = open(filename, "w")
        file.writelines(text)
        file.close()
    
    #读取信息 返回字符串数组
    def loadMemory(self, fileName):
        
        textArray = []
        if os.path.exists(fileName) == False:
            return textArray
            
        file = open(fileName)
        for line in file:
            textArray.append(line.strip())
        file.close()
        
        return textArray
    
class Robot(object):
    def __init__(self, graph):
        #self.graph = copy.deepcopy(graph)
        self.graph = Graph(graph)
        
        #做决策
        self.makeDecision()
        
    #做决策
    def makeDecision(self):
        
        #先判断门是否已经出现了
        doorx, doory = self.graph.findDoor()
        if doorx != -1 and doory != -1:
            #重新设置目标位置
            self.graph.setDestPosition(doorx, doory)
            
        #找到目标位置
        destx, desty = self.graph.findDest()
        if destx == -1 and desty == -1:
            #如果当前还没有目标位置 则找到一个最近的目标位置
            destx, desty = self.robotfindDest()
            
            #记录目标点 下次走的时候继续往这个目标点前进
            self.graph.setDestPosition(destx, desty)
        
        #根据目标位置查找一个当前要走的方向
        dirs = robotBFS( destx, desty )
        
        #根据方向输出机器人移动位置
        x, y = moveRobot( dirs )
        
        #重新设置机器人位置
        self.graph.setRobotPosition(x, y)
        
        #旋转地图
        self.graph.rotateGraph(dirs)
        
        #存储地图
        mem = Memory()
        mem.saveMemory(self.graph.graphSerialization(), Graph.FILEPATH)
    
        #输出答案
        print dirs
    
    #探索离它最近的未知区域，这里已经判断过门的位置，以及目标位置，这里产生目标位置
    def robotfindDest(self):
        destx = -1
        desty = -1
        
        unknownPosition = []
        raise Exception("为完成")
    
    
    #寻路算法
    def robotBFS( destx, desty ):
        raise Exception("未完成功能")
        return "DOWN"
    
    #移动机器人
    def moveRobot( self, dirs ):
        if dirs == "DOWN":
            return moveRobot()
        if dirs == "UP":
            return moveRobot()
        if dirs == "LEFT":
            return moveLeft()
        if dirs == "RIGHT":
            return moveRight()
            
        raise Exception("move Robot Error")
        return "ERROR"
        
    #向右移动
    def moveRight(self):
        #先获得机器人当前位置
        x,y = self.graph.findRobot()
        if x == -1 and y == -1:
            raise Exception("移动时寻找robot失败")
        
        #计算移动后机器人位置
        x, y = x, y + 1
        
        return x, y
        
    
    #向左移动
    def moveLeft(self):
        #先获得机器人当前位置
        x,y = self.graph.findRobot()
        if x == -1 and y == -1:
            raise Exception("移动时寻找robot失败")
        
        #计算移动后机器人位置
        x, y = x, y - 1
        
        return x, y
        
    #向上移动
    def moveUp(self):
        #先获得机器人当前位置
        x,y = self.graph.findRobot()
        if x == -1 and y == -1:
            raise Exception("移动时寻找robot失败")
        
        #计算移动后机器人位置
        x, y = x - 1, y
        
        return x, y
        
    #向下移动
    def moveDown(self):
        #先获得机器人当前位置
        x,y = self.graph.findRobot()
        if x == -1 and y == -1:
            raise Exception("移动时寻找robot失败")
        
        #计算移动后机器人位置
        x, y = x + 1, y
        
        return x, y
    
def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))    
    robot = Robot(graph)
    

if __name__ == "__main__":
    main()
