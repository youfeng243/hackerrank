
def main():
    T = input()
    for _ in xrange(T):
        N = input()
        N3 = (N - 1) / 3
        N5 = (N - 1) / 5
        N15 = (N - 1) / 15
        print 3 * ( 1 + N3 ) * N3 / 2 + 5 * ( 1 + N5 ) * N5 / 2 - 15 * (1 + N15) * N15 / 2

if __name__=="__main__":
    main()