
def main():
    N = input()
    DIC = {}
    for _ in xrange(N):
        text = raw_input().strip()
        if text in DIC:
            DIC[text] += 1
        else:
            DIC[text] = 1
    
    Q = input()
    for _ in xrange(Q):
        text = raw_input().strip()
        if text in DIC:
            print DIC[text]
        else:
            print 0
    
if __name__=="__main__":
    main()