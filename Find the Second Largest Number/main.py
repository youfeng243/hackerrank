#coding=utf-8
import random

def find(first, last, k, array):
    if k < first or k >= last:
        return -1

    #生成一个随机交换位置
    index = random.randrange(first, last);

    array[first], array[index] = array[index], array[first]

    count = 0
    cnt = first
    
    for i in xrange(first, last):
        if array[first] < array[i]:
            
            
            
    return index
    

def main():

    N = input()
    text = raw_input()
    numlist = list(map(int, text.split(" ")))
    print find(0, len(numlist), 2, numlist)
    

if __name__ == "__main__":
    main()
