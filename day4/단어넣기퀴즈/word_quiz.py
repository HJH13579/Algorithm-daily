import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    count_num = 0

    # [1] K개의 칸이 연속으로 1

    # [2] K개의 칸 양 옆으로 0 또는 벽면이 존재

    # 가로 방향
    for i in range(N):
        for j in range(N - K + 1):
            if (arr[i][j] == arr[i][j + 1] == arr[i][j + 2] == 1) and (arr[i][j - 1] == 0) and (arr[i][j + 1] == 0):
                count_num += 1
            else:
                pass

    # 세로 방향
    for j in range(N):
        for i in range(N - K + 1):
            if (arr[i][j] == arr[i + 1][j] == arr[i + 2][j] == 1) and (arr[i - 1][j] == 0 or i < 1) and (arr[i + 1][j] == 0 or i > N - 1):
                count_num += 1
            else:
                pass

    print(f'#{tck} {count_num}')