import os
import copy

class Robot(object):
    def __init__(self, graph):
        self.graph = copy.deepcopy(graph)
    
        
    
    def Print(self):
        for i in self.graph:
            print i
    
def main():
    player = input()
    graph = []
    for i in xrange(3):
        text = raw_input().strip()
        graph.append(list(text))    
    robot = Robot(graph)
    #robot.Print()
    

if __name__ == "__main__":
    main()
