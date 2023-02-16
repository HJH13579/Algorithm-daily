pri = {'+': 1, '*': 2}  # 높은 숫자가 높은 우선순위
T = int(input())
for test_case in range(1, T + 1):
    st = input()
    equ = ""
    stk = []

    for ch in st:
        if ch.isdigit():  # 숫자인 경우
            equ += ch
        else:  # 연산자인 경우
            # 나보다 높은 우선순위(같거나 높은)인 경우 순서대로 pop()해서 eq에 추가
            while stk and pri[ch] <= pri[stk[-1]]:  # 스택을 사용하기 전에는 항상 if stk:
                equ += stk.pop()
            stk.append(ch)

    # 모든 처리후 stk에 남아있는 연산자를 차례로 eq 추가
    while stk:
        equ += stk.pop()

    print(f'#{test_case} {equ}')