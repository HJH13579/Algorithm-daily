import sys
sys.stdin = open("s_input.txt", "r")

A = [i for i in range(1, 13)]
L = len(A)
bit = [0]*L

def sum_of_subset(i, l, sm, k, n):
    global cnt

    bit_cnt = 0
    for j in range(l):
        if bit[j]:
            bit_cnt += 1

    if i == l:
        if sm == k and bit_cnt == n:
            cnt += 1
        return
    else:
        bit[i] = 1
        sum_of_subset(i+1, l, sm + A[i], k, n)
        bit[i] = 0
        sum_of_subset(i+1, l, sm, k, n)

T = int(input())

for tck in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    sum_of_subset(0, L, 0, K, N)

    print(f'#{tck} {cnt}')