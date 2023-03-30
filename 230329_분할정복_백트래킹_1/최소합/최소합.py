import sys
sys.stdin = open("s_input.txt", "r")

def dfs(x, y, sm):
    global ans
    if ans <= sm:
        return

    if (x, y) == (N-1, N) or (x, y) == (N, N-1):
        ans = min(ans, sm)
        return

    else:
        if x < N and y < N:
            dfs(x+1, y, sm+arr[x][y])
            dfs(x, y+1, sm+arr[x][y])


T = int(input())

for tck in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N * N

    dfs(0, 0, 0)

    print(f'#{tck} {ans}')