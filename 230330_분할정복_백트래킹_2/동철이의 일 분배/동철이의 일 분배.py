import sys
sys.stdin = open("input.txt", "r")

def dfs(n, multi):
    global ans

    # 가지치기
    # 최대값이지만, 확률이므로 최대는 1
    # 확률은 곱할 수록 항상 작아지기에
    # 현재 multi보다 ans가 클 경우 정답 갱신 가능성이 없음
    if ans >= multi:
        return

    if n == N:
        ans = max(ans, multi)
        return

    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(n+1, multi * P[n][j] / 100)
                visited[j] = 0


T = int(input())

for tck in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N

    ans = 0.000000

    dfs(0, 1)

    result = "{:.6f}".format(ans * 100)

    print(f'#{tck} {result}')