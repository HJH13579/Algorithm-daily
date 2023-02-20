# 영역 풀이
def count(arr, si, sj):
    cnt = 0
    for i in range(si - 1, si + 2):
        for j in range(sj - 1, sj + 2):
            if arr[si][sj] > arr[i][j]:
                cnt += 1
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[10] * (M + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (M + 2)]
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            cnt = count(arr, i, j)
            if cnt >= 4:
                ans += 1

    print(f'#{test_case} {ans}')


# 방향 풀이
def count_delta(arr, si, sj):
    cnt = 0
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni, nj = si + di, sj + dj
        if arr[si][sj] > arr[ni][nj]:
            cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[10] * (M + 2)] + [[10] + list(map(int, input().split())) + [10] for _ in range(N)] + [[10] * (M + 2)]
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            cnt = count_delta(arr, i, j)
            if cnt >= 4:
                ans += 1

    print(f'#{test_case} {ans}')