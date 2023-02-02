import sys

sys.stdin = open("s_input.txt", "r")

for tck in range(1, 11):
    dump_num = int(input())
    height_lst = list(map(int, input().split()))

    max_height = 1
    min_height = 100


    for x in range(dump_num):


    for i in range(100):
        if max_height < height_lst[i]:
            max_height = height_lst[i]

    for j in range(100):
        if min_height > height_lst[j]:
            min_height = height_lst[j]



    print(f'#{tck} {max_height}')