import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    input_lst = list(map(int, input().split())) # 입력 배열

    # N은 5 이상 50 이하
    # lst 값은 0 이상 100 이하 값

    # [1] 빈도수 배열에 표시 및 누적 cnts
    count_lst = [0] * 101 # 카운트 배열
    temp_lst = [0] * N

    for i in range(N):
        count_lst[input_lst[i]] += 1

    for x in range(1, 101):
        count_lst[x] += count_lst[x - 1]

    # [2] 새로운 배열 생성, 위치에 맞게 저장
    for y in range(N - 1, -1, -1):
        count_lst[input_lst[y]] -= 1    # 저장 위치값 및 개수 1 감소
        temp_lst[count_lst[input_lst[y]]] = input_lst[y]    # 해당 위치에 숫자 저장


    print(f'#{tck}', *temp_lst)