import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    lst = list(input())
    size = len(lst)

    stack = [0] * size
    top = -1

    for x in lst:
        if x == '(':
            top += 1
            stack[top] = '('
        elif x == ')':
            top -= 1
            stack[top + 1] = 0

    if stack[-1] == 0 and top == -1:
        result = 1
    else:
        result = 0

    print(f'#{tck} {result}')