import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    print(f'#{tck}', *lst)
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    print(f'#{tck}', *lst)
