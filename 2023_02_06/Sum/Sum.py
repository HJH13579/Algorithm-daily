import sys
import pprint

sys.stdin = open("s_input.txt", "r")

for tck in range(1, 11):

    dummy = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_lst = []

    # 행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]

        sum_lst.append(sum_row)

    # 열의 합
    for j in range(100):
        sum_column = 0
        for i in range(100):
            sum_column += arr[i][j]

        sum_lst.append(sum_column)


    # 대각선의 합(1)
    for x in range(100):
        sum_diagonal1 = 0
        sum_diagonal1 += arr[x][x]

        sum_lst.append(sum_diagonal1)

    # 대각선의 합(2)
    for x in range(100):
        sum_diagonal2 = 0
        sum_diagonal2 += arr[x][99-x]

        sum_lst.append(sum_diagonal2)

    mx = 0

    for a in range(len(sum_lst)):
        if mx < sum_lst[a]:
            mx = sum_lst[a]


    print(f'#{tck} {mx}')