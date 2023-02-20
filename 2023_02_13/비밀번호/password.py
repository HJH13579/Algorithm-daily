import sys

sys.stdin = open("s_input.txt", "r")

for tck in range(1, 11):
    n, m = map(str, input().split())

    N = int(n)

    stack = [0] * N
    top = -1

    for x in m:
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

    ans = []

    for y in range(len(stack)):
        if stack[y] != 0:
            ans.append(stack[y])
        else:
            break

    print(f'#{tck}', "".join(map(str, ans)))