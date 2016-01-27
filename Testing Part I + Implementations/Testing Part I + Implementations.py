#coding=utf-8
def main():
    curD, curM, curY = map(int, raw_input().strip().split())
    D,M,Y = map(int, raw_input().strip().split())
    if curY > Y:
        print 10000
        return
    
    if curM > M:
        print (curM - M) * 500
        return
    
    if curD > D:
        print (curD - D) * 15
        return
    
    print 0
    
if __name__=="__main__":
    main()