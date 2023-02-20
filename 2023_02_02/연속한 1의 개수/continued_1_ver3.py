import sys

sys.stdin = open("input1.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    ans = cnt = 0

    for i in range(N):
        if lst[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans < cnt:
                ans = cnt

    print(f'#{tck} {ans}')