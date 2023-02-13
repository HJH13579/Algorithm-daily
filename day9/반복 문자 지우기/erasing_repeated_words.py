import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    lst = list(input())

    stack = [0] * len(lst)
    top = -1

    for x in lst:
        if top == -1:
            top += 1
            stack[top] = x
        else:
            if x != stack[top]:
                top += 1
                stack[top] = x
            else:
                top -= 1
                stack[top + 1] = 0

    cnt = 0

    for y in stack:
        if y != 0:
            cnt += 1

    print(f'#{tck} {cnt}')