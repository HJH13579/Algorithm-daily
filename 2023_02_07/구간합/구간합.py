import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # mn, mx의 초기값 설정 => 무조건 갱신되는 값
    # mx = 0 : 최대값은 항상 제일 작게
    # mn = M * 10000 : 최소값은 항상 제일 크게

    max = 0
    min = M * 10000

    for i in range(N - M + 1):
        sum_num = 0

        for j in range(i, i + M):
            sum_num += arr[j]

        if mx < sum_num:
            mx = sum_num

        if mn > sum_num:
            mn = sum_num

    print(f'#{tck} {max - min}')