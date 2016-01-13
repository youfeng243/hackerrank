#Find the Second Largest Number
#coding=utf-8

def main():
    N = input()
    text = raw_input()

    numlist = list(set(map(int, text.split(" "))))

    listlen = len(numlist)
    for i in xrange(2):
        for j in xrange(i + 1, listlen):
            if numlist[i] < numlist[j]:
                numlist[i], numlist[j] = numlist[j],numlist[i]
    print numlist[1]
    '''
    for i in xrange(1, listlen):
        if numlist[i] == numlist[0]:
            continue
        print numlist[i]
        break
    '''
    

if __name__ == "__main__":
    main()
