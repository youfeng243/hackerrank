import os
import copy

#有关地图信息的类
class Graph(object):
    

class Robot(object):
    def __init__(self, graph):
        self.graph = copy.deepcopy(graph)
    
    
    
def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))    
    robot = Robot(graph)
    

if __name__ == "__main__":
    main()
