import sys
sys.stdin = open("algo2_sample_in.txt", "r")

def dfs(n, sm, i):
    global ans

    if ans <= sm:
        return

    # a보다 b를 먼저 방문했을 경우 : 가지치기
    if visited[a] == 0 and visited[b] == 1:
        return

    # N-1번째 이동까지만 count 후 stop, 마지막은 사무실로 돌아와야함으로 정해져 있음
    if n == N-1:
        ans = min(ans, sm+e[i][0])
        return

    # 마지막은 사무실로 정해져있으므로(e[i][0]), j 범위를 1~N-1까지만, visited로 방문 여부 확인
    # 도착 지점이 출발 지점으로 갱신
    for j in range(1, N):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, sm+e[i][j], j)
            visited[j] = 0

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    a, b = map(int, input().split())

    visited = [0] * N

    ans = 100 * N * N

    # 방문횟수, 배터리 사용량 합, 출발 위치
    dfs(0, 0, 0)

    print(f'#{tck} {ans}')
