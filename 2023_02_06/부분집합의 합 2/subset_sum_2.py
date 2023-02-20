import sys

sys.stdin = open("s_input.txt", "r")


T = int(input())

for tck in range(1, T+1):
    N, K = map(int, input().split())

    arr = []    # 1 ~ 12까지의 숫자를 원소로 가진 리스트(집합)
    for i in range(1, 13):
        arr.append(i)

    count_num = 0

    for x in range(1 << 12):
        s = 0
        cnt = 0

        for y in range(12):
            if x & (1 << y):
                cnt += 1
                s += arr[y]

        if s == K and cnt == N:
            count_num += 1

    print(f'#{tck} {count_num}')