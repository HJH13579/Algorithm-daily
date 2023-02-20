import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    K, N, M = map(int, input().split())
    recharge_lst = list(map(int, input().split()))

    recharge_num = 1

    ideal_recharge_lst = [0] * M

    ideal_recharge_lst[0] = recharge_lst[0]

    for j in range(1, M):
        ideal_recharge_lst[j] = ideal_recharge_lst[j - 1] + K
        recharge_num += 1

        if ideal_recharge_lst[j] >= N:
            recharge_num -= 1
            break

    if ideal_recharge_lst[len(ideal_recharge_lst) - 2] + K < N:
        recharge_num = 0

    if recharge_lst[0] > K:
        recharge_num = 0

    for i in range(M-1):
        if recharge_lst[i + 1] - recharge_lst[i] > K:
            recharge_num = 0
            break


    print(f'#{tck} {recharge_num}')