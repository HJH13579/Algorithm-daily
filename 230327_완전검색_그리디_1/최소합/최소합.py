import sys
sys.stdin = open("s_input.txt", "r")

def dfs(i, j, sm):
    if i == N and j == N:
        lst.append(sm)
        return

    dfs(i+1, j, sm + arr[i][j])
    dfs(i, j+1, sm + arr[i][j])


T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    lst = []

    dfs(0, 0, 0)

    print(f'#{tck} {min(lst)}')