import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M, K = map(int, input().split())

    lst = list(map(int, input().split()))

    supply_lst = [0] * 11112

    for idx in lst:
        supply_lst[idx] -= 1

    for x in range(1, 11112):
        supply_lst[x] += supply_lst[x-1]

        if x % M == 0:
            supply_lst[x] += K

    for y in supply_lst:
        if y < 0:
            ans = 'Impossible'
            break
        ans = 'Possible'

    print(f'#{tck} {ans}')


