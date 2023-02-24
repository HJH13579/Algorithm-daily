import sys
sys.stdin = open("sample_input.txt", "r")

def home_service(arr, N, M, max_K):
    # 최대 K의 중앙을 arr에 전체로 돌려가면서 안에 있는 집 counting
    # K의 범위 표현

    mx_house = 0

    # K 범위 표현
    for x in range(N):
        for y in range(N):
            arr_ser = [[0] * N for _ in range(N)]   # K 전용 arr
            for i in range(-(max_K - 1), max_K):
                for j in range(-(max_K - 1), max_K):
                    if 0 <= abs(i) + abs(j) <= (max_K - 1) and 0 <= i + x < N and 0 <= j + y < N:
                        arr_ser[i + x][j + y] = 1

            cnt_house = 0

            for m in range(N):
                for n in range(N):
                    if arr_ser[m][n] == 1 and arr[m][n] == 1:   # K 범위 내 & 집이 있는 경우
                        cnt_house += 1

            if mx_house < cnt_house:
                mx_house = cnt_house

    if mx_house * M >= (max_K * max_K + (max_K - 1) * (max_K - 1)): # 재귀 탈출 조건 : 수익 >= 비용
        return mx_house

    return home_service(arr, N, M, max_K - 1)   # 수익 < 비용 : 운영 크기 -1

    # 최대 서비스 집의 수익 >= 운영 비용 검사
    # 안 되면 운영을 줄여가며 반복

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
    # K의 범위 표현

    print(f'#{tck} {home_service(arr, N, M, max_K)}')