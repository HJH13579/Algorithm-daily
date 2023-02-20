import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())

        adjL[v1].append(v2)

    c1, c2 = map(int, input().split())

    stack = []
    visited = [False for _ in range(V)]

    v = c1
    visited[c1 - 1] = True

    while 1:
        if v == c2:
            result = 1
            break

        for w in adjL[v]:
            if visited[w-1] == False:
                stack.append(v)
                v = w
                visited[w-1] = True
                break

        else:
            if stack:
                v = stack[-1]
                stack.pop()
            else:
                result = 0
                break

    print(f'#{tck} {adjL}')
