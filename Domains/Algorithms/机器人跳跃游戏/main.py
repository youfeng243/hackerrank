#coding=utf-8
N = input()
H = map(int, raw_input().strip().split())
MaxH = max(H)
MinH = 1

MinneedH = MaxH
while MaxH >= MinH:
    MidH = (MaxH + MinH) / 2

    across = True
    InitH = MidH
    for i in xrange(N):
        
        if InitH < 0:
            across = False
            break
        
        if InitH >= H[i]:
            InitH += InitH - H[i]
        else:
            InitH -= H[i] - InitH
            
    if across == True and InitH >= 0:
        MaxH = MidH - 1
        if MinneedH > MidH:
            MinneedH = MidH
    else:
        MinH = MidH + 1
print MinneedH

