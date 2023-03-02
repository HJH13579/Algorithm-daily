# 범위 한정을 하기 쉽지 않다.
#  Padding

import sys
sys.stdin = open("s_in1.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [[0]*(3*N)]*N + [[0]*N + list(map(int, input().split())) + [0]*N for _ in range(N)] + [[0]*(3*N)] * N

    mx = 0

    # '+' 형태 검사
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            sm1 = arr[i][j]
            for m in range(1, M):
                sm1 += arr[i][j+m]
                sm1 += arr[i][j-m]
            for n in range(1, M):
                sm1 += arr[i+n][j]
                sm1 += arr[i-n][j]

            if mx < sm1:
                mx = sm1

    # 'x' 형태 검사
    for i in range(N, 2*N):
        for j in range(N, 2*N):
            sm2 = arr[i][j]
            for k in range(1, M):
                sm2 += arr[i+k][j+k]
                sm2 += arr[i-k][j-k]
            for p in range(1, M):
                sm2 += arr[i+p][j-p]
                sm2 += arr[i-p][j+p]

            if mx < sm2:
                mx = sm2

    print(f'#{tck} {mx}')