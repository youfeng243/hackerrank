
def main():
    T = input()
    for _ in xrange(T):
        string = raw_input().strip()
        length = len(string)
        flag = True
        for i in xrange( 1, length ):
            if abs( ord(string[i]) - ord(string[i - 1]) ) != abs( ord(string[-i]) - ord(string[-i - 1]) ):
                flag = False
                break
        if flag == True:
            print "Funny"
        else:
            print "Not Funny"
        
if __name__ == "__main__":
    main()