import sys

sys.stdin = open("input.txt", "r", encoding="UTF8")

for tck in range(1, 11):
    L = int(input())

    arr1 = [list(input()) for _ in range(8)]
    arr2 = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            arr2[i][j] = arr1[j][i]

    cnt = 0

    # 가로 회문 체크
    for i in range(8):
        for j in range(8 - L + 1):
            if arr1[i][j:j+L] == arr1[i][j:j+L][::-1]:
                cnt += 1

    # 세로 회문 체크
    for i in range(8):
        for j in range(8 - L + 1):
            if arr2[i][j:j+L] == arr2[i][j:j+L][::-1]:
                cnt += 1

    print(f'#{tck} {cnt}')