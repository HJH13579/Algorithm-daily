import sys

sys.stdin = open("s_input.txt", "r")

def swap(ar, n):
    new_ar = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_ar[i][j] = ar[j][i]

    return new_ar

def palindrome(ar, n, m):
    result = []
    for i in range(n):
        for j in range(n - m + 1):
            lst = []
            for k in range(M):
                lst.append(ar[i][j + k])

            if lst == lst[::-1]:
                result = lst
    return result

T = int(input())

for tck in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]


    # 가로 테스트
    result_row = palindrome(arr, N, M)

    # 세로 테스트
    arr_swap = swap(arr, N)
    result_column = palindrome(arr_swap, N, M)

    if result_row == []:
        end = result_column
    else:
        end = result_row

    print(f'#{tck}', end=' ')
    print(*end, sep='')