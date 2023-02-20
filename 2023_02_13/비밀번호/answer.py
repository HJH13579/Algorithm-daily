T = 10
for test_case in range(1, T + 1):
    _ , st = input().split()
    stk = []
    for ch in st:
        if stk and ch==stk[-1]: # 같은 문자인 경우 스택에서 제거
            stk.pop()
        else:                   # 같지 않은 경우 스택에 보관
            stk.append(ch)
    print(f'#{test_case} {"".join(stk)}')
