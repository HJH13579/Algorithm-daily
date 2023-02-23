pri = {'+': 1, '*': 2}
# T = int(input())
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    st = input()
    equ = ""
    stk = []

    # [1] 후위표기식으로 변환
    for ch in st:
        if ch.isdigit():
            equ += ch
        else:
            while stk and pri[ch] <= pri[stk[-1]]:
                equ += stk.pop()
            stk.append(ch)
    while stk:
        equ += stk.pop()

    # [2] 후위표기식 연산
    ans = 0
    for ch in equ:
        if ch.isdigit():
            stk.append(int(ch))
        else:
            if len(stk) >= 2:
                if ch == '+':
                    stk.append(stk.pop() + stk.pop())
                elif ch == '*':
                    stk.append(stk.pop() * stk.pop())
                else:
                    ans = 'error'
                    break
            else:
                ans = 'error'
                break
    if ans != 'error':
        ans = stk.pop()

    print(f'#{test_case} {ans}')