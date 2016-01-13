# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
text = bin(N)[2:]
width = len(text)
for i in xrange(1, N + 1):
    num10 = str(i)
    num8 = oct(i)[1:]
    num16 = hex(i)[2:].upper()
    num2 = bin(i)[2:]
    width10 = width - len(num10)
    width8 = width - len(num8)
    width16 = width - len(num16)
    width2 = width - len(num2)
    print width10 * " " + num10 + " " + width8 * " " + num8 + " " + width16 * " " + num16 + " " + width2 * " " + num2
    #print num10, num8, num16, num2
