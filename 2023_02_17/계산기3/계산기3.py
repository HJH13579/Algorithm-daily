import sys
sys.stdin = open("input.txt", "r")

priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2} # '(' priority 값을 0으로 할당, ')'를 제외한 어떤 기호가 와도 pop이 되지 않고 그 위에 stacking

for tck in range(1, 11):
    N = int(input())
    string = input()

    equ = ''
    stk = []

    # [1] 후위표기식 변환
    # '('를 기준으로 완전 새로운 stack이 새로 만들어진다고 생각
    # '('는 무조건 스택에 추가, 그 위로 기호 stacking
    # ')'이 나타나면 '('위에 쌓인 stack들 모두 equation으로 pop, '('도 제거(pop)

    for x in string:
        if x.isdigit():
            equ += x
        elif x == '(':  # 스택에 추가
            stk.append(x)
        elif x == ')':
            while stk[-1] != '(':   # '('이 나타날 때까지 pop
                equ += stk.pop()
            stk.pop()   # '(' 제거
        else:
            while stk and priority[x] <= priority[stk[-1]]: # '('의 priority 값 할당 필요, ')'를 제외한 어떠한 기호가 와도 그 위로 stacking해야하며, ')'가 나오기 전까지 pop이 되면 안 된다.
                equ += stk.pop()
            stk.append(x)

    while stk:
        equ += stk.pop()

    # [2] 후위표기식 계산
    for y in equ:
        if y.isdigit():
            stk.append(int(y))
        else:
            if y == '+':
                stk.append(stk.pop() + stk.pop())
            elif y == '*':
                stk.append(stk.pop() * stk.pop())

    ans = stk.pop()

    print(f'#{tck} {ans}')