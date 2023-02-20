import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())

        adjL[v1].append(v2)
        adjL[v2].append(v1)

    for lst in adjL:
        for i in range(len(lst)-1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]

    stack = []
    visited = [False for _ in range(V)]
    lst_path = []

    v = 1
    visited[v-1] = True
    lst_path.append(v)

    while 1:
        for w in adjL[v]:
            if visited[w-1] == False:
                stack.append(v)
                v = w
                visited[w-1] = True
                lst_path.append(w)
                break
        else:
            if stack:
                v = stack[-1]
                stack.pop()
            else:
                break

    print(f'#{tck}', *lst_path)