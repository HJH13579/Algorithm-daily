import sys
sys.stdin = open("input.txt", "r")

priority = {'+': 1, '-':1, '*': 2, '/':2}

for tck in range(1, 11):
    N = int(input())
    string = input()

    equ = ''
    stk = []

    # [1] 후위표기식 표기
    for x in string:
        if x.isdigit():
            equ += x
        else:
            while stk and priority[x] <= priority[stk[-1]]:
                equ += stk.pop()
            stk.append(x)

    while stk:
        equ += stk.pop()

    print(f'#{tck} {equ}')






    print(f'#{tck} {string}')