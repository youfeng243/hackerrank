
def main():
    N = input()
    A = map(int, raw_input().strip().split())
    
    A.reverse()
    for i in A:
        print i,

if __name__=="__main__":
    main()