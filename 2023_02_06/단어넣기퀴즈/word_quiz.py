import sys

sys.stdin = open("s_input.txt", "r")

# [1] K개의 칸이 연속으로 1

# [2] K개의 칸 양 옆으로 0 또는 벽면이 존재

def ans_count(ar, n, k):

    count_num = 0

    for i in range(1, n + 1):
        for j in range(1, n - k + 2):
            check_num = 0
            if ar[i][j - 1] == 0 and ar[i][k + j] == 0:
                for s in range(k):
                    if ar[i][s + j] == 1:
                        check_num += 1
                if check_num == k:
                    count_num += 1

    return count_num

T = int(input())

for tck in range(1, T+1):

    N, K = map(int, input().split())

    # 벽면 처리를 위해 padding
    arr1 = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]

    # 가로 방향
    ans_row = ans_count(arr1, N, K)

    # 세로 방향
    # 가로, 세로를 대칭되게 바꿔서 함수 하나로 해결
    arr2 = [[0] * (N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            arr2[i][j] = arr1[j][i]

    ans_column = ans_count(arr2, N, K)

    ans = ans_row + ans_column

    print(f'#{tck} {ans}')