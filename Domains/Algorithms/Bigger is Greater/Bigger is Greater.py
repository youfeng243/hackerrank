#coding=utf-8
#Bigger is Greater

def find( start, end, c, string ):
    Max = '1'
    index = start - 1
    for i in xrange(start, end + 1):
        if string[i] > c:
            if Max == '1':
                Max = string[i]
                index = i
                continue
            if string[i] <= Max:
                Max = string[i]
                index = i
    #print "index = ", index
    return index
    
def solve(string):
    length = len(string)
    j = length - 1
    while j > 0:
        if string[j] <= string[j - 1]:
            j -= 1
            continue
        break
    if j <= 0:
        #file.writelines("no answer\n")
        print "no answer"
        return
    
    #here  string[j] > string[j - 1]
    maxindex = find(j, length - 1, string[j - 1], string)
    
    #ΩªªªŒª÷√
    string[maxindex], string[j - 1] = string[j - 1], string[maxindex]
    
    stringtemp = string[j:]
    stringtemp.sort()
    string = string[:j] + stringtemp
    print "".join(string)
    
    #file.writelines("".join(string) + "\n")

def main():
    
    global N
    N = 0
    N = input()
    for _ in xrange(N):
        string = list(raw_input().strip())
        solve(string)
if __name__ == "__main__":
    main()
    
