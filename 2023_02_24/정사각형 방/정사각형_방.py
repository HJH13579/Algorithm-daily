import sys
sys.stdin = open("s_input.txt", "r")

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def counting(i, j):
    global cnt

    for _ in range(4):
        ni = i + di[_]
        nj = j + dj[_]

        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
            cnt += 1

            counting(ni, nj)

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_cnt = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            cnt = 1
            counting(i, j)
            arr_cnt[i][j] = cnt

    mx = 0
    idx_mx = 0
    idy_mx = 0

    for x in range(N):
        for y in range(N):
            if mx < arr_cnt[x][y]:
                mx = arr_cnt[x][y]
                idx_mx = x
                idy_mx = y
            elif mx == arr_cnt[x][y]:
                if arr[idx_mx][idy_mx] > arr[x][y]:
                    idx_mx = x
                    idy_mx = y

    print(f'#{tck} {arr[idx_mx][idy_mx]} {arr_cnt[idx_mx][idy_mx]}')


