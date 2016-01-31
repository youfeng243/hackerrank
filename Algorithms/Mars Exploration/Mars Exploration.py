
def main():
    string = raw_input().strip()
    length = len(string)
    
    cnt = 0
    for i in xrange( 0, length, 3 ):
        if string[i] != "S":
            cnt += 1
        if string[i + 1] != "O":
            cnt += 1
        if string[i + 2] != "S":
            cnt += 1
    print cnt

if __name__=="__main__":
    main()