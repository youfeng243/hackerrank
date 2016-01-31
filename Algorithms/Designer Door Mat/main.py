#coding=utf-8


def main():
    text = ""
    for line in open("./in.txt"):
        text += line
    N, M = map(int, text.split())

    #print N, M
    for i in xrange(N/2):
        print (N / 2 - i) * 3 * '-' + ((i + 1) * 2 - 1) * '.|.' + (N / 2 - i) * 3 * '-'
    print ( M - 7 ) / 2 * '-' + "WELCOME" + ( M - 7 ) / 2 * '-'

    for i in xrange(N/2):
        print (i + 1) * 3 * '-' + ((N/2 - i) * 2 - 1) * '.|.' + (i + 1) * 3 * '-'

if __name__ == "__main__":
    main()
