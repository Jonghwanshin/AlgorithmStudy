s = 0
tc_num = int(input().strip())
for i in range(tc_num):
    inputs = input().strip().split()
    if(len(inputs) == 1):
        op = inputs
    else:
        op = inputs[0]
        data = int(inputs[1])
    if(op == 'add'):
        s = s | (1<<data)
    elif(op == 'check'):
        res = s & (1<<data)
        print(res>>data)
    elif(op == 'toggle'):
        s = s ^ (1<<data)
    elif(op == 'remove'):
        s = s & ~(1<<i)
    elif(op == 'all'):
        s = 1048575
    elif(op == 'empty'):
        s = 0
