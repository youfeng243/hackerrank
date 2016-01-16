def  maxXor( l,  r):
    
    '''
    binstr = bin(r)[2:]
    Max = r
    length = len(binstr)
    for i in xrange(length):
        if '1' == binstr[i]:
            continue
        x = pow(2, length - 1 - i)
        if x >= l:
            Max += x
    '''
    Max = 0
    for i in xrange(l, r + 1):
        for j in xrange(i, r + 1):
            Max = max(Max, i^j)
    
    return Max

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
