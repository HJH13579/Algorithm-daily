import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    lst = list(map(int, input()))

    counts_lst = [0] * 12

    for i in range(6):
        counts_lst[lst[i]] += 1

    running = 0
    triplet = 0

    while (1):
        for x in range(12):
            if counts_lst[x] >= 3:
                counts_lst[x] -= 3
                triplet += 1
                continue    # 반복문 다시 돌리기

        for y in range(10):
            if counts_lst[y] >= 1 and counts_lst[y + 1] >= 1 and counts_lst[y + 2] >= 1:
                counts_lst[y] -= 1
                counts_lst[y + 1] -= 1
                counts_lst[y + 2] -= 1
                running += 1
                continue

        else:
            break

    if triplet + running == 2:
        result = 1
    else:
        result = 0

    print(f'#{tck} {result}')