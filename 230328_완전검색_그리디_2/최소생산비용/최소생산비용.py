import sys
sys.stdin = open("s_input.txt", "r")

def dfs(i, sm):
    global mn
    if sm > mn:
        return

    if i == N:
        if mn > sm:
            mn = sm
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(i+1, sm + arr[i][j])
                visited[j] = 0

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    mn = 99 * N

    dfs(0, 0)

    print(f'#{tck} {mn}')