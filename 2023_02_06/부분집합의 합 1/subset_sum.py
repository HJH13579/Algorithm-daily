import sys

sys.stdin = open("s_in2.txt", "r")


T = int(input())

for tck in range(1, T+1):

    arr = list(map(int, input().split()))
    check_lst = []

    for i in range(1 << 10):  # 1<<n : 부분 집합의 개수, 0 ~ 2^n - 1
        s = 0
        for j in range(10):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번 비트가 1인 경우
                s += arr[j]
                check_lst.append(s)

    for x in check_lst:
        if x == 0:
            result = 1
            break
        else:
            result = 0

    print(f'#{tck} {result}')