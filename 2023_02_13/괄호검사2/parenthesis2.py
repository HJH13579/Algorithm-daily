import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    result = 1  # 시작부터 ')'나 '}' 박고 시작해도 result = 0으로 break되서 그대로 초기 상태 유지, 조건(top == -1 and stack[-1] == 0)이 성립

    lst = list(input())
    size = len(lst)

    stack = [0] * size
    top = -1

    for x in lst:
        if x == '(':
            top += 1
            stack[top] = '('
        elif x == '{':
            top += 1
            stack[top] = '{'
        elif x == ')':
            if stack[top] == '(':
                top -= 1
                stack[top + 1] = 0
            else:
                result = 0
                break
        elif x == '}':
            if stack[top] == '{':
                top -= 1
                stack[top + 1] = 0
            else:
                result = 0
                break
        else:
            continue

    if result != 0 and top == -1 and stack[top] == 0:   # break되어서 result 0이 1로 바뀌는 걸 방지하기 위해서 result 초기값을 1로 부여, 만약 1이 아니면 성립 안 하도록 조치
        result = 1
    else:
        result = 0

    print(f'#{tck} {result}')