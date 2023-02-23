# '(' incomming 때는 가장 높은 우선순위=>무조건 스택에 push
# '(' in stack 경우에는 가장 낮은 우선순위=>그래야 ')' 나올때까지 스택에서 pop되지 않음
icp = {'(': 3, '*': 2, '+': 1}
isp = {'*': 2, '+': 1, '(': 0}
T = 10
for tc in range(1, T + 1):
    _ = input()
    st = input()
    # [1] 중위표기식 => 후위표기식 변환
    stk = []
    equ = ""
    ans = 0
    for ch in st:
        if ch.isdigit():  # 숫자인 경우 equ추가
            equ += ch
        else:
            # if ch=='(':     # 무조건 스택에 저장
            #     stk.append(ch)
            # elif ch==')':   # '(' 만날때까지 모두 pop해서 equ추가, '('제거
            if ch == ')':  # '(' 만날때까지 모두 pop해서 equ추가, '('제거
                while stk:
                    t = stk.pop()
                    if t == '(':  # 괄호연산 완료
                        break
                    else:
                        equ += t
            else:
                while stk and icp[ch] <= isp[stk[-1]]:
                    equ += stk.pop()
                stk.append(ch)
    while stk:
        equ += stk.pop()

    # [2] 후위표기식을 연산
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
                    ans = -1  # 이 경우는 발생하지 않음
            else:
                ans = -1  # 이 경우는 발생하지 않음
    if ans != -1:
        ans = stk.pop()
    print(f'#{tc} {ans}')