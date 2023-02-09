import sys

sys.stdin = open("s_input.txt", "r")

dic = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
convert_dic = {v:k for k,v in dic.items()}  # 기존의 딕셔너리의 key와 value의 위치를 바꿔서 새로운 딕셔너리 생성

# 좀 더 활용성 있고 범용적인 딕셔너리 만들기
# tbl = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# dct = {tbl[n]:n for n in range(len(tbl))}

def my_sort(arr,n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

T = int(input())

for tck in range(1, T + 1):

    _, n = map(str, input().split())    # '#tck'라는 더미 데이터를 거르기 위해 일단 str으로 받기

    N = int(n)  # 길이는 필요, str 형태의 숫자를 숫자 형태로 변환

    arr_gns = list(map(str, input().split()))

    arr_num = []    # 문자로 된 숫자를 숫자로 변환해서 넣을 리스트

    for x in arr_gns:
        arr_num.append(dic[x])  # 딕셔너리를 이용해서 문자를 숫자로 변환

    sort_arr_num = my_sort(arr_num, N)  # 오름차순 정렬

    sort_arr_gns = []   # 숫자를 문자로 다시 변환해서 넣을 리스트

    for y in sort_arr_num:
        sort_arr_gns.append(convert_dic[y]) # 딕셔너리를 이용해서 숫자를 문자로 변환

    print(f'#{tck}')
    print(*sort_arr_gns)

    # [answer]

    # # [1] cnts[] 누적표시
    # cnts = [0] * (len(tbl))
    # for st in lst:
    #     cnts[dct[st]] += 1
    #
    # # [3] 정답 문자열 완성
    # ast = ""
    # for i in range(len(tbl)):
    #     ast += (tbl[i]+" ")*cnts[0]

