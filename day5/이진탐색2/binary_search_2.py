import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

def binary_search(p, k):
    start = 1
    end = p
    cnt = 0

    while start <= end:
        c = int((start + end) / 2)
        if c > k:
            end = c
        elif c < k:
            start = c
        else: # c == k
            return cnt
        cnt += 1

    return 0


for tck in range(1, T+1):
    P, A, B = map(int, input().split())

    a = binary_search(P, A)
    b = binary_search(P, B)

    if a < b:
        result = 'A'
    elif a > b:
        result = 'B'
    else: # a = b
        result = 0

    print(f'#{tck} {result}')