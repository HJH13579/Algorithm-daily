import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]    # 첫 원소를 최대로 가정
    min_num = arr[0]    # 첫 원소를 최소로 가정

    for i in range(1, N):   # 나머지 원소와 비교
        if max_num < arr[i]: # 가정값보다 크면 갈아치우기
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i] # 가정값보다 작으면 갈아치우기

    result = max_num - min_num

    print(f'#{tck} {result}')
