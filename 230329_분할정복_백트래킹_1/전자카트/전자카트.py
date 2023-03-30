# 왠만하면 그림과 array를 맞추는 것이 좋다.
# padding
# visited list가 필요할 것 같다.
# 반드시 1번으로 되돌아와야한다.

import sys
sys.stdin = open("s_input.txt", "r")

def dfs(n, sm, i):
    global ans

    if ans <= sm:
        return

    if n == N:
        sm += e[i][1]
        ans = min(ans, sm)
        return

    else:
        for j in range(2, N+1):
            if visited[j] == 0:
                visited[j] = 1
                dfs(n+1, sm+e[i][j], j)
                visited[j] = 0

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    e = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 100 * N * N
    visited = [0] * (N+1)

    dfs(1, 0, 1)

    print(f'#{tck} {ans}')