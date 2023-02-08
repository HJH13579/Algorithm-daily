import sys

sys.stdin = open("s_input.txt", "r")

def ans_count(ar, n, k):

    count_num = 0

    for i in range(1, n + 1):
        for j in range(1, n - k + 2):
            if (arr[i][s + j] == 1 and ar[i][s + j - 1] == 0 and ar[i][s + j + 1] == 0 for s in range(K)):
                count_num += 1

    return count_num


T = int(input())

for tck in range(1, T+1):

    N, K = map(int, input().split())

    arr = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)]

    count_num = 0

    # [1] K개의 칸이 연속으로 1

    # [2] K개의 칸 양 옆으로 0 또는 벽면이 존재

    # 벽면 처리를 위해 padding


    # 가로 방향
    ans1 = ans_count(arr, N, K)


    # 세로 방향
    ans2 = ans_count(arr, N, K)

    ans = ans1 + ans2

    print(f'#{tck} {ans}')