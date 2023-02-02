import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    lst = []
    max_num = 0

    for i in range(N):
        cnt = 0

        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                cnt += 1

        if max_num < cnt:
            max_num = cnt

    print(f'#{tck} {max_num}')
