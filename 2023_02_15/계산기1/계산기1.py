import sys
sys.stdin = open("input.txt", "r")

for tck in range(1, 11):
    N = int(input())

    string = input()

    eq = ''
    stk = []

    # [1] 후위 표기식
    for x in string:
        if x.isdigit():
            eq += x
        else:
            if stk:
                eq += stk.pop()

            stk.append(x)

    while stk:
        eq += stk.pop()

    print(f'#{tck} {eq}')

    # [2] 후위 표기식 계산
    for i 