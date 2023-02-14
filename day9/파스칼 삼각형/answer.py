# arr/lst 익숙한 구조로 접근!

# 맨 위 행과 맨 왼쪽 열에 padding for 범위 체크

# arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# [1] arr[1][1] = 1
# [2] 순회
#   for i(2, N+1)
#       for j(1, i+1)

import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]
    # 문제 설명대로의 구현
    arr[1][1] = 1   # [1] 첫 줄은 항상 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            # [2] 한 행 위 왼쪽과 한 행 위 값의 합
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]


    print(f'#{tck}')
    # 모두 출력이 아닌, 0이 아닌 값만 출력(또는 범위)
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(f'{arr[i][j]}', end=' ')