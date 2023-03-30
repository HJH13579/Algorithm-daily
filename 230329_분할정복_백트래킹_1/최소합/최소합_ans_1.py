import sys
sys.stdin = open("s_input.txt", "r")

def dfs(ci, cj, sm):
    global ans
    if ans <= sm:
        return

    if (ci, cj) == (N, N):
        ans = min(ans, sm)
        return

    if ci < N:  # 아래쪽
        dfs(ci + 1, cj, sm + arr[ci + 1][cj])
    if cj < N:  # 오른쪽
        dfs(ci, cj + 1, sm + arr[ci][cj + 1])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 왼쪽 위쪽 0으로 패딩: 1,1 => N,N 그림과 매치
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    ans = 10 * 2 * N
    dfs(1, 1, arr[1][1])
    print(f'#{test_case} {ans}')