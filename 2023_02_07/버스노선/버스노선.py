import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    lst = [0] * 5001

    N = int(input())

    cnt = 0

    for n in range(N):
        A, B = map(int, input().split())

        for x in range(A, B + 1):
            lst[x] += 1

    P = int(input())

    station_lst = []

    for p in range(P):
        C = int(input())
        station_lst.append(lst[C])

    print(f'#{tck}', *station_lst, end=' ')