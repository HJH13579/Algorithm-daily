import sys

sys.stdin = open("s_input.txt", "r")

def my_max(lst):
    max_height = 0

    for i in range(len(lst)):
        if max_height < lst[i]:
            max_height = lst[i]

    return max_height

def my_min(lst):
    min_height = 100

    for j in range(len(lst)):
        if min_height > lst[j]:
            min_height = lst[j]

    return min_height


for tck in range(1, 11):
    dump_num = int(input())
    height_lst = list(map(int, input().split()))

    for _ in range(dump_num):

        mx = my_max(height_lst)
        mn = my_min(height_lst)

        mx -= 1
        mn += 1

        result = mx - mn

        for i in range(100):
            if height_lst[i] == mx + 1:
                height_lst[i] -= 1
                continue




        if my_max(height_lst) - my_min(height_lst) <= 1:    # 높이 차가 1 이하일 경우 pass
            break

    print(f'#{tck} {a}')