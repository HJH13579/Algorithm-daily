import sys
sys.stdin = open("s_input.txt", "r")

def min_array_sum(i, n, sm):
    global ans

    if i == n:
        if ans > sm:
            ans = sm
        return
    else:
        mn = 9
        j_mn = 0
        for j in range(n):
            if mn > arr[i][j] and column_arr[j] == 0:
                mn = arr[i][j]
                j_mn = j

            column_arr[j_mn] = 1

            min_array_sum(i+1, n, sm + arr[i][j_mn])

            column_arr[j_mn] = 0

            # min_array_sum(i+1, n, arr[i][j_mn])


T = int(input())

for tck in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    column_arr = [0] * 10

    ans = 10
    min_array_sum(0, N, 0)

    print(f'#{tck} {ans}')

