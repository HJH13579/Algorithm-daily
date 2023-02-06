import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):

    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    count_num = 0

    # 가로 테스트
    di = [0] * (K + 2)
    dj = []
    n = -2
    for _ in range(K + 2):
        n += 1
        dj.append(n)

    for i in range(N):
        for j in range(N):
            for k in range(K + 2):
                ni, nj = i + di[k], j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    if arr[0][0] == arr[0][K + 1] == 0 and [arr[0][x] for x in range(1, K + 1)] == 1:
                        count_num += 1
                elif arr[0][0] < 0:
                    if arr[0][K + 1] == 0 and [arr[0][x] for x in range(1, K + 1)] == 1:
                        count_num += 1
                elif arr[0][K + 1] > N:
                    if arr[0][0] == 0 and [arr[0][x] for x in range(1, K + 1)] == 1:
                        count_num += 1
                else:
                    pass

    # # 세로로 테스트
    di, dj = dj, di

    for i in range(N):
        for j in range(N):
            for k in range(K + 2):
                ni, nj = i + di[k], j + dj[k]

                if 0 <= ni < N and 0 <= nj < N:
                    if arr[0][0] == arr[K + 1][0] == 0 and [arr[x][0] for x in range(1, K + 1)] == 1:
                        count_num += 1
                elif arr[0][0] < 0:
                    if arr[K + 1][0] == 0 and [arr[x][0] for x in range(1, K + 1)] == 1:
                        count_num += 1
                elif arr[K + 1][0] > N:
                    if arr[0][0] == 0 and [arr[x][0] for x in range(1, K + 1)] == 1:
                        count_num += 1
                else:
                    pass

    print(f'#{tck} {count_num}')