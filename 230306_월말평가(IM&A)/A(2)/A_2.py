# 장기 포 게임
import sys
sys.stdin = open("sample_input.txt", "r")


def rock_game(N, arr, idx_i, idx_j):
    # 알을 찾고, 찾은 알 이후 그 다음 알/벽면까지 이동 가능
    for di, dj in [(1, 0), (-1, 0)]:
        for n in range(1, N):
            ni = idx_i + di*n
            if 0 <= ni < N and arr[ni][idx_j] == 1:
                for _ in range(ni+1, N):
                    if



    # 이동 후 또 탐색(DFS)

    # 3번 반복했을 때 잡을 수 있는 알의 개수



T = int(input())

for tck in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # 포 찾기(2)
    idx_i = 0
    idx_j = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                idx_i = i
                idx_j = j

    print(f'#{tck} {visited}')