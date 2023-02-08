import sys

sys.stdin = open("s_input.txt", "r")

dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
convert_dic = {v:k for k,v in dic.items()}

def my_sort(arr,n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

T = int(input())

for tck in range(1, T + 1):

    _, n = map(str, input().split())

    N = int(n)

    arr_gns = list(map(str, input().split()))

    arr_num = []

    for x in arr_gns:
        arr_num.append(dic[x])

    sort_arr_num = my_sort(arr_num, N)

    sort_arr_gns = []

    for y in sort_arr_num:
        sort_arr_gns.append(convert_dic[y])

    print(f'#{tck}')
    print(*sort_arr_gns)
