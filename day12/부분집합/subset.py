import sys
sys.stdin = open("s_input.txt", "r")

def subset_sum(i, n, sm, k):
    global cnt
    bit = [0]*n

    if i == n:
        if sm == k:
            cnt += 1
        return
    else:
        bit[i] = 1
        subset_sum(i+1, n, sm + lst[i], k)
        bit[i] = 0
        subset_sum(i+1, n, sm, k)

T = int(input())

for tck in range(1, T+1):
    N, K = map(int, input().split())

    lst = list(map(int, input().split()))

    cnt = 0
    subset_sum(0, N, 0, K)

    print(f'#{tck} {cnt}')