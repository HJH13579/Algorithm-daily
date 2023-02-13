import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    stack = []
    top = -1

    print(f'#{tck}')

    for x in range(N):
        if stack == []:
            stack.append(1)
            print(*stack)
        elif stack == [1]:
            stack.append(1)
            print(*stack)
        else:
            for y in range(x):
                stack[(x-1) - y] = stack[(x-1) - y] + stack[(x-1) - y - 1]

            stack[0] = 1

            stack.append(1)
            print(*stack)


