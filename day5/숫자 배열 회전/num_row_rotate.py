import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

def degree_90(lst, n):
    rotate_lst = [[0] * n for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rotate_lst[j][N - 1 - i] = lst[i][j]

    return rotate_lst

for tck in range(1, T+1):

    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    lst_90 = degree_90(arr, N)
    lst_180 = degree_90(lst_90, N) # 90도 두번 돌리면 180도
    lst_270 = degree_90(lst_180, N) # 180도에서 90도 돌리면 270도

    print(f'#{tck}')

    for x in range(N):
            print(*lst_90[x], sep='', end=' ')
            print(*lst_180[x], sep='', end=' ')
            print(*lst_270[x], sep='')
