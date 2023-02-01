import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())


def count(lst_1):
    num = 0

    for _ in lst_1:
        num += 1

    return num


def my_max(lst_2):
    max_num = lst_2[0]

    for i in range(1, count(lst_2)):
        if lst_2[0] < lst_2[i]:
            lst_2[0] = lst_2[i]

    return max_num


for tck in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    lst = []

    for i in range(N-1):
        cnt = 0

        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1
            else:
                break

        lst.append(cnt)

    max_gravity = my_max(lst)

    print(f'#{tck} {max_gravity}')
