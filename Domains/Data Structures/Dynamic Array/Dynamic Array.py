
def main():
    N,Q = map(int, raw_input().strip().split())
    array = [ [] for _ in xrange(N) ]
    
    lastans = 0
    for _ in xrange(Q):
        t, x, y = map(int, raw_input().strip().split())
        if t == 1:
            index = (x ^ lastans) % N
            array[index].append(y)
            continue
        
        index = (x ^ lastans) % N
        lastans = array[index][y % len(array[index])]
        print lastans
        
if __name__=="__main__":
    main()