import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 집 수
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

    # 모든 집이 비용을 지불해도 할 수 있는 최대 크기의 운영(최대 K)
    k = 1
    while cnt * M - (k*k + (k-1)*(k-1)) >= 0:
        k += 1

    max_K = k-1

    # 최대 K의 중앙을 arr에 전체로 돌려가면서 안에 있는 집 counting
    # K의 범위 표현 : - (max_K-1) <= x + y <= (max_K-1)

    for i in range(N):
        for j in range(N):
            arr_K = [[0]*N for _ in range(N)]
            if


    print(f'#{tck} {cnt} {k} {arr_K}')