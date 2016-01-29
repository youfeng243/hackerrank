#coding=utf-8

def main():
    string = raw_input().strip()
    string = string[::-1]
    rawstring = ""
    
    Delete = [0] * 26
    for i in string:
        Delete[ord(i) - ord('a')] += 1
    
    for i in xrange(26):
        Delete[i] /= 2
    
    i = 0
    j = 0
    Find = Delete[:]
    length = len(string)
    while i < length and j < length / 2:
        
        Min = 100000
        curindex = 0
        temp = [0] * 26
        
        while i < length and j < length / 2:
            strindex = ord(string[i]) - ord('a')
            if Delete[strindex] < 0:
                break
            
            #ÅÐ¶ÏÊÇ·ñÐèÒªÑ°ÕÒ
            if Find[strindex] > 0:
                if ord(string[i]) < Min:
                    Min = ord(string[i])  
                    temp = Delete[:]
                    curindex = i + 1
                
            Delete[strindex] -= 1
            if Delete[strindex] < 0:
                break
            i += 1
        
        i = curindex
        Delete = temp[:]
        j += 1
        rawstring += chr(Min)
        Find[Min - ord('a')] -= 1
        
    print rawstring
        

if __name__=="__main__":
    main()